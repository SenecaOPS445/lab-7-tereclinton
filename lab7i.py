#!/usr/bin/env python3
# Student ID: 119911220

def function1():
    global schoolName  # Declare that we use the global variable
    schoolName = 'SICT'  # Change the global variable
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # Declare that we use the global variable
    schoolName = 'SSDO'  # Change the global variable
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)  # Will print 'SICT'
function2()
print('print() in main on schoolName:', schoolName)  # Will print 'SSDO'

