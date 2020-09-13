#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program checks if someone is eligible to date my grandchild


import random


def main():
    # This function checks if someone is eligible to date my grandchild

    # Input
    print("So, you want to date my grandchild,")
    print("")
    wealth = int(input("What is your net worth? $"))
    print("")
    appearance = int(input("On a scale from 1 - 10, how attractive are you? "))
    print("")

    # Process & Output
    if wealth >= 2250000 or appearance >= 7:
        print("Great! You are free to date my grandchild!")
    else:
        print("I am so sorry, but I can’t allow you to date my grandchild!")


if __name__ == "__main__":
    main()
