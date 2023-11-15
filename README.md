# DIRBRUTER
*DirBruter is a Python based CLI tool. It looks for hidden or existing directories/files using brute force method. It basically works by launching a dictionary based attack against a webserver and analyse its response.*

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![OS](https://img.shields.io/badge/OS-Windows-blue?style=flat&logo=windows)
![GitHub](https://img.shields.io/github/license/rly0nheart/DirBruter?style=flat&logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/rly0nheart/DirBruter?style=flat&logo=github)
[![GitHub forks](https://img.shields.io/github/forks/rly0nheart/DirBruter?style=flat&logo=github)](https://github.com/rly0nheart/DirBruter/network)
[![GitHub stars](https://img.shields.io/github/stars/rly0nheart/DirBruter?style=flat&logo=github)](https://github.com/rly0nheart/DirBruter/stargazers)

![Screenshot from 2023-10-21 02-51-13](https://github.com/rly0nheart/DirBruter/assets/74001397/36d403f8-0de4-4238-b682-b4d434696394)
***

# Installation

```
git clone https://github.com/rly0nheart/DirBruter
```

```
cd DirBruter
```

```
pip install -r requirements.txt
```


# Usage
```
python dirbruter.py --help
```
```
 ____  _        ____             _            
|  _ \(_)_ __  | __ ) _ __ _   _| |_ ___ _ __ 
| | | | | '__| |  _ \| '__| | | | __/ _ \ '__|
| |_| | | |    | |_) | |  | |_| | ||  __/ |   
|____/|_|_|    |____/|_|   \__,_|\__\___|_|   
                                              

usage: dirBruter.py [-h] -w <wordlist> [-o] [-d] [-e <extensions>] url

DirBruter — https://github.com/rly0nheart

positional arguments:
  url                   Target URL

options:
  -h, --help            show this help message and exit
  -w <wordlist>, --wordlist <wordlist>
                        Path to wordlist
  -o, --output          Save found results to a file
  -d, --debug           run in debug mode
  -e <extensions>, --extensions <extensions>
                        Extensions (example ".php,.exe,.bak")

DirBruter is a Python-based CLI tool that looks for hidden or existing directories/files using the brute force method. It basically works by launching a dictionary-based attack against a
webserver and analyzing its response

```

# Disclaimer

*This Tool is made for educational purpose, and should not be used in environments without legal authorization. The author will not be responsible for any misuse of this toolkit.*


# Wordlists
 
* [Dirb wordlist](https://github.com/v0re/dirb/tree/master/wordlists)
* [Dirbuster](https://github.com/daviddias/node-dirbuster/tree/master/lists)


# Extensions Wordlist
*If you are using default DBwordlist.txt then don't add any other extenstions.*

*Get the extensions wordlist from* [SecLists](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt)
