#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Paige Adams with help from Tiffany Mclean"

import sys

def get_file(filename):
    with open(filename, 'r') as f:
        text = f.readlines()
    return text



def is_nested(line):
    """Validate a single input line for correct nesting"""
    brackets = {')': '(', '}': '{', ']': '[', '>': '<', '*)': '(*'}

    stack = []
    i = 0

    closing_brackets = brackets.keys()
    opening_brackets = brackets.values()
    new_list = list(line)
    skip = False
    for index, is_bracket in enumerate(new_list):
        if skip:
            skip = False
            continue
        else:
            if index != len(new_list) - 1:
                if is_bracket in opening_brackets:
                    stack.append(is_bracket)
                    i += 1
                elif is_bracket in closing_brackets:
                    i += 1
                    if stack[-1] == brackets[is_bracket]:
                        stack.pop()
                    else:
                        return "NO " + str(i)
                else:
                    i += 1
    if len(stack) == 0:
        return "YES"
    else:
        i += 1
        return "NO " + str(i)



def main(args):
    """Open the input file and call `is_nested()` for each line"""
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as wf:
            for line in f:
                get_output = is_nested(line)
                print(get_output)
                wf.write(str(get_output + '\n'))
    


if __name__ == '__main__':
    main(sys.argv[1:])
