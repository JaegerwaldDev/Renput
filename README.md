<p align="center">
<img src="https://github.com/JaegerwaldDev/Renput/blob/main/Renput_ReadMe.png" height="96px"/>
</p>
<h1 align="center">Renput</h1>
<h2 align="center">A simple Python library for Windows, which replaces the default input function in order to add the functionality to automatically complete an input using the tab key.</h2>
<p align="center">
<a href="https://github.com/JaegerwaldDev/Renput/blob/master/LICENSE">
    <img alt="GitHub license" src="https://img.shields.io/github/license/JaegerwaldDev/Renput">
</a>
<a href="https://github.com/JaegerwaldDev/Renput/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/JaegerwaldDev/Renput">
</a>
<a href="https://github.com/JaegerwaldDev/Renput">
    <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/JaegerwaldDev/Renput/total">
</a>
<a href="https://github.com/JaegerwaldDev/Renput">
    <img alt="GitHub all releases" src="https://img.shields.io/github/watchers/JaegerwaldDev/Renput">
</a>
</p>

# Features

## `input(prompt, auto_complete)`

- `prompt`: The prompt given to the user before the input line.
- `auto_complete`: A list of auto completions that get input when the `tab ↹` key is pressed

# Example of use
```py
from renput import *

auto_complete = [
    "apple",
    "banana",
    "cherry",
    "pineapple"
]

print("Enter the first few letters of apple, banana, cherry or pinapple,\nthen press tab to see the functionality of Renput:")
while True:
    input(auto_complete=auto_complete)
```

Please report any issues that you find when using the library, but only if you are on the newest version.
Optionally, you can report new issues on [my discord server](https://discord.gg/MRb8jQf9fU).
