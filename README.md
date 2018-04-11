# bitwise
A set of basic bitwise calculators
Written in Python 3

Includes
--------
 - and.py
 - or.py
 - xor.py
 - helpers.py (common code shared by the other functions)
 
Imported Python modules
-----------------------
  - sys

Usage
-----
 - and.py value1 value2
 - or.py value1 value2
 - xor.py value1 value2
 
Values can be in the following formats
--------------------------------------
 - Hex - 0x34
 - Hex - 34h
 - Decimal - 52
There is no error checking, so entering anything not in these formats will probably not end well.

Examples -
-----------------
and.py 5445 4554h
-----------------

                 0b1010101000101
               0b100010101010100
AND-----------------------------
                   0b10101000100

Decimal - 1348  |        Hex - 0x544    |        Binary - 0b10101000100         |        ASCII - out of range


----------------
or.py 5445 4554h
----------------

                 0b1010101000101
               0b100010101010100
OR------------------------------
               0b101010101010101

Decimal - 21845         |        Hex - 0x5555   |        Binary - 0b101010101010101     |        ASCII - out of range


-----------------
xor.py 5445 4554h
-----------------

                 0b1010101000101
               0b100010101010100
XOR-----------------------------
               0b101000000010001

Decimal - 20497         |        Hex - 0x5011   |        Binary - 0b101000000010001     |        ASCII - out of range
