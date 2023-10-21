import argparse
import asyncio
import logging
import os
import random
import sys
import time

import aiohttp
import pyfiglet
from rich import print
from rich.logging import RichHandler

from resources.useragents import user_agents

print(f"[red]{pyfiglet.figlet_format('Dir Bruter')}[/]")


def set_loglevel(debug_mode: bool) -> logging.getLogger:
    """
    Configure and return a logging object with the specified log level.

    :param debug_mode: If True, the log level is set to "NOTSET". Otherwise, it is set to "INFO".
    :return: A logging object configured with the specified log level.
    """
    logging.basicConfig(
        level="NOTSET" if debug_mode else "INFO",
        format="%(message)s",
        handlers=[
            RichHandler(markup=True, log_time_format="%H:%M:%S", show_level=debug_mode)
        ],
    )
    return logging.getLogger("Tor2Tor")


async def fetch(session, url, headers):
    """
    Fetch URL using aiohttp

    :param session: aiohttp ClientSession
    :param url: URL to fetch
    :param headers: Request headers
    :return: Response text and status code as a tuple
    """
    async with session.get(url, headers=headers, timeout=5) as response:
        return await response.text(), response.status


async def dir_bruter(wordlist, extensions=None):
    """
    Brute force directories and files.

    :param wordlist: List of words to brute force
    :param extensions: File extensions to check, defaults to None
    """
    async with aiohttp.ClientSession() as session:
        for word in wordlist:
            word = word.strip()
            # Prepare the list of attempts based on word and extensions
            attempt_list = [f"/{word}/"] if "." not in word else [f"/{word}"]

            if extensions:
                for extension in extensions:
                    attempt_list.append(f"/{word}{extension}")

            for brute in attempt_list:
                target_url = f"{args.url.rstrip('/')}{brute}"
                headers = {"User-Agent": random.choice(user_agents)}
                try:
                    _, status = await fetch(session, target_url, headers)
                    if status == 200:
                        log.info(f"[bold][green]Found[/][/] [{status}]: {target_url}")
                        if args.output:
                            save_found_results(target_url)
                    else:
                        log.info(
                            f"[bold][yellow]Not Found[/][/] [{status}]: {target_url}"
                        )

                except Exception as e:
                    log.critical(f"{target_url}: [red]{e}[/]")


def is_valid_wordlist(wordlist: str):
    """
    Validate wordlist file path.

    :param wordlist: Wordlist file path
    :return: List of words from the wordlist
    """
    if not os.path.exists(wordlist):
        log.warning(f"The file {wordlist} does not exist.")
        sys.exit(1)
    else:
        print(f"[[green]+[/]] Wordlist: {wordlist}")
        with open(wordlist, "r") as f:
            return f.readlines()


def save_found_results(target_url):
    """
    Save found results to file.

    :param target_url: URL that was found
    """
    ts = time.localtime()
    timestamp = time.strftime("%H:%M:%S", ts)
    with open("dB_output.txt", "a") as f:
        f.write(f"[{timestamp}] : {target_url}\n")


if __name__ == "__main__":
    """Main function to parse arguments and run the brute forcer."""
    # Argument parser setup
    parser = argparse.ArgumentParser(
        description=f"DirBruter — https://github.com/rly0nheart",
        epilog=f"DirBruter is a Python-based CLI tool that looks for hidden or existing directories/files "
        f"using the brute force method. It basically works by launching a dictionary-based attack against a "
        f"webserver and analyzing its response",
    )

    parser.add_argument("url", type=str, help="Target URL")
    parser.add_argument(
        "-w",
        "--wordlist",
        type=lambda wordlist: is_valid_wordlist(wordlist=wordlist),
        help="Path to wordlist",
        metavar="<wordlist>",
        required=True,
    )
    parser.add_argument(
        "-o", "--output", help="Save found results to a file", action="store_true"
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="run in debug mode",
        action="store_true",
    )
    parser.add_argument(
        "-e",
        "--extensions",
        help='Extensions (example ".php,.exe,.bak")',
        metavar="<extensions>",
    )

    args = parser.parse_args()
    log = set_loglevel(debug_mode=args.debug)
    extensions = args.extensions.split(",") if args.extensions else None

    print(f"[[green]+[/]] Target: {args.url}")
    print(f"-" * 41)

    try:
        # Start asynchronous loop
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            dir_bruter(wordlist=args.wordlist, extensions=extensions)
        )
    except KeyboardInterrupt:
        log.warning("User interruption detected ([yellow]Ctrl+C[/])")
    except Exception as e:
        log.error(f"An error occurred: [red]{e}[/]")
