import sys

reg = [0]*32
mem = [0]*4096

# funchk takes one line as an input at a time and calls the corresponding functions to be excuted on the registers 
def funchk(thislist,reg,mem):
    
    if thislist[0] == "jr" and thislist[1] == "$ra":
        print(mem)
        sys.exit()
                        
    elif thislist[0] == "add":
        thislist.pop(0)
        addition(thislist,reg)
        line = fp.readline()
        cnt +=1
                        
    elif thislist[0] == "sub":
        thislist.pop(0)
        subtraction(thislist,reg)
        line = fp.readline()
        cnt += 1
                        
    elif thislist[0] == "bne":
        thislist.pop(0)
        bnote(thislist,reg,mem)
        line = fp.readline()
        cnt += 1
        
    elif thislist[0]=="la":
        thislist.pop(0)
        loadarray(thislist,reg)
        line = fp.readline
        cnt += 1
        
                        
    elif thislist[0] == "lw":
        thislist.pop(0)
        loadword(thislist,reg,mem)
        line = fp.readline()
        cnt += 1
                        
    elif thislist[0] == "sw":
        thislist.pop(0)
        storeword(thislist,reg,mem)
        line = fp.readline()
        cnt += 1
                        
    elif thislist[0] == "j":
        thislist.pop(0)
        jump(thislist,reg,mem)
        line = fp.readline()
        cnt += 1
        
    elif thislist[0] == "slt":
        thislist.pop(0)
        slt(thislist,reg)
        line = fp.readline()
        cnt += 1
        
    elif thislist[0] == "li":
        thislist.pop(0)
        loadi(thislist,reg)
        line = fp.readline()
        cnt += 1
        
    else:
        thislist.pop(0)
        funchk(thislist,reg,mem)
# end of funchk                        

# the functions that funchk calls are written here
def addition(thislist,reg):
    p = linechk(thislist[0])
    q = linechk(thislist[1])
    r = linechk(thislist[2])
    
    reg[p] = reg[q] + reg[r]
    return reg[p]
    
    
def subtraction(thislist,reg):
    p = linechk(thislist[0])
    q = linechk(thislist[1])
    r = linechk(thislist[2])
    
    reg[p] = reg[q] - reg[r]
    return reg[p]
    
def bnote(thislist,reg,mem):
    p = linechk(thislist[0])
    q = linechk(thislist[1])
    n = thislist[2]
    if reg[p] != reg[q]:
        filepath = 'testcode.txt'
        with open(filepath) as ap:
            line = ap.readline()
            while line:
                line = ap.readline()
                lines = line.split(" ")
                h = list()
                for i in lines:
                    h.append(i.strip(','))
                    h.append(i.strip())
                    thislist = h
                a = ":"
                a = n + a 
                if thislist[0] == a :
                    funchk(thislist,reg,mem)
                     
                    
def jump(thislist,reg,mem):
    l = thislist[0]
    filepath = 'testcode.txt'
    with open(filepath) as bp:
            line = bp.readline()
            while line:
                    line = bp.readline()
                    lines = line.split(" ")
                    h = list()
                    for i in lines:
                        h.append(i.strip(','))
                        h.append(i.strip())
                        thislist = h
                    a = ":"
                    a = l + a 
                    if thislist[0] == a:
                        funchk(thislist,reg,mem)
                    

def slt(thislist,reg):
    p = linechk(thislist[0])
    q = linechk(thislist[1])
    r = linechk(thislist[2])
    
    if reg[q] < reg[r] :
        reg[p] = 1
    else :
         reg[p] = 0
         
    return reg[p]
        
def loadarray(thislist,reg):
    p = linechk(thislist[0])
    reg[p] = 0
    
    return reg[p]
    
    
def loadword(thislist,reg,mem):
    a = thislist[1]
    b = a.split("(")
    c = b[1].split(")")

    p = linechk(thislist[0])
    q = linechk(c[0])
    r = int(b[0])
    reg[p] = mem[ reg[q] + (r/4) ]
    
    return reg[p]
    
    
def storeword(thislist,reg,mem):
    a = thislist[1]
    b = a.split("(")
    c = b[1].split(")")

    p = linechk(thislist[0])
    q = linechk(c[0])
    r = int(b[0])
    mem[ reg[q] + (r/4) ] = reg[p]
    
    return mem[ reg[q] + (r/4) ]
    
    
def loadi(thislist,reg):
    p = linechk(thislist[0])
    reg[p] = int(thislist[1])
    
    return reg[p]
# end of the functions to be called by funchk
    
def linechk(i):
    
    if i == "$s0":
        k=0
    elif i == "$s1":
        k=1
    elif i == "$s2":
        k=2
    elif i == "$s3":
        k=3
    elif i == "$s4":
        k=4
    elif i == "$s5":
        k=5
    elif i == "$s6":
        k=6
    elif i == "$s7":
        k=7
        
    elif i == "$t0":
        k=8
    elif i == "$t1":
        k=9
    elif i == "$t2":
        k=10
    elif i == "$t3":
        k=11
    elif i == "$t4":
        k=12
    elif i == "$t5":
        k=13
    elif i == "$t6":
        k=14
    elif i == "$t7":
        k=15
    elif i == "$t8":
        k=16
    elif i == "$t9":
        k=17
        
    elif i == "$zero":
        k=18
        
    elif i == "$a0":
        k=19
    elif i == "$a1":
        k=20
    elif i == "$a2":
        k=21
    elif i == "$a3":
        k=22
        
    elif i == "$v0":
        k=23
    elif i == "$v1":
        k=24
        
    elif i == "$gp":
        k=25
    elif i == "$fp":
        k=26
    elif i == "$sp":
        k=27
        
    elif i == "$ra":
        k=28
    elif i == "$at":
        k=29
        
    elif i == "$k0":
        k=30
    elif i == "$k1":
        k=31
    return k

# main code starts from here
filepath = 'testcode.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        if line == ".data":
            cnt = 2
            line = fp.readline()
        if cnt == 2:
            if line =="array:":
                line = fp.readline()
                lines =line.strip('.word')
                lines = lines.split(",")
                f = list()
                for i in lines:
                    f.append(i.strip())
                    thislist1 = f
                
                h = thislist1.len()
                c = 0
                while c < h:
                    mem[c] = int(thislist1[c])
                    c+=1
        
            cnt = 3       
            line = fp.readline()
        if cnt == 3:
            if line == ".text":
                cnt = 4
                line = fp.readline()
        if cnt == 4:
            if line == ".globl main":
                cnt = 5
                line = fp.readline()
        if cnt == 5:
            if line == "main:":
                cnt = 6 
                line = fp.readline()
                lines = line.split(",")
                h = list()
                for i in lines:
                    h.append(i.strip())
                    thislist = h
                line = fp.readline()            
        if cnt >=6:
            funchk(thislist,reg,mem)
                    
