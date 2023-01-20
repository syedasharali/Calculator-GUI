from PIL import Image, ImageGrab
from tkinter import *

root=Tk()
root.title('Tic Tac Toe')
root.iconbitmap('tic.ico')
root.geometry('500x500')
root.resizable(0,0)

x=0;y=0
count=0


def checkwin():
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
    zb_list=[]
    cb_list=[]

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
        canvas.create_line(250/3,250/3-65,250/3,250/3+400,width=8,fill='red')
    elif cb_list[3]==cb_list[4]==cb_list[5]==1:
        canvas.create_line(250/3+166.66,250/3-65,250/3+166.66,250/3+400,width=8,fill='red')
    elif cb_list[6]==cb_list[7]==cb_list[8]==1:
        canvas.create_line(250/3+2*166.66,250/3-65,250/3+2*166.66,250/3+400,width=8,fill='red')
    elif cb_list[0]==cb_list[3]==cb_list[6]==1:
        canvas.create_line(250/3-65,250/3,250/3+400,250/3,width=8,fill='red')
    elif cb_list[1]==cb_list[4]==cb_list[7]==1:
        canvas.create_line(250/3-65,250/3+166.66,250/3+400,250/3+166.66,width=8,fill='red')
    elif cb_list[2]==cb_list[5]==cb_list[8]==1:
        canvas.create_line(250/3-65,250/3+2*166.66,250/3+400,250/3+2*166.66,width=8,fill='red')
    elif cb_list[0]==cb_list[4]==cb_list[8]==1:
        canvas.create_line(40,40,460,460,width=8,fill='red')
    elif cb_list[6]==cb_list[4]==cb_list[2]==1:
        canvas.create_line(40,460,460,40,width=8,fill='red')
    
    
    elif zb_list[0]==zb_list[1]==zb_list[2]==1:
        canvas.create_line(250/3,250/3-65,250/3,250/3+400,width=8,fill='blue')
    elif zb_list[3]==zb_list[4]==zb_list[5]==1:
        canvas.create_line(250/3+166.66,250/3-65,250/3+166.66,250/3+400,width=8,fill='blue')
    elif zb_list[6]==zb_list[7]==zb_list[8]==1:
        canvas.create_line(250/3+2*166.66,250/3-65,250/3+2*166.66,250/3+400,width=8,fill='blue')
    
    elif zb_list[0]==zb_list[3]==zb_list[6]==1:
        canvas.create_line(250/3-65,250/3,250/3+400,250/3,width=8,fill='blue')
    elif zb_list[1]==zb_list[4]==zb_list[7]==1:
        canvas.create_line(250/3-65,250/3+166.66,250/3+400,250/3+166.66,width=8,fill='blue')
    elif zb_list[2]==zb_list[5]==zb_list[8]==1:
        canvas.create_line(250/3-65,250/3+2*166.66,250/3+400,250/3+2*166.66,width=8,fill='blue')
    elif zb_list[0]==zb_list[4]==zb_list[8]==1:
        canvas.create_line(40,40,460,460,width=8,fill='blue')
    elif zb_list[6]==zb_list[4]==zb_list[2]==1:
        canvas.create_line(40,460,460,40,width=8,fill='blue')
    else:
        return True
    
    

def zero():
    global count
    canvas.create_oval(33.33+x,33.33+y,133.33+x,133.33+y,outline='blue',width=5)
    count+=1
    
    
    
    
    
def cross():
    global count
    canvas.create_line(33.33+x,33.33+y,133.33+x,133.33+y,fill='red',width=5)
    canvas.create_line(133.33+x,33.33+y,33.33+x,133.33+y,fill='red',width=5)
    count+=1
    

    

def clicked(evt):
    global x, y, count
    if checkwin()==True:
        if 0<evt.x<166.66 and 0<evt.y<166.66:
            x=0;y=0
        if 0<evt.x<166.66 and 166.66<evt.y<333.33:
            x=0;y=166.66
        if 0<evt.x<166.66 and 166.66+166.66<evt.y<333.33+166.66:
            x=0;y=2*166.66
            
        if 166.66<evt.x<166.66+166.66 and 0<evt.y<166.66:
            x=166.66;y=0
        if 166.66<evt.x<166.66+166.66 and 166.66<evt.y<333.33:
            x=166.66;y=166.66
        if 166.66<evt.x<166.66+166.66 and 166.66+166.66<evt.y<333.33+166.66:
            x=166.66;y=2*166.66

        if 2*166.66<evt.x<3*166.66 and 0<evt.y<166.66:
            x=2*166.66;y=0
        if 2*166.66<evt.x<3*166.66 and 166.66<evt.y<333.33:
            x=2*166.66;y=166.66
        if 2*166.66<evt.x<3*166.66 and 166.66+166.66<evt.y<333.33+166.66:
            x=2*166.66;y=2*166.66
        
        img = ImageGrab.grab((canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + 600, canvas.winfo_rooty() + 600))
        if img.getpixel((x+80,y+100/3))!=(0,0,255) and img.getpixel((x+250/3,y+250/3))!=(255,0,0):
            if (count+2)%2==0:
                cross()
                canvas.update()
                checkwin()
            else:
                zero()
                canvas.update()
                checkwin()
     
canvas=Canvas(root,bg='white',height=500,width=500)

canvas.bind('<Button-1>',clicked)

canvas.pack()

canvas.create_line(500/3,0,500/3,500,width=10,fill='lime')
canvas.create_line(500-500/3,0,500-500/3,500,width=10,fill='lime')
canvas.create_line(0,500/3,500,500/3,width=10,fill='lime')
canvas.create_line(0,500-500/3,500,500-500/3,width=10,fill='lime')




root.mainloop()

