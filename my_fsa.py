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
            self.add_state(i)
        
    def add_state(self, state):
        self.states.append(state)
            
    def add_transition(self, start, inp, end, out):
        #(init, input): final)
        if start not in self.states or end not in self.states:
            print("Invalid start or end state")
        else: 
            self.transitions[(start,inp)] = (end, out)
    
    def check_automaton(self):
        if self.initial_state is None:
            print("Please provide an initial state")
            return False
        elif self.final_states == []:
            print("Please provide one or more final states")
            return False
        elif self.transitions == {}:
            print("Please provide one or more transitions")
            return False
        else:
            return True
    
    
    def run_fsa(self, inp = None):
        
        if self.check_automaton() == False:
            return -1
        if inp is None:
            print("Please provide a input string")
            return -1
        
        print("Running automaton",self.name,"on input: ", inp)
        self.current_state = self.initial_state
        self.out=[]
        i = 0
        L = len(inp)
        #print(self.out)
        while i<L:
            cmd = inp[i]
            try:
                current_tr = self.transitions[(self.current_state, cmd)]
                i += 1
            except KeyError:
                #print("No transition is defined for state and input tuple: ", e)
                break
            #print(self.transitions[(self.current_state, cmd)])
            self.current_state = current_tr[0]
            self.out.append(current_tr[1])
            #print(self.out)
            
        print("the final state is: ",self.current_state)
        print("output: ", "".join(self.out))
        if (self.current_state in self.final_states) and (i == L):
            print("The automaton accepts this string")
            return 0
        else:
            print("The automaton does not accept this string")
            return -1


def fsa_from_txt(file, name=""):
    automaton = Fsa(name)
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
            automaton.add_transition(tr[0],tr[1],tr[2],tr[3])
        return automaton

