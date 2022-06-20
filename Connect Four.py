#!/usr/bin/env python
# coding: utf-8

# In[3]:


debug_mode=0

#imports
import random

#Board array 
board=[[[0] for i in range(7)]for j in range(7)]
fc=[]
ch=[0 for i in range(7)]
#0 is empty
#1 and 2 are players one and two respectively
if debug_mode==1:
    print(board)
def print_board(board):
    top="|     |"
    for i in range(7):
        if i<9:
            top+=(" C"+str(i+1)+"  | ")
        else:
            top+=("C"+str(i+1)+"  | ")
    print(top)
    e1=0
    for i in range(7):
        if i<9:
            line="|  R"+str(e1+1)+" |"
        else:
            line="| R"+str(e1+1)+" |"
        e1+=1
        for e in range(7):
            if board[e][i][0]==0:
                line+="     | "
                continue
            if board[e][i][0]==1:
                line+="  X  | "
                continue
            if board[e][i][0]==2:
                line+="  O  | "
                continue
               
        print(line)
        
if debug_mode==1:
    print_board(board)
    

def coin_vis(coin_vis_val):
    
    if coin_vis_val==1:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  H  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
        
    if coin_vis_val==0:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  T  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
        
coin=[0, 1]

p1=str(input("Enter Player 1 name: "))
while len(p1)==0:
    print("You have to enter a name")
    p1=str(input("Enter Player 1 name: "))
    
p2=str(input("Enter Player 2 name: "))
while len(p2)==0:
    print("You have to enter a name")
    p2=str(input("Enter Player 2 name: "))

p2f=0

input("Press Enter to flip a coin to see who goes first.")

speed_tie_breaker=random.choice(coin)
pf2=0                                
if speed_tie_breaker==1:
    coin_vis(1)
    print('Heads')
    print(p1+' plays first')
    
    
if speed_tie_breaker==0:
    coin_vis(0)
    print('Tails')
    print(p2+' plays first')
    p2f=1
    p1,p2=p2,p1
    
    
x=0
y=0
    
def play(player):
    while True:
        cn=input("Enter the columb number you wish to drop a coin in: ")
        if not cn.isdigit():
            print("You have not entered a number, please try again:")
            continue
        if int(cn) in fc:
            print("That columb is full try a diffrent columb:")
            continue
        if cn.isdigit():
            if 0<int(cn) and int(cn)<8:
                cn=int(cn)-1
                break
            else:
                print("You have entered an invalid number, Enter a number between 1 and 7:")
        
    
    
    board[cn][6-ch[cn]][0]=player
    
    x=cn
    y=6-ch[cn]
    
    ch[cn]+=1
    if ch[cn]==7:
        fc.append(cn+1)
    
    
    
    
def check_win(player):
    if debug_mode==1:
        print("x,y,player:")
        print(x,y,player)
        print(board[x][y][0])
    c1=0
    c2=0
    for i in range(7):
        for e in range(7):
            if board[i][e][0]==player:
                c1+=1
                if c1>=4:
                    return player
            else:
                c1=0
            if board[e][i][0]==player:
                c2+=1
                if c2>=4:
                    return player
            else:
                c2=0
    return 0
    
    
    
    
    
    
gip=1
w=0
while gip==1:
    if w==0:
        play(pf2+1)
    if w==0:
        w=check_win(1)
    if w==0:
        w=check_win(2)
    if pf2==0:
        pf2=1
    elif pf2==1:
        pf2=0
        
    print_board(board)
    if debug_mode==1:
        print(w)
    if w==1:
        print(p1+" wins")
        gip=0
        break
    if w==2:
        print(p2+" wins")
        gip=0
        break


# In[ ]:





# In[ ]:




