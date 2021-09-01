# DirBruter
<p>DirBruter is a Python based CLI tool. It looks for hidden or existing directories/files using brute force method. It basically works by launching a dictionary based attack against a webserver and analyse its response.</p>

# Installation

<code>git clone https://github.com/vijaysahuofficial/DirBruter.git</code>

<code>cd DirBruter</code>

<code>pip install -r requirements.txt</code>

<code>sudo chmod +x dirBruter</code>


# Usage

<h2>Linux</h2>
<code>dirBruter -u "http://testphp.vulnweb.com" -w "wordlist"</code>
<h2>Windows</h2>
<code>python dirBruter -u "http://testphp.vulnweb.com" -w "wordlist"</code>

<p>or</p>
<code>python3 dirBruter -u "http://testphp.vulnweb.com" -w "wordlist"</code>


# Help
<code>dirBruter -h</code>

# Wordlists

<ul>
    <li><a href="https://github.com/v0re/dirb/tree/master/wordlists" target="_blank">Dirb Wordlist</a></li>
    <li><a href="https://github.com/daviddias/node-dirbuster/tree/master/lists" target="_blank">Dirbuster Wordlist</a></li>
</ul>

