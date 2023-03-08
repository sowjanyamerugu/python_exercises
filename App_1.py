# Import Module
from tkinter import *
import pandas as pd
df = pd.read_csv("C:\\Sowjanya\\Python\\Automobile_data.csv")
#print("First 30 from the list")
#print(df.head(30))

# create root window
root = Tk()
 
# root window title and dimension
root.title("Welcome to Automobiles")
# Set geometry (widthxheight)
root.geometry('900x500')

#adding a label to the root window
lbl = Label(root, text ="honda cars list")
lbl .grid(column =2, row =2)

#adding a label to the root window
lbl = Label(root, text ="toyota cars list")
lbl .grid(column =7, row =5)


#adding Entry Field
#txt = Entry(root, width=60)
#txt.grid(column =8, row =8)

#function to display text when
#button is clicked
def clicked1():
    car_manufactures =df.groupby('company')
    res =car_manufactures.get_group('honda')
    lbl.grid(column =10, row =12)
    lbl.configure(text =res)


#function to display text when
#button is clicked
def clicked2():
    car_manufactures =df.groupby('company')
    res =car_manufactures.get_group('toyota')
    lbl.grid(column =20, row =15)
    lbl.configure(text =res)

 
# Create a Button
btn1 = Button(root, text = 'Click me !', bd = '5',
                          command =clicked1)
# set Button grid
btn1.grid(column=2,row =4)
#button widget with red colour text
# inside

# Create a Button
btn2 = Button(root, text = 'Click me !', bd = '7',
                          command = clicked2)


# set Button grid
btn2.grid(column=7,row =6)
#button widget with blue colour text
# inside

#all widgets will be here
# Execute Thinker
root.mainloop()
