from PIL import Image, ImageGrab
import random as r
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from tkinter import *
from math import ceil
from time import time
import webbrowser



x=0;y=0
count=0
cross_counter=0
zero_counter=0
flag=False

    

def computer_zero():
    
    global x,y
    
    if zb_list[0]==zb_list[1]==1 and cb_list[2]==0:
        x=0;y=2*500/3
    elif zb_list[1]==zb_list[2]==1 and cb_list[0]==0:
        x=0;y=0
    elif zb_list[0]==zb_list[2]==1 and cb_list[1]==0:
        x=0;y=500/3
    
    elif zb_list[3]==zb_list[4]==1 and cb_list[5]==0:
        x=500/3;y=2*500/3
    elif zb_list[3]==zb_list[5]==1 and cb_list[4]==0:
        x=500/3;y=500/3
    elif zb_list[4]==zb_list[5]==1 and cb_list[3]==0:
        x=500/3;y=0
        
    elif zb_list[6]==zb_list[7]==1 and cb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif zb_list[6]==zb_list[8]==1 and cb_list[7]==0:
        x=2*500/3;y=500/3
    elif zb_list[7]==zb_list[8]==1 and cb_list[6]==0:
        x=2*500/3;y=0
        
    elif zb_list[0]==zb_list[3]==1 and cb_list[6]==0:
        x=2*500/3;y=0
    elif zb_list[0]==zb_list[6]==1 and cb_list[3]==0:
        x=500/3;y=0
    elif zb_list[3]==zb_list[6]==1 and cb_list[0]==0:
        x=0;y=0
    
    elif zb_list[1]==zb_list[4]==1 and cb_list[7]==0:
        x=2*500/3;y=500/3
    elif zb_list[1]==zb_list[7]==1 and cb_list[4]==0:
        x=500/3;y=500/3
    elif zb_list[4]==zb_list[7]==1 and cb_list[1]==0:
        x=0;y=500/3
        
    elif zb_list[2]==zb_list[5]==1 and cb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif zb_list[2]==zb_list[8]==1 and cb_list[5]==0:
        x=500/3;y=2*500/3
    elif zb_list[5]==zb_list[8]==1 and cb_list[2]==0:
        x=0;y=2*500/3
        
    elif zb_list[0]==zb_list[4]==1 and cb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif zb_list[0]==zb_list[8]==1 and cb_list[4]==0:
        x=500/3;y=500/3
    elif zb_list[4]==zb_list[8]==1 and cb_list[0]==0:
        x=0;y=0
        
    elif zb_list[2]==zb_list[4]==1 and cb_list[6]==0:
        x=2*500/3;y=0
    elif zb_list[2]==zb_list[6]==1 and cb_list[4]==0:
        x=500/3;y=500/3
    elif zb_list[4]==zb_list[6]==1 and cb_list[2]==0:
        x=0;y=2*500/3

    
    
    
    
    elif cb_list[0]==cb_list[1]==1 and cb_list[2]==zb_list[2]==0:
        x=0;y=2*500/3
    elif cb_list[1]==cb_list[2]==1 and cb_list[0]==zb_list[0]==0:
        x=0;y=0
    elif cb_list[0]==cb_list[2]==1 and cb_list[1]==zb_list[1]==0:
        x=0;y=500/3
    
    elif cb_list[3]==cb_list[4]==1 and cb_list[5]==zb_list[5]==0:
        x=500/3;y=2*500/3
    elif cb_list[3]==cb_list[5]==1 and cb_list[4]==zb_list[4]==0:
        x=500/3;y=500/3
    elif cb_list[4]==cb_list[5]==1 and cb_list[3]==zb_list[3]==0:
        x=500/3;y=0
        
    elif cb_list[6]==cb_list[7]==1 and cb_list[8]==zb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif cb_list[6]==cb_list[8]==1 and cb_list[7]==zb_list[7]==0:
        x=2*500/3;y=500/3
    elif cb_list[7]==cb_list[8]==1 and cb_list[6]==zb_list[6]==0:
        x=2*500/3;y=0
        
    elif cb_list[0]==cb_list[3]==1 and cb_list[6]==zb_list[6]==0:
        x=2*500/3;y=0
    elif cb_list[0]==cb_list[6]==1 and cb_list[3]==zb_list[3]==0:
        x=500/3;y=0
    elif cb_list[3]==cb_list[6]==1 and cb_list[0]==zb_list[0]==0:
        x=0;y=0
    
    elif cb_list[1]==cb_list[4]==1 and cb_list[7]==zb_list[7]==0:
        x=2*500/3;y=500/3
    elif cb_list[1]==cb_list[7]==1 and cb_list[4]==zb_list[4]==0:
        x=500/3;y=500/3
    elif cb_list[4]==cb_list[7]==1 and cb_list[1]==zb_list[1]==0:
        x=0;y=500/3
        
    elif cb_list[2]==cb_list[5]==1 and cb_list[8]==zb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif cb_list[2]==cb_list[8]==1 and cb_list[5]==zb_list[5]==0:
        x=500/3;y=2*500/3
    elif cb_list[5]==cb_list[8]==1 and cb_list[2]==zb_list[2]==0:
        x=0;y=2*500/3
        
    elif cb_list[0]==cb_list[4]==1 and cb_list[8]==zb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif cb_list[0]==cb_list[8]==1 and cb_list[4]==zb_list[4]==0:
        x=500/3;y=500/3
    elif cb_list[4]==cb_list[8]==1 and cb_list[0]==zb_list[0]==0:
        x=0;y=0
        
    elif cb_list[2]==cb_list[4]==1 and cb_list[6]==zb_list[6]==0:
        x=2*500/3;y=0
    elif cb_list[2]==cb_list[6]==1 and cb_list[4]==zb_list[4]==0:
        x=500/3;y=500/3
    elif cb_list[4]==cb_list[6]==1 and cb_list[2]==zb_list[2]==0:
        x=0;y=2*500/3
    
    
    else:
        while True:
            m=0
            index_list=[]
            rand=r.randint(0,8)
            combined_list=cb_list+zb_list
            for i in combined_list:
                if i==1:
                    index_list.append(m)
                m+=1
            if combined_list.count(1)==9:
                break
            elif rand in index_list or (rand+9) in index_list:
                continue
            else:
                if rand==0:
                    x=0;y=0
                elif rand==1:
                    x=0;y=500/3
                elif rand==2:
                    x=0;y=2*500/3
                    
                if rand==3:
                    x=500/3;y=0
                elif rand==4:
                    x=500/3;y=500/3
                elif rand==5:
                    x=500/3;y=2*500/3
                
                if rand==6:
                    x=2*500/3;y=0
                elif rand==7:
                    x=2*500/3;y=500/3
                elif rand==8:
                    x=2*500/3;y=2*500/3
                break
    zero()
    canvas.update()
    checkwin()
        
def computer_cross():
    global x,y
    
    if cb_list[0]==cb_list[1]==1 and zb_list[2]==0:
        x=0;y=2*500/3
    elif cb_list[1]==cb_list[2]==1 and zb_list[0]==0:
        x=0;y=0
    elif cb_list[0]==cb_list[2]==1 and zb_list[1]==0:
        x=0;y=500/3
    
    elif cb_list[3]==cb_list[4]==1 and zb_list[5]==0:
        x=500/3;y=2*500/3
    elif cb_list[3]==cb_list[5]==1 and zb_list[4]==0:
        x=500/3;y=500/3
    elif cb_list[4]==cb_list[5]==1 and zb_list[3]==0:
        x=500/3;y=0
        
    elif cb_list[6]==cb_list[7]==1 and zb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif cb_list[6]==cb_list[8]==1 and zb_list[7]==0:
        x=2*500/3;y=500/3
    elif cb_list[7]==cb_list[8]==1 and zb_list[6]==0:
        x=2*500/3;y=0
        
    elif cb_list[0]==cb_list[3]==1 and zb_list[6]==0:
        x=2*500/3;y=0
    elif cb_list[0]==cb_list[6]==1 and zb_list[3]==0:
        x=500/3;y=0
    elif cb_list[3]==cb_list[6]==1 and zb_list[0]==0:
        x=0;y=0
    
    elif cb_list[1]==cb_list[4]==1 and zb_list[7]==0:
        x=2*500/3;y=500/3
    elif cb_list[1]==cb_list[7]==1 and zb_list[4]==0:
        x=500/3;y=500/3
    elif cb_list[4]==cb_list[7]==1 and zb_list[1]==0:
        x=0;y=500/3
        
    elif cb_list[2]==cb_list[5]==1 and zb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif cb_list[2]==cb_list[8]==1 and zb_list[5]==0:
        x=500/3;y=2*500/3
    elif cb_list[5]==cb_list[8]==1 and zb_list[2]==0:
        x=0;y=2*500/3
        
    elif cb_list[0]==cb_list[4]==1 and zb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif cb_list[0]==cb_list[8]==1 and zb_list[4]==0:
        x=500/3;y=500/3
    elif cb_list[4]==cb_list[8]==1 and zb_list[0]==0:
        x=0;y=0
        
    elif cb_list[2]==cb_list[4]==1 and zb_list[6]==0:
        x=2*500/3;y=0
    elif cb_list[2]==cb_list[6]==1 and zb_list[4]==0:
        x=500/3;y=500/3
    elif cb_list[4]==cb_list[6]==1 and zb_list[2]==0:
        x=0;y=2*500/3
    
    elif zb_list[0]==zb_list[1]==1 and zb_list[2]==cb_list[2]==0:
        x=0;y=2*500/3
    elif zb_list[1]==zb_list[2]==1 and zb_list[0]==cb_list[0]==0:
        x=0;y=0
    elif zb_list[0]==zb_list[2]==1 and zb_list[1]==cb_list[1]==0:
        x=0;y=500/3
    
    elif zb_list[3]==zb_list[4]==1 and zb_list[5]==cb_list[5]==0:
        x=500/3;y=2*500/3
    elif zb_list[3]==zb_list[5]==1 and zb_list[4]==cb_list[4]==0:
        x=500/3;y=500/3
    elif zb_list[4]==zb_list[5]==1 and zb_list[3]==cb_list[3]==0:
        x=500/3;y=0
        
    elif zb_list[6]==zb_list[7]==1 and zb_list[8]==cb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif zb_list[6]==zb_list[8]==1 and zb_list[7]==cb_list[7]==0:
        x=2*500/3;y=500/3
    elif zb_list[7]==zb_list[8]==1 and zb_list[6]==cb_list[6]==0:
        x=2*500/3;y=0
        
    elif zb_list[0]==zb_list[3]==1 and zb_list[6]==cb_list[6]==0:
        x=2*500/3;y=0
    elif zb_list[0]==zb_list[6]==1 and zb_list[3]==cb_list[3]==0:
        x=500/3;y=0
    elif zb_list[3]==zb_list[6]==1 and zb_list[0]==cb_list[0]==0:
        x=0;y=0
    
    elif zb_list[1]==zb_list[4]==1 and zb_list[7]==cb_list[7]==0:
        x=2*500/3;y=500/3
    elif zb_list[1]==zb_list[7]==1 and zb_list[4]==cb_list[4]==0:
        x=500/3;y=500/3
    elif zb_list[4]==zb_list[7]==1 and zb_list[1]==cb_list[1]==0:
        x=0;y=500/3
        
    elif zb_list[2]==zb_list[5]==1 and zb_list[8]==cb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif zb_list[2]==zb_list[8]==1 and zb_list[5]==cb_list[5]==0:
        x=500/3;y=2*500/3
    elif zb_list[5]==zb_list[8]==1 and zb_list[2]==cb_list[2]==0:
        x=0;y=2*500/3
        
    elif zb_list[0]==zb_list[4]==1 and zb_list[8]==cb_list[8]==0:
        x=2*500/3;y=2*500/3
    elif zb_list[0]==zb_list[8]==1 and zb_list[4]==cb_list[4]==0:
        x=500/3;y=500/3
    elif zb_list[4]==zb_list[8]==1 and zb_list[0]==cb_list[0]==0:
        x=0;y=0
        
    elif zb_list[2]==zb_list[4]==1 and zb_list[6]==cb_list[6]==0:
        x=2*500/3;y=0
    elif zb_list[2]==zb_list[6]==1 and zb_list[4]==cb_list[4]==0:
        x=500/3;y=500/3
    elif zb_list[4]==zb_list[6]==1 and zb_list[2]==cb_list[2]==0:
        x=0;y=2*500/3
    else:
        while True:
            m=0
            index_list=[]
            rand=r.randint(0,8)
            combined_list=cb_list+zb_list
            for i in combined_list:
                if i==1:
                    index_list.append(m)
                m+=1
            if combined_list.count(1)==9:
                break
            elif rand in index_list or (rand+9) in index_list:
                continue
            else:
                if rand==0:
                    x=0;y=0
                elif rand==1:
                    x=0;y=500/3
                elif rand==2:
                    x=0;y=2*500/3
                    
                if rand==3:
                    x=500/3;y=0
                elif rand==4:
                    x=500/3;y=500/3
                elif rand==5:
                    x=500/3;y=2*500/3
                
                if rand==6:
                    x=2*500/3;y=0
                elif rand==7:
                    x=2*500/3;y=500/3
                elif rand==8:
                    x=2*500/3;y=2*500/3
                break
    cross()
    canvas.update()
    checkwin()

def computer_move():
    if flag==True:
        return True
    elif count%2==0:
        computer_cross()
    else:
        computer_zero()
        
    
    

def validate_input(new_text):
    return len(new_text) <= 8

def draw():
    global flag
    flag=True

def cross_win():
    global cross_counter, zero_counter, count, flag
    count=3
    flag=True
    cross_counter+=1
    if cb_list.count(1)==zb_list.count(1):
        count=count+1
    canvas.itemconfig(text1,text=f'{ent1.get()} = {cross_counter}')

def zero_win():
    global cross_counter, zero_counter, count,flag
    count=2
    flag=True
    zero_counter+=1
    if cb_list.count(1)==zb_list.count(1):
        count=count+1
    canvas.itemconfig(text2,text=f'{ent2.get()} = {zero_counter}')
    


def checkwin():
    global cross_counter, zero_counter,zb_list,cb_list
    img = ImageGrab.grab((canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + 600, canvas.winfo_rooty() + 600))

    zero_list=[img.getpixel((80,100/3))
                ,img.getpixel((80,100/3+500/3))
                ,img.getpixel((80,100/3+500/3+500/3))
                ,img.getpixel((80+500/3,100/3))
                ,img.getpixel((80+500/3,100/3+500/3))
                ,img.getpixel((80+500/3,100/3+500/3+500/3))
                ,img.getpixel((80+500/3+500/3,100/3))
                ,img.getpixel((80+500/3+500/3,100/3+500/3))
                ,img.getpixel((80+500/3+500/3,100/3+500/3+500/3))]

    cross_list=[img.getpixel((250/3,250/3))
                ,img.getpixel((250/3,250/3+500/3))
                ,img.getpixel((250/3,250/3+500/3+500/3))
                ,img.getpixel((250/3+500/3,250/3))
                ,img.getpixel((250/3+500/3,250/3+500/3))
                ,img.getpixel((250/3+500/3,250/3+500/3+500/3))
                ,img.getpixel((250/3+500/3+500/3,250/3))
                ,img.getpixel((250/3+500/3+500/3,250/3+500/3))
                ,img.getpixel((250/3+500/3+500/3,250/3+500/3+500/3))]

    cb_list=[]
    zb_list=[]

    for i in range(9):
        if zero_list[i]==(0,0,255):
            zb_list.append(1)
        else:
            zb_list.append(0)
            
        if cross_list[i]==(255,0,0):
            cb_list.append(1)
        else:
            cb_list.append(0)
        
    if cb_list[0]==cb_list[1]==cb_list[2]==1:
        canvas.create_line(250/3,250/3-65,250/3,250/3+400,width=8,fill='red',tag='line')
        cross_win()
        
    elif cb_list[3]==cb_list[4]==cb_list[5]==1:
        canvas.create_line(250/3+500/3,250/3-65,250/3+500/3,250/3+400,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[6]==cb_list[7]==cb_list[8]==1:
        canvas.create_line(250/3+2*500/3,250/3-65,250/3+2*500/3,250/3+400,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[0]==cb_list[3]==cb_list[6]==1:
        canvas.create_line(250/3-65,250/3,250/3+400,250/3,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[1]==cb_list[4]==cb_list[7]==1:
        canvas.create_line(250/3-65,250/3+500/3,250/3+400,250/3+500/3,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[2]==cb_list[5]==cb_list[8]==1:
        canvas.create_line(250/3-65,250/3+2*500/3,250/3+400,250/3+2*500/3,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[0]==cb_list[4]==cb_list[8]==1:
        canvas.create_line(40,40,460,460,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[6]==cb_list[4]==cb_list[2]==1:
        canvas.create_line(40,460,460,40,width=8,fill='red',tag='line')
        cross_win()
    
    
    elif zb_list[0]==zb_list[1]==zb_list[2]==1:
        canvas.create_line(250/3,250/3-65,250/3,250/3+400,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[3]==zb_list[4]==zb_list[5]==1:
        canvas.create_line(250/3+500/3,250/3-65,250/3+500/3,250/3+400,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[6]==zb_list[7]==zb_list[8]==1:
        canvas.create_line(250/3+2*500/3,250/3-65,250/3+2*500/3,250/3+400,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[0]==zb_list[3]==zb_list[6]==1:
        canvas.create_line(250/3-65,250/3,250/3+400,250/3,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[1]==zb_list[4]==zb_list[7]==1:
        canvas.create_line(250/3-65,250/3+500/3,250/3+400,250/3+500/3,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[2]==zb_list[5]==zb_list[8]==1:
        canvas.create_line(250/3-65,250/3+2*500/3,250/3+400,250/3+2*500/3,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[0]==zb_list[4]==zb_list[8]==1:
        canvas.create_line(40,40,460,460,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[6]==zb_list[4]==zb_list[2]==1:
        canvas.create_line(40,460,460,40,width=8,fill='blue',tag='line')
        zero_win()
    
    elif zb_list.count(1)+cb_list.count(1)==9:
        
        draw()
    
    
    
    else:
        return True


def zero():
    global count
    canvas.create_oval(100/3+x,100/3+y,400/3+x,400/3+y,outline='blue',width=8,tag='zero')
    count+=1
       
    
def cross():
    global count
    canvas.create_line(100/3+x,100/3+y,400/3+x,400/3+y,fill='red',width=8,tag='cross')
    canvas.create_line(400/3+x,100/3+y,100/3+x,400/3+y,fill='red',width=8,tag='cross')
    count+=1
    
def clicked2(evt):
    global x, y, count,flag
    if flag==True:
        canvas.delete('cross')
        canvas.delete('zero')
        canvas.delete('line')
        if count%2==0:
            canvas.itemconfig(text1,font='Ariel 28')
            canvas.itemconfig(text2,font='Ariel 20')
        else:
            canvas.itemconfig(text1,font='Ariel 20')
            canvas.itemconfig(text2,font='Ariel 28')
        flag=False
    elif checkwin()==True:
        if 0<evt.x<500/3 and 0<evt.y<500/3:
            x=0;y=0
        if 0<evt.x<500/3 and 500/3<evt.y<1000/3:
            x=0;y=500/3
        if 0<evt.x<500/3 and 500/3+500/3<evt.y<1000/3+500/3:
            x=0;y=2*500/3
            
        if 500/3<evt.x<500/3+500/3 and 0<evt.y<500/3:
            x=500/3;y=0
        if 500/3<evt.x<500/3+500/3 and 500/3<evt.y<1000/3:
            x=500/3;y=500/3
        if 500/3<evt.x<500/3+500/3 and 500/3+500/3<evt.y<1000/3+500/3:
            x=500/3;y=2*500/3

        if 2*500/3<evt.x<3*500/3 and 0<evt.y<500/3:
            x=2*500/3;y=0
        if 2*500/3<evt.x<3*500/3 and 500/3<evt.y<1000/3:
            x=2*500/3;y=500/3
        if 2*500/3<evt.x<3*500/3 and 500/3+500/3<evt.y<1000/3+500/3:
            x=2*500/3;y=2*500/3
        if 0<evt.x<500 and 500<evt.y<550:
            return True
        canvas.update()
        img = ImageGrab.grab((canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + 500, canvas.winfo_rooty() + 500))
        if img.getpixel((x+80,y+100/3))!=(0,0,255) and img.getpixel((x+250/3,y+250/3))!=(255,0,0):
            PlaySound('click.wav', SND_FILENAME|SND_ASYNC)
            if count%2==0:
                cross()
                canvas.itemconfig(text1,font='Ariel 20')
                canvas.itemconfig(text2,font='Ariel 28')
                canvas.update()
                checkwin()
            else:
                zero()
                canvas.itemconfig(text1,font='Ariel 28')
                canvas.itemconfig(text2,font='Ariel 20')
                canvas.update()
                checkwin()

def clicked(evt):
    global x, y, count,flag
    if flag==True:
        canvas.delete('cross')
        canvas.delete('zero')
        canvas.delete('line')
        flag=False
        if var.get()==1 and zb_list.count(1)<=cb_list.count(1) and count%2!=0:    #which means when player is cross
            computer_move()
        elif var.get()==2 and cb_list.count(1)<=zb_list.count(1) and count%2==0:  #which means when player is zero
             computer_move()
    elif checkwin()==True:
        if 0<evt.x<500/3 and 0<evt.y<500/3:
            x=0;y=0
        if 0<evt.x<500/3 and 500/3<evt.y<1000/3:
            x=0;y=500/3
        if 0<evt.x<500/3 and 500/3+500/3<evt.y<1000/3+500/3:
            x=0;y=2*500/3
            
        if 500/3<evt.x<500/3+500/3 and 0<evt.y<500/3:
            x=500/3;y=0
        if 500/3<evt.x<500/3+500/3 and 500/3<evt.y<1000/3:
            x=500/3;y=500/3
        if 500/3<evt.x<500/3+500/3 and 500/3+500/3<evt.y<1000/3+500/3:
            x=500/3;y=2*500/3

        if 2*500/3<evt.x<3*500/3 and 0<evt.y<500/3:
            x=2*500/3;y=0
        if 2*500/3<evt.x<3*500/3 and 500/3<evt.y<1000/3:
            x=2*500/3;y=500/3
        if 2*500/3<evt.x<3*500/3 and 500/3+500/3<evt.y<1000/3+500/3:
            x=2*500/3;y=2*500/3
        if 0<evt.x<500 and 500<evt.y<550:
            return True
        canvas.update()
        img = ImageGrab.grab((canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + 600, canvas.winfo_rooty() + 600))
        if img.getpixel((x+80,y+100/3))!=(0,0,255) and img.getpixel((x+250/3,y+250/3))!=(255,0,0):
            PlaySound('click.wav', SND_FILENAME|SND_ASYNC)
            if (count)%2==0:
                cross()
                canvas.update()
                checkwin()
                computer_move()
            else:
                zero()
                canvas.update()
                checkwin()
                computer_move()


def menu():
    global button1,button2, button3, bm,n
    canvas.destroy()
    bm=Button(root,image=sound_play,command=mute,bd=0,bg='white')
    bm.pack(side=BOTTOM,anchor=SE,padx=20,pady=20)
    button1=Button(frame, text='New Game',command=choice,font='Monaco 25 bold',bd=1,bg='white',width=15)
    button1.pack()
    button2=Button(frame, text='Exit',font='Monaco 25 bold',width=15,bd=1,bg='white',command=exit_program)
    button2.pack(pady=30)
    button3=Button(frame,text='How To Play?',font='Monaco 25 bold',width=15,bd=1,bg='white',command=howtoplay)
    button3.pack()
    PlaySound('ticsoundtrack.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)
    if n%2!=0:
        n+=1


def canv2():
    global root, canvas, text1,text2,count,ent1,ent2
    bb.destroy()
    bm.destroy()
    PlaySound(None, SND_FILENAME)
    a1.destroy()
    a2.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    canvas=Canvas(root,bg='white',height=550,width=500)
    canvas.bind('<Button-1>',clicked2)
    canvas.pack()
    btn=Button(root,bg='white',bd=0,command=menu)
    btn.pack()
    canvas.create_window(22,522,window=btn)
    btn.config(image=resign)
    btn2=Button(root,bg='white',bd=0,command=exit_program)
    btn2.pack()
    canvas.create_window(500-20,522,window=btn2)
    btn2.config(image=exit_image)
    canvas.create_line(500/3,0,500/3,500,width=10,fill='lime')
    canvas.create_line(500-500/3,0,500-500/3,500,width=10,fill='lime')
    canvas.create_line(0,500/3,500,500/3,width=10,fill='lime')
    canvas.create_line(0,500-500/3,500,500-500/3,width=10,fill='lime')
    
    text1=canvas.create_text(138,522,text=f'{ent1.get()} = {cross_counter}',font='Ariel 20',fill='red')
    text2=canvas.create_text(360,522,text=f'{ent2.get()} = {zero_counter}',font='Ariel 20',fill='blue')
    canvas.itemconfig(text1,font='Ariel 28')
    canvas.itemconfig(text2,font='Ariel 20')


def canv():
    global root, canvas, text1,text2,count,ent1,ent2
    bb.destroy()
    bm.destroy()
    PlaySound(None, SND_FILENAME)
    if var.get()==2:
        temp1=ent1
        ent1=ent2
        ent2=temp1
        count=1
    a.destroy()
    e1.destroy()
    b1.destroy()
    r1.destroy()
    r2.destroy()
    canvas=Canvas(root,bg='white',height=550,width=500)
    canvas.bind('<Button-1>',clicked)
    canvas.pack(fill=BOTH,expand=TRUE)
    
    btn=Button(root,bg='white',bd=0,command=menu)
    btn.pack()
    canvas.create_window(22,522,window=btn)
    btn.config(image=resign)
    btn2=Button(root,bg='white',bd=0,command=exit_program)
    btn2.pack()
    canvas.create_window(500-20,522,window=btn2)
    btn2.config(image=exit_image)
    
    canvas.create_line(500/3,0,500/3,500,width=10,fill='lime')
    canvas.create_line(500-500/3,0,500-500/3,500,width=10,fill='lime')
    canvas.create_line(0,500/3,500,500/3,width=10,fill='lime')
    canvas.create_line(0,500-500/3,500,500-500/3,width=10,fill='lime')
    if var.get()==1:
        text1=canvas.create_text(138,522,text=f'{ent1.get()} = {cross_counter}',font='Ariel 28',fill='red')
        text2=canvas.create_text(360,522,text=f'{ent2.get()} = {zero_counter}',font='Ariel 20',fill='blue')
    elif var.get()==2:
        text1=canvas.create_text(138,522,text=f'{ent1.get()} = {cross_counter}',font='Ariel 20',fill='red')
        text2=canvas.create_text(360,522,text=f'{ent2.get()} = {zero_counter}',font='Ariel 28',fill='blue')

def vscomputer():
    global var, a,e1,r1,r2,b1,ent1,ent2
    bb['command']=back2
    button1.destroy()
    button2.destroy()
    button3.destroy()
    ent1=StringVar()
    ent1.set('Player')
    ent2=StringVar()
    ent2.set('Computer')
    var=IntVar()
    var.set(1)
    a=Label(frame,text='Player Name:   ',bg='white',font='Comicsansms 20 bold')
    a.grid(row=1,column=0,pady=5,padx=27)
    e1=Entry(frame,textvariable=ent1,font='Ariel 15',validate="key", validatecommand=(root.register(validate_input), "%P"))
    e1.grid(row=1,column=1,columnspan=2,pady=5,ipady=2,ipadx=2)
    r1=Radiobutton(frame,text='X',font='Calibri 20 bold',fg='red',bg='white',variable=var,value=1)
    r1.grid(row=3,column=1,padx=20)
    r2=Radiobutton(frame,text='O',font='Calibri 20 bold',fg='blue',bg='white',variable=var,value=2)
    r2.grid(row=3,column=2,padx=20)
    b1=Button(frame, text='Play',command=canv,font='Ariel 15',width=15)
    b1.grid(row=5,column=1,columnspan=2,padx=2,pady=2)
    root.bind('<Return>', lambda event: b1.invoke())
    e1.focus_set()


def vsplayer():
    global  a1,a2,e1,e2,b1,ent1,ent2
    bb['command']=back2
    button1.destroy()
    button2.destroy()
    button3.destroy()
    ent1=StringVar()
    ent1.set('Player1')
    ent2=StringVar()
    ent2.set('Player2')
    a1=Label(frame,text='Player Name (X):  ',bg='white',fg='red',font='Comicsansms 20 bold')
    a1.grid(row=1,column=0,pady=5,padx=27)
    a2=Label(frame,text='Player Name (O):  ',bg='white',fg='blue',font='Comicsansms 20 bold')
    a2.grid(row=2,column=0,pady=5,padx=27)
    e1=Entry(frame,textvariable=ent1,font='Ariel 15',validate="key", validatecommand=(root.register(validate_input), "%P"))
    e1.grid(row=1,column=1,columnspan=2,pady=5,ipady=2,ipadx=2)
    e2=Entry(frame,textvariable=ent2,font='Ariel 15',validate="key", validatecommand=(root.register(validate_input), "%P"))
    e2.grid(row=2,column=1,columnspan=2,pady=5,ipady=2,ipadx=2)
    b1=Button(frame, text='Play',command=canv2,font='Ariel 15',width=15)
    b1.grid(row=5,column=1,columnspan=2,padx=2,pady=2)
    root.bind('<Return>', lambda event: b1.invoke())
    e1.focus_set()
    
def callback(url):
    webbrowser.open_new_tab(url)

def back3():
    global button3
    l1.destroy()
    l2.destroy()
    link.destroy()
    bb.destroy()
    button3=Button(frame,text='How To Play?',font='Monaco 25 bold',width=15,bd=1,bg='white',command=howtoplay)
    button3.pack()
    

def howtoplay():
    global bb, l1,l2, link
    button3.destroy()
    note=open('how to play.txt')
    bb=Button(root,image=back_image,command=back3,bd=0,bg='white')
    bb.pack(side=TOP,anchor=NW)
    l1=Label(root,text='Here are some instructions on how to play the Tic Tac Toe Game.',font='Timesnewroman 12 underline bold',bg='white', wraplength=500,padx=20,pady=10)
    l1.pack()
    l2=Label(root,text=note.read(),font='Timesnewroman 12',bg='white', wraplength=500,justify='left')
    l2.pack()
    link=Label(root,text='https://patreon.com/ashar2friends',font='Arial 12 underline',bg='white',fg='blue', wraplength=500,justify='left', cursor="hand2")
    link.pack(side=LEFT)
    link.bind("<Button-1>", lambda e: callback("https://patreon.com/ashar2friends"))
    note.close()
    
    
    

def choice():
    global bb
    bb=Button(root,image=back_image,command=back1,bd=0,bg='white',font='Ariel 20')
    bb.pack(side=TOP,anchor=NW,padx=10,pady=10)
    button1['text']='With Computer'
    button1['command']=vscomputer
    button2['text']='With Friend'
    button2['command']=vsplayer
    button3.destroy()


n=0
def mute():
    global n,bm
    if n%2==0:
        PlaySound(None, SND_FILENAME)
        bm.destroy()
        bm=Button(root,image=sound_mute,command=mute,bd=0)
        bm.pack(side=BOTTOM,anchor=SE,padx=20,pady=20)
    else:
        PlaySound('ticsoundtrack.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)
        bm.destroy()
        bm=Button(root,image=sound_play,command=mute,bd=0)
        bm.pack(side=BOTTOM,anchor=SE,padx=20,pady=20)
    n+=1

def exit_program():
    PlaySound(None, SND_FILENAME)
    root.destroy()

def back1():
    global button3
    button1['text']='Play'
    button1['command']=choice
    button2['text']='Exit'
    button2['command']=exit_program
    button3=Button(frame,text='How To Play?',font='Monaco 25 bold',width=15,bd=1,bg='white',command=howtoplay)
    button3.pack()
    
    bb.destroy()

def back2():
    global bb,button1,button2
    bb['command']=back1
    try:
        a.destroy()
        e1.destroy()
        b1.destroy()
        r1.destroy()
        r2.destroy()
    except:
        pass
    
    try:
        a1.destroy()
        a2.destroy()
        e1.destroy()
        e2.destroy()
        b1.destroy()
    except:
        pass
    button1=Button(frame, text='With Computer',command=vscomputer,font='Monaco 25 bold',bd=1,bg='white',width=15)
    button1.pack()
    button2=Button(frame, text='With Friend',font='Monaco 25 bold',width=15,bd=1,bg='white',command=vsplayer)
    button2.pack(pady=30)


def save(evt):
    global n
    img = ImageGrab.grab((root.winfo_rootx(), root.winfo_rooty(), root.winfo_rootx() + 500, root.winfo_rooty() + 550))
    img.save(f'screenshots/{ceil(time())}.jpg')


root=Tk()
root.title('Tic Tac Toe')
root.geometry('500x550')
root.iconbitmap('tic.ico')
back_image = PhotoImage(file="back.png")
resign = PhotoImage(file="resign1.png")
exit_image = PhotoImage(file="exit.png")
sound_play = PhotoImage(file="speakeron.png")
sound_mute = PhotoImage(file="speakeroff.png")
root.resizable(0,0)

PlaySound('ticsoundtrack.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)

im=PhotoImage(file='1.png')
bg=Label(root,image=im)
bg.place(x=0,y=0)

frame=Frame(root,bg='#FFFFFF')
frame.place(relx=0.5,rely=0.6,anchor=CENTER)


bm=Button(root,image=sound_play,command=mute,bd=0,bg='white')
bm.pack(side=BOTTOM,anchor=SE,padx=20,pady=20)
button1=Button(frame, text='New Game',command=choice,font='Monaco 25 bold',bd=1,bg='white',width=15)
button1.pack()
button2=Button(frame, text='Exit',font='Monaco 25 bold',width=15,bd=1,bg='white',command=exit_program)
button2.pack(pady=30)
button3=Button(frame,text='How To Play?',font='Monaco 25 bold',width=15,bd=1,bg='white',command=howtoplay)
button3.pack()

root.protocol("WM_DELETE_WINDOW", exit_program)
root.bind('<Button-3>',save)
root.config(cursor="plus red")

root.mainloop()
