## (non) Linear Programming Problem Solver using Monte Carlo Method

The purpose of this project was to develop a program to solve problems defined by a finite set of constraint functions over finite set of real, non-negative variables using Monte Carlo method.
The program uses Python Lex-Yacc for parsing mathematical expressions and multiprocessing to speed up evaluating whether or not generated points satisfy constraint functions.
Most of the time it provides moderately good answers in acceptable time, though usage of multiprocessing in this one is pretty clunky.

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
