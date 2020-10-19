# Indonesian Kata Baku Checker
An example is worth a thousand words.

Assume that I have a text file named `teks.txt`
```
Nama saya Ucup. Saya adalah seorang atlit tauladan.
Saya juga adalah seorang cendikiawan yang memiliki kreatifitas tinggi.
```
If I run the program with `bakuCheck teks.txt`, It will give the following output:
```
######################################################################
# Indonesian Kata Baku Checker                                       #
# Author   : Turfa Auliarachman                                      #
# Date     : October 23, 2016                                        #
######################################################################

Checker       : Kata Baku Checker
Line          : 1
Original text : ...Saya adalah seorang atlit tauladan.
Message       : The correct word for 'atlit' is 'atlet'

Checker       : Kata Baku Checker
Line          : 1
Original text : ...dalah seorang atlit tauladan.
Message       : The correct word for 'tauladan' is 'teladan'

Checker       : Kata Baku Checker
Line          : 2
Original text : ...juga adalah seorang cendikiawan yang memiliki kr...
Message       : The correct word for 'cendikia' is 'cendekia'

Checker       : Kata Baku Checker
Line          : 2
Original text : ...iawan yang memiliki kreatifitas tinggi.
Message       : The correct word for 'kreatifitas' is 'kreativitas'
```


## Requirement
- Python 3.x


## Usage
In this usage instruction, I assume that you use Linux Operating System. For other OS users, you can adapt this instruction for your own OS.


### With Symbolic Link (Recommended)
It is recommended that you create a symbolic link from the script to `/usr/bin/bakuCheck`, so you can run this script from any folder. To create a symbolic link, simply use this following command:
```
sudo ln -s <path-to-script>/bakuCheck.py /usr/bin/bakuCheck
```
Now, in the same folder with the text file that you want to check, just use this command:
```
bakuCheck <filename>
```


### Without Symbolic Link
If you don't have a root access, you can use this command:
```
./bakuCheck.py <path-to-file>/<filename>
```


## Improvement Suggestion
- Add other common mistakes to the dictionary list `dict.txt`. See the format below.
- Create more checkers.


## Dictionary List
The default dictionary list file is `dict.txt` placed in the root folder of the script. To change the dictionary list file, simply change the `dictFile` constant in the `bakuCheck.py`. The format of this file follow the format below:
```
<correct word 1>|<wrong word 1>
<correct word 2>|<wrong word 2>
<correct word 3>|<wrong word 3>
<correct word 4>|<wrong word 4>
...
<correct word n>|<wrong word n>
```

Although the program automatically detect duplicate entries and treat it as one, it is indeed not a good thing to keep duplicate entries in the dictionary list file. So, I made a simple script `improveDict.py` to delete duplicate entries (leave one of them). Usage :
```
./improveDict.py <src> <dst>
```
where `src` is the current dictionary list file and `dst` is the "improved" dictionary list file.

P.S : even I don't know why I named it "improve" :D

## Use as Package

You can easly use as package from your any python program look at example below

```python
from IndonesianKataBakuChecker import WordReader

reader = WordReader()
text = "saya sangat handal dalam bermain bola"

for res in reader.get_result(text):
    print(res)
```

The result will look like this

```
{   
    'checker': 'Kata Baku Checker', 
    'line': 1, 
    'original_text': 'saya sangat handal bermain bola', 
    'message': "The correct word for 'handal' is 'andal'"
}
```

## License
```
Copyright © 2016 Turfa Auliarachman <turfa_auliarachman@rocketmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the LICENSE file for more details.
```
