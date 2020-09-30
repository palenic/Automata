# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:50:11 2020

@author: kikka
Tests for FSA
"""


import unittest
import my_fsa as fsa

class TestBWT(unittest.TestCase):

    def test_fsa_switch(self):
        x = fsa.fsa_from_txt("data/switch.txt")
        a=x.run_fsa("RSSRS")
        self.assertEqual(a,-1)
        a=x.run_fsa("RSRRR")
        self.assertEqual(a, 0)
    
    def test_binary_transducer(self):
        x = fsa.fsa_from_txt("data/binary_transducer.txt")
        a=x.run_fsa("110000")
        self.assertEqual(a,0)
        self.assertEqual("".join(x.out), "111100")
        a=x.run_fsa("01100")
        self.assertEqual(a,-1)
        self.assertEqual("".join(x.out), "11110")
        
        
if __name__ == '__main__':
    unittest.main()