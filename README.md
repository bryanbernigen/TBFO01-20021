# Python Compiler using CYK Algorithm
> Check whether a python file is syntactically correct or not.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)


## General Information
- main.py is an external python compiler to check whether a python file is syntactically correct or not.
- There are 2 core in our project : python parser using DFA (deterministic finite automata) and python compiler
- python parser will parse a python file into a string that will be tested in our compiler.
- The core of our compiler is converting python languange to CFG (Context Free Grammar)
- then we convert CFG to CNF (Chomsky Normal Form).
- then we use CYK (Cocke–Younger–Kasami) algorithm to our parsed python filer to test whether that string belongs to our language (our CNF). 


## Technologies Used
- Python 3.9.2


## Features
List the ready features here:
- parse a python file
- test whether a python file is syntactically correct or not.


## Setup
1. install python : https://www.python.org/downloads/
2. open your directory in terminal/cmd and clone this repository by:
    ```
    git clone https://github.com/bryanbernigen/TBFO01-20021
    ```
    or copy the main.py, tokenreader.py, and variable_dfa.py to your directory

## Usage
1. put the file that are going to be tested in the same directory
2. open the directory in teminal/cmd and run main.py by:
    ```
    python main.py
    ```
    if you use automatic code runner (press a button to run a file), then please pay attention to the path 
3. enter the name of the python file that are going to be tested e.g test.py
4. Enjoy


## Project Status
Project is: no longer being worked on


## Room for Improvement
Room for improvement:

- Differentiate indentation, e.g

  Case 1: Syntax Error

    ```x x```
    
  Case 2: Not a Syntax Error
  
  ```
  x
  x
  ```
      
  Our compiler couldn't differentiate case 1 and 2 so case 1 and 2 will be accepted in our compiler
  
- Add other python languanges that havent been implemented, e.g

  finally, lambda, try, nonlocal, etc.
  
  our compiler only cover python laguages that are listed in "docs/Spek Tugas Pemrograman TBFO.pdf"
