# DIRBRUTER

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=for-the-badge&logo=linux)
![OS](https://img.shields.io/badge/OS-Windows-blue?style=for-the-badge&logo=windows)
![GitHub](https://img.shields.io/github/license/rly0nheart/DirBruter?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/rly0nheart/DirBruter?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/rly0nheart/DirBruter?style=for-the-badge)](https://github.com/rly0nheart/DirBruter/network)
[![GitHub stars](https://img.shields.io/github/stars/rly0nheart/DirBruter?style=for-the-badge)](https://github.com/rly0nheart/DirBruter/stargazers)

*DirBruter is a Python based CLI tool. It looks for hidden or existing directories/files using brute force method. It basically works by launching a dictionary based attack against a webserver and analyse its response.*

# INSTALLATION

```
git clone https://github.com/rly0nheart/DirBruter.git
```

```
cd DirBruter
```

```
pip install -r requirements.txt
```

```
sudo chmod +x dirBruter
```


# USAGE

**Linux**
```
dirBruter -u "http://testphp.vulnweb.com" -w DBwordlist.txt
```

**Windows**

```
python dirBruter -u "http://testphp.vulnweb.com" -w "DBwordlist.txt"
```

*or*
```
python3 dirBruter -u "http://testphp.vulnweb.com" -w "DBwordlist.txt"
```

# OPTIONAL ARGUMENTS
| Option       | Metavar | Description |
| ------------- |:---------:|:---------:|
| ``-t/--threads`` | threads |  *number of threads (default is 1)* |
| ``-w/--wordlist`` | wordlist |  *wordlist/path to wordlist file* |
| ``-o/--output`` | filename |  *write found results to a file* |
| ``-e/--extensions`` | extensions | *extensions (e.g ".php,.html,.exe")* |
| ``-v/--verbose`` |  |  *enable verbosity* |

# DISCLAIMER

*This Tool is made for educational purpose, and should not be used in environments without legal authorization. The author will not be responsible for any misuse of this toolkit.*


# HELP
```
dirBruter -h
```

# WORDLISTS
 
* [Dirb wordlist](https://github.com/v0re/dirb/tree/master/wordlists)
* [Dirbuster](https://github.com/daviddias/node-dirbuster/tree/master/lists)


# EXTENSIONS WORDLIST
*If you are using default DBwordlist.txt then don't add any other extenstions.*

*Get the extensions wordlist from* [SecLists](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt)
