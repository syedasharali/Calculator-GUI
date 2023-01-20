from PIL import Image, ImageGrab
from tkinter import *




x=0;y=0
count=0
cross_counter=0
zero_counter=0
flag=False

def validate_input(new_text):
    return len(new_text) <= 8

def draw():
    global flag
    flag=True

def cross_win():
    global cross_counter, zero_counter, count, flag
    flag=True
    cross_counter+=1
    if cb_list.count(1)==zb_list.count(1):
        count=count+1
    canvas.itemconfig(text1,text=f'{ent1.get()} = {cross_counter}')

def zero_win():
    global cross_counter, zero_counter, count,flag
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
        canvas.create_line(250/3+166.66,250/3-65,250/3+166.66,250/3+400,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[6]==cb_list[7]==cb_list[8]==1:
        canvas.create_line(250/3+2*166.66,250/3-65,250/3+2*166.66,250/3+400,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[0]==cb_list[3]==cb_list[6]==1:
        canvas.create_line(250/3-65,250/3,250/3+400,250/3,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[1]==cb_list[4]==cb_list[7]==1:
        canvas.create_line(250/3-65,250/3+166.66,250/3+400,250/3+166.66,width=8,fill='red',tag='line')
        cross_win()
    elif cb_list[2]==cb_list[5]==cb_list[8]==1:
        canvas.create_line(250/3-65,250/3+2*166.66,250/3+400,250/3+2*166.66,width=8,fill='red',tag='line')
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
        canvas.create_line(250/3+166.66,250/3-65,250/3+166.66,250/3+400,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[6]==zb_list[7]==zb_list[8]==1:
        canvas.create_line(250/3+2*166.66,250/3-65,250/3+2*166.66,250/3+400,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[0]==zb_list[3]==zb_list[6]==1:
        canvas.create_line(250/3-65,250/3,250/3+400,250/3,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[1]==zb_list[4]==zb_list[7]==1:
        canvas.create_line(250/3-65,250/3+166.66,250/3+400,250/3+166.66,width=8,fill='blue',tag='line')
        zero_win()
    elif zb_list[2]==zb_list[5]==zb_list[8]==1:
        canvas.create_line(250/3-65,250/3+2*166.66,250/3+400,250/3+2*166.66,width=8,fill='blue',tag='line')
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
    canvas.create_oval(33.33+x,33.33+y,133.33+x,133.33+y,outline='blue',width=8,tag='zero')
    count+=1
    
    
    
    
    
def cross():
    global count
    canvas.create_line(33.33+x,33.33+y,133.33+x,133.33+y,fill='red',width=8,tag='cross')
    canvas.create_line(133.33+x,33.33+y,33.33+x,133.33+y,fill='red',width=8,tag='cross')
    count+=1
    

    

def clicked(evt):
    global x, y, count,flag
    if flag==True:
        canvas.delete('cross')
        canvas.delete('zero')
        canvas.delete('line')
        flag=False
    elif checkwin()==True:
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
     
def canv():
    global root, canvas, text1,text2
    root.destroy()
    root=Tk()
    root.title('Tic Tac Toe')
    root.iconbitmap('tic.ico')
    root.geometry('500x550')
    root.resizable(0,0)
    canvas=Canvas(root,bg='white',height=550,width=500)
    canvas.bind('<Button-1>',clicked)
    canvas.pack()

    canvas.create_line(500/3,0,500/3,500,width=10,fill='lime')
    canvas.create_line(500-500/3,0,500-500/3,500,width=10,fill='lime')
    canvas.create_line(0,500/3,500,500/3,width=10,fill='lime')
    canvas.create_line(0,500-500/3,500,500-500/3,width=10,fill='lime')
    text1=canvas.create_text(138,522,text=f'{ent1.get()} = {cross_counter}',font='Ariel 20',fill='red')
    text2=canvas.create_text(360,522,text=f'{ent2.get()} = {zero_counter}',font='Ariel 20',fill='blue')
    root.mainloop()


root=Tk()
root.title('Tic Tac Toe')
root.iconbitmap('tic.ico')
ent1=StringVar()
ent2=StringVar()
Label(root,text='Player1 (X):   ',font='Comicsansms 20 bold',fg='red').grid(row=0,column=0,pady=5)
e1=Entry(root,textvariable=ent1,font='Ariel 15',validate="key", validatecommand=(root.register(validate_input), "%P"))
e1.grid(row=0,column=1,columnspan=2,pady=5,ipady=2,ipadx=2)
Label(root,text='Player2 (O):   ',font='Comicsansms 20 bold',fg='blue').grid(row=1,column=0,pady=5)
Entry(root,textvariable=ent2,font='Ariel 15',validate="key", validatecommand=(root.register(validate_input), "%P")).grid(row=1,column=1,columnspan=2,pady=5,ipady=2,ipadx=2,padx=2)
b1=Button(root, text='Play',command=canv,font='Ariel 15',width=15)
b1.grid(row=2,column=2,columnspan=2,padx=2,pady=2)
root.bind('<Return>', lambda event: b1.invoke())
e1.focus_set()

root.mainloop()
