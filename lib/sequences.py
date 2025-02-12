#!/usr/bin/env python3

def print_fibonacci(length):
    '''Prints the Fibonacci sequence up to the given length.'''
    sequence = []
    a, b = 0, 1
    while len(sequence) < length:
        sequence.append(a)
        a, b = b, a + b
    print(sequence)