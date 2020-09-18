# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:35:07 2017

@author: sacjain
"""

from vsearch import search4vowels
from vsearch import search4letters

word='sachin'
vowels=search4vowels(word)
print(vowels)
letters=search4letters(word,'sch')
print(letters)