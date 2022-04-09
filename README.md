# DIRBRUTER

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=for-the-badge&logo=linux)
![GitHub](https://img.shields.io/github/license/vijaysahuofficial/DirBruter?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/vijaysahuofficial/DirBruter?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/vijaysahuofficial/DirBruter?style=for-the-badge)](https://github.com/vijaysahuofficial/DirBruter/network)
![Lines of code](https://img.shields.io/tokei/lines/github/vijaysahuofficial/DirBruter?style=for-the-badge)
[![GitHub stars](https://img.shields.io/github/stars/vijaysahuofficial/DirBruter?style=for-the-badge)](https://github.com/vijaysahuofficial/DirBruter/stargazers)

*DirBruter is a Python based CLI tool. It looks for hidden or existing directories/files using brute force method. It basically works by launching a dictionary based attack against a webserver and analyse its response.*

# INSTALLATION

```
git clone https://github.com/vijaysahuofficial/DirBruter.git
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
