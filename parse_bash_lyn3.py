#!/usr/bin/python
import os
import re
from subprocess import call



''' draw a graph for each file/student
  for each student, create a list of cmds
  for each cmd, create a dictionary of options
'''

from cmd import *

options = ['-f', '-e', '-c', '-o']

commands = ['strace', 'man', 'which', 'cat'] #deleted 'ls'

#dir = '.'
#in_filename = 'richard'
#out_filename = 'cmds_richard'

def main():
    ## read input file  ##
    #filename = input("enter filename ");
    #os.mkdir('graphs')
    for filename in os.listdir(os.getcwd()):
    	if '' in filename: # was Jens
    		print filename
    		infile = open(filename + '/.bash_history', 'r')
    		outfile = open('../' + filename + '3.dot', 'w')
    		process_files(infile, outfile)
    		infile.close()
    		outfile.close()
    		
    		call("dot -Tpdf " + '../' + filename + '3.dot' + " > " + '../' + filename + "3.pdf", shell=True)


def process_files(infile, outfile):
    lines = infile.readlines()
    listCommands = []

    for l in lines:
        print(l)
        toks = l.split()
        if "/tmp/data/filenames" in l:
            listCommands.append('"/tmp/data/filenames"')
        elif re.search("/tmp/data/.*secret.txt-2016", l):
            listCommands.append('"/tmp/data/.*secret.txt"')
        elif "strace -f cat" in l:
            listCommands.append('"strace -f cat"')
        elif 'strace' in toks:
            print (toks)
            listCommands.append(check_options(toks))
            # convert to a set
            # listCommands.append(Cmd('nmap'))
        else:
            for c in commands:
                if c in toks:
                    listCommands.append(c)
                    break
    print('-------------')
    for c in listCommands:
        print (c)
    make_dot_file(outfile, listCommands)
    
    

def check_options(tokens):
    # test if opt in line/toks
    result = '"strace'
    for o in options:
        if o in tokens:
            result = result + " " + o + " "
    # join(result)
    result = result + '"'
    return result

def make_dot_file(file, cmds):
    lines = ["digraph G { \n"]
    ## handle the first command 
    if len(cmds) > 0:
    	old = cmds[0]
    #lines.append(c)

    for i in range(1,len(cmds)):
        c = cmds[i]
        lines.append(old + " -> " + c + " [label="+str(i)+"]; ")
        old=c

    lines.append("\n } \n")
    file.writelines(lines)
    

main()
