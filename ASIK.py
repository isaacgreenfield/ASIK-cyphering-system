import random

def Whopper(a, b):
    if(ord(a) + b > 11000): return chr(ord(a) + b - 11000)
    return chr(ord(a) + b) 

def Reversed_Whopper(a, b):
    if(ord(a) - b < 0): return chr(ord(a) - b + 11000)
    return chr(ord(a) - b)

def First_part(t):
    global x
    t = list(t)
    x = random.randint(3, 810)
    for i in range(len(t)):
        t[i] = Whopper(t[i], x)
    t.append(chr(x))    
    return ''.join(t)   

def Second_part(t):
    global y
    y = random.randint(3, 810)
    t = list(t)
    for i in range(len(t)):
        t[i] = Whopper(t[i], y)
    t.append(chr(y))
    return ''.join(t)

def Third_part(t):
    global z
    z = random.randint(3, 810)
    t = list(t)
    for i in range(len(t)):
        t[i] = Whopper(t[i], z)
    t.append(chr(z))
    return ''.join(t) 

def In(text):
    l = (int)(len(text)/3)
    return First_part(text[:l]) + Second_part(text[l:2*l]) + Third_part(text[2*l:])

def Out(cypher):
    cypher = list(cypher)
    l = (int)(len(cypher)/3)
    here_x = ord(cypher[l - 1])
    here_y = ord(cypher[2*l - 1])
    here_z = ord(cypher[3*l])
    for i in range(l):
        cypher[i] = Reversed_Whopper(cypher[i], here_x)
    for i in range(l, 2*l):
        cypher[i] = Reversed_Whopper(cypher[i], here_y)
    for i in range(2*l, 3*l + 1):
        cypher[i] = Reversed_Whopper(cypher[i], here_z)
    return ''.join(cypher)            

Message = input()
print("Original message: " + Message)
print("system: " + In(Message))
print("out: " + Out(In(Message)))