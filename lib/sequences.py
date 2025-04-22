#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    sequence = [0,1]

    while len(sequence) < length:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    print(sequence[:length])       
    