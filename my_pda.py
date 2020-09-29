# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:50:17 2020

@author: kikka
"""

import my_fsa as fsa
class Pda(fsa.Fsa):
    def __init__(self, name=""):
        super().__init__(name)
        self.pile = ["Z0"]
        
    def add_transition(self, start, inp, current_cell, end, pile_action, out):
        #(init, input): final)
        if start not in self.states or end not in self.states:
            print("Invalid start or end state")
        else: 
            self.transitions[(start, inp, current_cell)] = (end, pile_action, out)
    
    def run_fsa(self, inp = ""):
        pass
    
    def run_pda(self, inp = None):
        if self.initial_state is None:
            print("Please provide an initial state")
            return -1
        if self.final_states == []:
            print("Please provide one or more final states")
            return -1
        if self.transitions == {}:
            print("Please provide one or more transitions")
            return -1
        if inp is None:
            print("Please provide a input string")
            return -1
        self.pile=["Z0"]
        print("Running automaton",self.name,"on input: ", inp)
        self.current_state = self.initial_state
        accepted = True
        i = 0
        L = len(inp)
        #print(self.transitions[("q0","(","Z0")])
        while i<L:
            try:
                cmd = inp[i]
                #print(self.current_state, cmd, self.pile[-1])
                current_tr = self.transitions[(self.current_state, cmd, self.pile[-1])]
                #print(self.current_state, cmd, self.pile[-1],current_tr)
                i += 1
                #print(i,cmd)
            except KeyError:
                try:
                    #if there is no transition defined for output and pile, try epsilon move
                    current_tr = self.transitions[(self.current_state, "eps", self.pile[-1])]
                    #print(self.current_state, "eps", self.pile[-1],current_tr)
                except KeyError:
                    #if there is no transition and no epsilon move, we cannot move from this
                    #state but the string is not finished. So it must be unacceptable
                    #print(e)
                    #print("string not finished")
                    #accepted = False
                    break
            self.current_state = current_tr[0]
            if current_tr[1] == "del":
                del self.pile[-1]
            elif current_tr[1] == "":
                pass
            else:
                self.pile.append(current_tr[1])
            self.out.append(current_tr[2]) 
        # try epsilon moves once the string is over
        #print("input over, switching to eps")
        while True:
            #print(self.pile)
            try:
                eps_move = self.transitions[(self.current_state, "eps", self.pile[-1])]
                #print(self.current_state, "eps", self.pile[-1],eps_move)
                self.current_state = eps_move[0]
                if eps_move[1] == "del":
                    del self.pile[-1]
                elif eps_move[1] == "":
                    pass
                else:
                    self.pile.append(current_tr[1])
                    self.out.append(current_tr[2]) 
            except KeyError:
                #print("no more eps")
                break
        print("the final state is: ",self.current_state)
        #print(i)
        print("output: ", "".join(self.out))
        if (self.current_state in self.final_states) and accepted == True and i == len(inp):
            print("The automaton accepts this string")
            return 0
        else:
            print("The automaton does not accept this string")
            return -1

def pda_from_txt(file, name=""):
    automaton = Pda(name)
    with open(file) as f:
        states = f.readline().strip()
        states = states.split(",")
        #print(states)
        automaton.add_states(states)
        start = f.readline().strip()
        automaton.define_start(start)
        end = f.readline().strip().split(",")
        automaton.define_end(end)
        for line in f.readlines():
            tr = line.strip().split(",")
            automaton.add_transition(tr[0],tr[1],tr[2],tr[3],tr[4],tr[5])
        return automaton