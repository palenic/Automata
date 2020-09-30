# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:09:02 2020

@author: kikka
"""


import my_pda as pda
x=pda.pda_from_txt("data/parentheses_compl.txt","bad parentheses")
inp="((()()()()"
x.run_pda(inp)
print()
y=pda.pda_from_txt("data/parentheses.txt", "good parentheses")
y.run_pda(inp)

x.run_pda("(()())")
y.run_pda("(()())")