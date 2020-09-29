# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:17:10 2020

@author: kikka
"""
class Fsa:
    def __init__(self,name=""):
        self.states = []
        self.transitions = {}
        self.current_state = None
        self.initial_state = None
        self.final_states = []
        self.out = []
        self.name = name
        
    def define_start(self, start_state):
        if start_state not in self.states:
            print(start_state, "is not part of the automaton allowed states, so it can't be used as initial state")
        else:
            self.initial_state = start_state
            
    def define_end(self, end_states):
        for i in end_states:
            if i not in self.states:
                print(i, "is not part of the automaton allowed states, so it can't be used as final state")
            else:
                self.final_states.append(i)
            
    def add_states(self, states):
        for i in states:
            self.states.append(i)
            
    def add_transition(self, start, inp, end, out):
        #(init, input): final)
        if start not in self.states or end not in self.states:
            print("Invalid start or end state")
        else: 
            self.transitions[(start,inp)] = (end, out)
    
    def run_fsa(self, inp = None):
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
        
        print("Running automaton",self.name,"on input: ", inp)
        self.current_state = self.initial_state
        self.out=[]
        #print(self.out)
        for cmd in inp:
            try:
                current_tr = self.transitions[(self.current_state, cmd)]
            except KeyError as e:
                print("No transition is defined for state and input tuple: ", e)
                return -1
            #print(self.transitions[(self.current_state, cmd)])
            self.current_state = current_tr[0]
            self.out.append(current_tr[1])
            #print(self.out)
        print("the final state is: ",self.current_state)
        if self.current_state in self.final_states:
            print("The automaton accepts this string")
            print("output: ", "".join(self.out))
            return 0
        else:
            print("The automaton does not accept this string")
            print("output: ", "".join(self.out))
            return -1


