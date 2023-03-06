import random

game  = True
rdict = {
    "1" : "Cik būs 2 + 2?",
    "2" : "Kads tagad ir gads?",
    "3" : "Cik būs 200 - 10 * 2? "
}
a = '''
     /\         
    /  \         
   / /\ \                              
  / ____ \         
 /_/    \_\
'''
b = '''
 _____
 |  _ \         
 | |_) |        
 |  _ <         
 | |_) |        
 |____/   
'''
c =  '''
  _____       
 / ____|      
 | |           
 | |           
 | |____       
 \_____|   
'''
d = '''
  _____         
 |  __ \        
 | |  | |       
 | |  | |       
 | |__| |       
 |_____/    
'''
e = '''
  ______        
 |  ____|       
 | |__          
 |  __|         
 | |____        
 |______|       
'''
f = '''
  ______        
 |  ____|       
 | |__          
 |  __|         
 | |            
 |_|
'''
g = '''
   _____        
  / ____|       
 | |  __        
 | | |_ |       
 | |__| |       
  \_____|  
'''

h = '''
  _    _        
 | |  | |       
 | |__| |       
 |  __  |       
 | |  | |       
 |_|  |_|       
'''

i = '''
  _____         
 |_   _|        
   | |          
   | |          
  _| |_         
 |_____|     
'''

j = '''
       _        
      | |       
      | |       
  _   | |       
 | |__| |       
  \____/        
'''

k = '''
  _  __         
 | |/ /         
 | ' /          
 |  <           
 | . \          
 |_|\_\         
'''

l = '''
  _            
 | |            
 | |            
 | |            
 | |____        
 |______|       
'''

m = '''
  __  __        
 |  \/  |       
 | \  / |       
 | |\/| |       
 | |  | |       
 |_|  |_|   
'''

n = '''
  _   _         
 | \ | |        
 |  \| |        
 | . ` |        
 | |\  |        
 |_| \_|        
'''

o = '''
   ____         
  / __ \        
 | |  | |       
 | |  | |       
 | |__| |       
  \____/            
'''

p = '''
  _____         
 |  __ \        
 | |__) |       
 |  ___/        
 | |            
 |_|
'''

q = '''
   ____         
  / __ \        
 | |  | |       
 | |  | |       
 | |__| |       
  \___\_\       
'''

r = '''
  _____         
 |  __ \        
 | |__) |       
 |  _  /        
 | | \ \        
 |_|  \_\       
'''

s = '''
   _____        
  / ____|       
 | (___         
  \___ \        
  ____) |       
 |_____/
'''

t = '''
  _______  
 |__   __| 
    | |    
    | |    
    | |    
    |_|  
'''

u = '''
  _    _   
 | |  | |  
 | |  | |  
 | |  | |  
 | |__| |  
  \____/   
'''

v = '''
 __      __
 \ \    / /
  \ \  / / 
   \ \/ /  
    \  /   
'''

w = '''
 __          __
 \ \        / /
  \ \  /\  / / 
   \ \/  \/ /  
    \  /\  /   
     \/  \/    
'''

x = '''
 __   __   
 \ \ / /   
  \ V /    
   > <     
  / . \    
 /_/ \_\
'''

y = '''
 __     __ 
 \ \   / / 
  \ \_/ /  
   \   /   
    | |    
    |_|
'''


z = '''
  ______
 |___  /
    / / 
   / /  
  / /__ 
 /_____|
'''





randnum = random.randint(1, 3)
while game:    
    if randnum == 1:
        print(rdict.get("1"))
        answer = int(input("Jūsu atbilde: "))
        if answer == 4:
            print("Ļoti labi! Man ir davana tev! Uzraksti savu vardu!")
            name = str(input("Jūsu vard šeit: "))
            for lit in name:
                if lit == "a":
                    print(a)
                if lit == "b":
                    print(b)
                if lit == "c":
                    print(c)
                if lit == "d":
                    print(d)
                if lit == "e":
                    print(e)
                if lit == "f":
                    print(f)
                if lit == "g":
                    print(g)
                if lit == "h":
                    print(h)
                if lit == "i":
                    print(i)
                if lit == "j":
                    print(j)
                if lit == "k":
                    print(k)
                if lit == "l":
                    print(l)
                if lit == "m":
                    print(m)
                if lit == "n":
                    print(n)
                if lit == "o":
                    print(o)
                if lit == "p":
                    print(p)
                if lit == "q":
                    print(q)
                if lit == "r":
                    print(r)
                if lit == "s":
                    print(s)
                if lit == "t":
                    print(t)
                if lit == "u":
                    print(u)
                if lit == "v":
                    print(v)
                if lit == "w":
                    print(w)
                if lit == "x":
                    print(x)
                if lit == "y":
                    print(y)
                if lit == "z":
                    print(z)
            game = False
        else:
            print("Es uzvaru! Ha, ha, ha!")
            game  = False
    elif randnum == 2:
        print(rdict.get("2"))
        answer = int(input("Jūsu atbilde: "))
        if answer == 2023:
            print("Ļoti labi! Man ir davana tev! Uzraksti savu vardu!")
            name = str(input("Jūsu vard šeit: "))
            for lit in name:
                if lit == "a":
                    print(a)
                if lit == "b":
                    print(b)
                if lit == "c":
                    print(c)
                if lit == "d":
                    print(d)
                if lit == "e":
                    print(e)
                if lit == "f":
                    print(f)
                if lit == "g":
                    print(g)
                if lit == "h":
                    print(h)
                if lit == "i":
                    print(i)
                if lit == "j":
                    print(j)
                if lit == "k":
                    print(k)
                if lit == "l":
                    print(l)
                if lit == "m":
                    print(m)
                if lit == "n":
                    print(n)
                if lit == "o":
                    print(o)
                if lit == "p":
                    print(p)
                if lit == "q":
                    print(q)
                if lit == "r":
                    print(r)
                if lit == "s":
                    print(s)
                if lit == "t":
                    print(t)
                if lit == "u":
                    print(u)
                if lit == "v":
                    print(v)
                if lit == "w":
                    print(w)
                if lit == "x":
                    print(x)
                if lit == "y":
                    print(y)
                if lit == "z":
                    print(z)
            game = False
        else:
            print("Es uzvaru! Ha, ha, ha!")
            game  = False
    elif randnum == 3:
        print(rdict.get("3"))
        answer = int(input("Jūsu atbilde: "))
        if answer == 380:
            print("Ļoti labi! Man ir davana tev! Uzraksti savu vardu!")
            name = str(input("Jūsu vard šeit: "))
            for lit in name:
                if lit == "a":
                    print(a)
                if lit == "b":
                    print(b)
                if lit == "c":
                    print(c)
                if lit == "d":
                    print(d)
                if lit == "e":
                    print(e)
                if lit == "f":
                    print(f)
                if lit == "g":
                    print(g)
                if lit == "h":
                    print(h)
                if lit == "i":
                    print(i)
                if lit == "j":
                    print(j)
                if lit == "k":
                    print(k)
                if lit == "l":
                    print(l)
                if lit == "m":
                    print(m)
                if lit == "n":
                    print(n)
                if lit == "o":
                    print(o)
                if lit == "p":
                    print(p)
                if lit == "q":
                    print(q)
                if lit == "r":
                    print(r)
                if lit == "s":
                    print(s)
                if lit == "t":
                    print(t)
                if lit == "u":
                    print(u)
                if lit == "v":
                    print(v)
                if lit == "w":
                    print(w)
                if lit == "x":
                    print(x)
                if lit == "y":
                    print(y)
                if lit == "z":
                    print(z)
            game = False
        else:
            print("Es uzvaru! Ha, ha, ha!")
            game  = False


