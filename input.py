import sys

def get_input():
    return sys.stdin.readline().rstrip("\n")

def get_all_input():
    return sys.stdin.read().split("\n")

def get_input_int():
    return [int(n) for n in sys.stdin.readline().rstrip("\n").split()]

def get_input_float():
    return [float(n) for n in sys.stdin.readline().rstrip("\n").split()]

