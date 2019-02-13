## (non) Linear Programming Problem Solver using Monte Carlo Method

The purpose of this project was to develop a program to solve problems defined by a goal function and a finite set of constraint functions over finite set of real, non-negative variables using Monte Carlo method.

Constraints are input as text, and can range from expressions with simple linear functions
```
1.5x + 5 < 20
```
to more complex ones such as
```
y / (z) < sin(x * y^(-1/5)) < z^(pi * e)
```

The program uses grammar and lexing rules written with Python Lex-Yacc for parsing mathematical expressions and concurrency via multiprocessing to speed up evaluating whether or not generated points satisfy constraint functions.
For most textbook problems it provides good answers in acceptable time. 

### Prerequisites

For this program to work, you need to have PLY (Python 
Lex-Yacc) installed on your system or virtual environment. You can get it with pip:
```
pip install ply
```

Or, if you're an Arch Linux user, you can get it from extra 
repository with pacman:
```
sudo pacman -S python-ply
```
