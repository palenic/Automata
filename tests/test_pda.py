# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:02:08 2020

@author: kikka
Tests for PDA
"""


import unittest
import my_pda as pda

class TestBWT(unittest.TestCase):

    def test_pda_anbn(self):
        x = pda.pda_from_txt("data/anbn.txt")
        inp="aaaabbbb"
        a=x.run_pda(inp)
        self.assertEqual(a,0)
        inp="aaabbbb"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="aaaabbb"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="a"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="abba"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="bba"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
    
    def test_pda_anbn2(self):
        x = pda.pda_from_txt("data/anbn_v2.txt")
        inp="aaaabbbb"
        a=x.run_pda(inp)
        self.assertEqual(a,0)
        self.assertEqual("".join(x.out),"AAAABBBB")
        inp="aaabbbb"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        self.assertEqual("".join(x.out),"AAABBB")
        inp="aaaabbb"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="a"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="abba"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="bba"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
    
    def test_pda_parentheses(self):
        x = pda.pda_from_txt("data/parentheses.txt")
        inp="(())"
        a=x.run_pda(inp)
        self.assertEqual(a,0)
        inp="(()())"
        a=x.run_pda(inp)
        self.assertEqual(a,0)
        inp="(()"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="()))"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="))"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="()()"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        
    def test_pda_parentheses_compl(self):
        print("complement")
        x = pda.pda_from_txt("data/parentheses_compl.txt")
        inp="(())"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="(()())"
        a=x.run_pda(inp)
        self.assertEqual(a,-1)
        inp="()()))"
        a=x.run_pda(inp)
        self.assertEqual(a,0)
        inp="())"
        a=x.run_pda(inp)
        self.assertEqual(a,0)
        inp="(("
        a=x.run_pda(inp)
        self.assertEqual(a,0)
        
if __name__ == '__main__':
    unittest.main()