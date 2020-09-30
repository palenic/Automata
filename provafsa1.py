# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:37:39 2020

@author: kikka
"""
#%%
import my_fsa as fsa

x = fsa.Fsa("light switch")
states = ["on","off"]
x.add_states(states)
x.define_start("off")
x.define_end(["off"])
x.add_transition("on", "S", "on", "")
x.add_transition("on", "R", "off", "")
x.add_transition("off", "S", "on", "")
x.add_transition("off", "R", "off", "")
inp = "SSR"

x.run_fsa(inp)
#%%

import my_fsa as fsa

y = fsa.Fsa("special binary")
states = ["q1", "q0"]
y.add_states(states)
y.define_start("q0")
y.define_end(["q0"])
y.add_transition("q0", "1", "q0", "11")
y.add_transition("q0", "0", "q1", "")
y.add_transition("q1", "1", "q1", "11")
y.add_transition("q1", "0", "q0", "0")
inp = "011000"
y.run_fsa(inp)
y.run_fsa("10000")