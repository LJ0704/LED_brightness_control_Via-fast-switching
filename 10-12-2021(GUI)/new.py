from tkinter import *
import time
import serial
root=Tk()
root.title('Internal Lights') #makes the title of the window
root.geometry("500x300")       # size of the GUI
#arduino = serial.Serial(port='COM8', baudrate=115200, timeout=1) # establishing serial interface
#def write_read(x):  #read function 
        
        #arduino.write(bytes(str(x), 'utf-8')) #writes to arduino
        #time.sleep(0.01)
        #print(arduino.readline()) 
#
#
global  is_on  # keeping is_on state global(on or off)
global mode_on  # keeping mode_on state global(day or night mode)
global cur #CURSOR POSITION
cur = 50  #default mode=day + 50 % light intensity



def flood_plus():#flood light fun increasing 
    global cur   
    cur = cur + 25 #increment by 25 if clicked + sign
    flood.set(cur) #sets the flood light to (current value+25)
    if(cur>100): #if cur value is 100 keep default value as 100
        cur = 100
    print(cur) # printing current value of cur
   # write_read(cur) #sending current value to arduino


def flood_minus():# same as flood_add but decreases the value
    global cur
    cur = cur - 25
    flood.set(cur)
    if(cur<0):
        cur=0
    print(cur)
   # write_read(cur)
    

def hide_widget(widget): #hides a widget usually in off state
    widget.grid_forget()

def show_widget(widget,r,col,pad):#shows the widget usually in ON state
    widget.grid(row=r,column=col,pady=pad)

flood = Scale(root, from_=0, to=100, orient=VERTICAL)#track bar
flood.set(cur)#setting current value

mode_label = Label(root,text="Mode") #day or night mode
flood_label = Label(root, text="Flood Light") #flood light displays
#back_label = Label(root, text="Back Light")
nthng = Label(root, text="            ")




is_on = True # setting default on 
mode_on = True#setting default day mode

my_label = Label(root, text="DEFAULT LED ON", fg="green") #label for the on text
my_label.grid(row=0, column=1, pady=20)

def switch():
    global is_on 
    global cur
    # determine if on/off
    if is_on:#if its on the next step is on and vice-versa
        on_button.config(image=off)
        my_label.config(text="OFF", fg="grey")
        is_on=False#making the next step off
        cur = 0#sets the trackbar value to 0
        flood.set(0)
        print(cur)
        write_read(cur)
        hide_widget(flood)#if off state hide flood
        hide_widget(flood_label)
        hide_widget(flood_decrease)
        hide_widget(flood_increase)
        hide_widget(mode_label)
        hide_widget(mode_button)


    else:
        on_button.config(image=on)
        my_label.config(text="ON", fg="green")
        is_on= True
        cur = 50
        flood.set(50)
        print(cur)
       # write_read(cur)
        show_widget(flood,5,1,10)
        show_widget(flood_label,4,1,5)
        show_widget(flood_increase,5,2,10)
        show_widget(flood_decrease,5,0,10)
        show_widget(mode_label,2,1,5)
        show_widget(mode_button,3,1,10)


def mode():
    global mode_on
    global cur
    # determine if day/night mode
    if mode_on: #day mode to night
        mode_button.config(image=dark)
        my_label.config(text="NIGHT MODE", fg="grey")
        mode_on=False
        flood.set(50)
        cur = 50
        print(cur)
        #write_read(cur)
        flood_increase.config(state=NORMAL)
        flood_decrease.config(state=NORMAL)


    else:
        mode_button.config(image=light)
        my_label.config(text="DAY MODE", fg="green")
        mode_on= True
        flood.set(50)
        cur = 50
        print(cur)
       # write_read(cur)
       # print(arduino.readline())
        flood_increase.config(state=DISABLED)
        flood_decrease.config(state=DISABLED)


on = PhotoImage(file="on.png")
off= PhotoImage(file="off.png")
dark = PhotoImage(file="toggle_dark.png")
light = PhotoImage(file="toggle_light.png")
plus = PhotoImage(file="plus.png")
minus = PhotoImage(file="minus.png")

on_button = Button(root, image=on, bd=0, command=switch)
on_button.grid(row=1,column=1,pady=10)

mode_label.grid(row=2,column=1,pady=5)

mode_button = Button(root, image=light,height=20,width=20,command=mode)
mode_button.grid(row=3,column=1,pady=10)

flood_label.grid(row=4,column=1,pady=5)

flood_decrease = Button(root,image=minus,height=30,width=30,state=DISABLED,command=flood_minus)
flood_decrease.grid(row=5,column=0,pady=10)

flood.grid(row=5,column=1)

flood_increase = Button(root,image=plus,height=30,width=30,state=DISABLED,command=flood_plus)
flood_increase.grid(row=5,column=2,pady=10)

print(cur)
#write_read(cur)
#print(arduino.readline())
#back_label.grid(row=6,column=1,pady=5)

#back_decrease = Button(root,image=minus,height=30,width=30)
#back_decrease.grid(row=10,column=0,pady=10)

#back_increase = Button(root,image=plus,height=30,width=30)
#back_increase.grid(row=10,column=2,pady=10)

root.mainloop()
