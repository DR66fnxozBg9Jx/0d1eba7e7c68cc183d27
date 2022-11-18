#!/usr/bin/python3.9


'''generate a random, fairly secure 32-character ASCII-extended password'''
import random as r
from time import time_ns as t

LETTERS = [chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
NUMS = [str(i) for i in range(10)]

r.seed(t())
chars = [chr(i) for i in range(33, 256) if chr(i).isprintable()]
r.shuffle(chars)

def generate_pwd():
	return ''.join(r.choices(chars, k=30))+r.choice(NUMS)+r.choice(LETTERS)

pwd = list(generate_pwd())
r.shuffle(pwd)
print(''.join(pwd))
