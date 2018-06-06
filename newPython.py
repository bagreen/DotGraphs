#!/usr/bin/python
import os

def main(): 
    for file in os.listdir(os.getcwd()):
        #call("awk '{$1=""; sub(" ", " "); print}'" + file + "/.bash_history" + " > " + file + "/3.dot")
        call("awk '{$1=""; sub(" ", " "); print}' ben/.bash_history > ben/3.dot")
        call("dot -Tpdf " + '../' + file + '3.dot' + ' > ' + '../' + file + '3.pdf', shell=True)
        
        
        # if '' in files:
        #     input = open(file + '/.bash_history', 'r')
        #     output = open('../' + file + '3.dot', 'w')
            
            
            #options = ['-f', '-o']
            #commands = ['find', 'man']
            #lines = input.readlines()
            #listCommands = []
            
            # for l in lines:
            #     words = l.split()
            # 
            #     #remaining commands
            #     for c in words:
            #         if c in commands:
            #             listCommands.append(c)
            #             break
            #print('--------------')
            
            #looking for find - better way to do this?
            #if "find" in l:
            #    listCommands.append("find")
            
            
            # 
            # 
            # 
            # input.close()
            # output.close()
            # 
