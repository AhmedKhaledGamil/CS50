# CS50
Problem sets for CS50 course by Harvard University on edX

[Link to CS50](https://courses.edx.org/courses/course-v1:HarvardX+CS50+X/course/](https://courses.edx.org/courses/course-v1:HarvardX+CS50+X/course/ "CS50")

**pset1: code in C**

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

**pset2: code in C**

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

**pset3: code in C**

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
