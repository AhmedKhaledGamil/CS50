# CS50
Problem sets for CS50 course by Harvard University on edX

[Link to CS50](https://courses.edx.org/courses/course-v1:HarvardX+CS50+X/course/](https://courses.edx.org/courses/course-v1:HarvardX+CS50+X/course/ "CS50")

**pset1**

hello.c : a program that prints out a simple greeting to the user, per the below. <br/>
[Detailed Description](https://docs.cs50.net/2018/x/psets/1/hello/hello.html)
```
$ ./hello  
hello, world
```

mario.c : a program that prints out a double half-pyramid of a specified height, per the below. <br/>
[Detailed Description](https://docs.cs50.net/2018/x/psets/1/mario/more/mario.html)
```
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

credit.c : a program that determines whether a provided credit card number is valid according to Luhn’s algorithm.  
[Detailed Description](https://docs.cs50.net/2018/x/psets/1/credit/credit.html)
```
$ ./credit
Number: 378282246310005
AMEX
$ ./credit
Number: 6176292929
INVALID
```

**pset2**

vigenere.c: a program that encrypts messages using Vigenère’s cipher, per the below.  
[Detailed Description](https://docs.cs50.net/2018/x/psets/2/vigenere/vigenere.html)
```
$ ./vigenere 13
Usage: ./vigenere k
$ ./vigenere bacon
plaintext: Meet me at the park at eleven am
ciphertext: Negh zf av huf pcfx bt gzrwep oz
```

crack.c: a program that cracks passwords, per the below.  
[Detailed Description](https://docs.cs50.net/2018/x/psets/2/crack/crack.html)
```
$ ./crack 50fkUxYHbnXGw
rofl
```

**pset3**

find.c: a program that finds a number among numbers, per the below.   
[Detailed Description](https://docs.cs50.net/problems/find/more/find.html)
```
$ ./generate 1000 | ./find 42
Didn't find needle in haystack.
$ ./find 42
50
43
^d
Didn't find needle in haystack.

$ ./find 42
50
42
^d
Found needle in haystack!
```

fifteen.c: the Game of Fifteen, per the below.  
[Detailed Description](https://docs.cs50.net/problems/fifteen/fifteen.html)
```
$ ./fifteen 3
WELCOME TO GAME OF FIFTEEN

8  7  6

5  4  3

2  1  _

Tile to move:
```

**pset4**

whodunit.c: a program that reveals a hidden message in a BMP, per the below.     
[Detailed Description](https://docs.cs50.net/2018/x/psets/4/whodunit/whodunit.html)
```
$ ./whodunit clue.bmp verdict.bmp
```

resize.c: a program that resizes BMPs, per the below.       
[Detailed Description](https://docs.cs50.net/2018/x/psets/4/resize/more/resize.html)
```
$ ./resize .25 large.bmp small.bmp
$ ./resize 4 small.bmp large.bmp
```

recover.c: a program that recovers JPEGs from a forensic image, per the below.         
[Detailed Description](https://docs.cs50.net/2018/x/psets/4/recover/recover.html)
```
$ ./recover card.raw
```

**pset5**

speller.c : a program that spell-checks a file, per the below.  
[Detailed Description](https://docs.cs50.net/2018/x/psets/5/speller/speller.html)  
```
$ ./speller texts/lalaland.txt

MISSPELLED WORDS

Chazelle
L
TECHNO
L
.
.
.
.
Mia
Mia
Sebastian's
L

WORDS MISSPELLED:     955
WORDS IN DICTIONARY:  143091
WORDS IN TEXT:        17756
TIME IN load:         0.27
TIME IN check:        0.06
TIME IN size:         0.00
TIME IN unload:       0.12
TIME IN TOTAL:        0.44
```
**pset6**
[Detailed Description](https://docs.cs50.net/2018/x/psets/6/sentimental/sentimental)
hello.py : a program that prints out a simple greeting to the user, per the below.   
```
$ python hello.py  
hello, world
```

mario.py : a program that prints out a double half-pyramid of a specified height, per the below.  
```
$ python mario.py
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```

credit.py : a program that determines whether a provided credit card number is valid according to Luhn’s algorithm.  
```
$ python credit.py
Number: 378282246310005
AMEX
$ python credit.py
Number: 6176292929
INVALID
```

vigenere.py : a program that encrypts messages using Vigenère’s cipher, per the below.  
```
$ python vigenere.py 13
Usage: ./vigenere k
$ python vigenere.py bacon
plaintext: Meet me at the park at eleven am
ciphertext: Negh zf av huf pcfx bt gzrwep oz
```

crack.py : a program that cracks passwords, per the below.  
```
$ python crack.py 50fkUxYHbnXGw
rofl
```

similarties.py : a program that measures the edit distance between two strings.  
a web app that depicts the costs of transforming one string into another, a la the below.  
[Detailed Description](https://docs.cs50.net/2018/x/psets/6/similarities/more/similarities.html)
![alt text](https://github.com/AhmedKhaledGamil/CS50/blob/master/pset6/similarities/image.png)  

```
Usage: Using the Command Line  
./score FILE1 FILE2  
Usage: Via a web app
flask run
```

**pset7**

finance: a website via which users can "buy" and "sell" stocks, a la the below.  
[Detailed Description](https://docs.cs50.net/2018/x/psets/7/finance/finance.html)  
![alt text](https://github.com/AhmedKhaledGamil/CS50/blob/master/pset7/image.png)  
```
flask run
```

**pset8**

mashup: a website that lets users search for articles atop a map, a la the below.   
[Detailed Description](https://docs.cs50.net/2018/x/psets/8/mashup/mashup.html)  
![alt text](https://github.com/AhmedKhaledGamil/CS50/blob/master/pset8/image.png)  
```
flask run
```


