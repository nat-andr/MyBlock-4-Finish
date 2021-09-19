# Analyst csv files
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import Menu #$$$$$$$$$$$$$$$
import os
import pandas as pd

# Create main window
myWin=tk.Tk()
myWin.geometry("650x650")
myWin.title("Analyst of .csv files")

# Create listbox for choosing field  @@@@@@@@@@@@@@@@@@@
myListBox=tk.Listbox(myWin,selectmode='browse')
myListBox.grid(row=5,column=0)

##############################   functions    #################################
# openning file dialog
def do_dialog():
    my_dir=os.getcwd()
    name=fd.askopenfilename(initialdir=my_dir)
    return name

# reading csv
def pandas_read_csv(file_name):
        df=pd.read_csv(file_name,header=None,sep=';')
        cnt_rows=df.shape[0]
        cnt_columns=df.shape[1]
        label_11['text']=cnt_rows
        label_21['text']=cnt_columns
        return df


# menu file
def open_csv_file():
    file_name=do_dialog()
    label_01['text']=file_name
    df=pandas_read_csv(file_name)
 #   
    lst2=df.shape[1]
    for j in range(df.shape[0]):
        myListBox.insert(tk.END,lst2[j])
    return lst2


# handle event
def onselect(event):
    w = event.widget
    idx = int(w.curselection()[0])
    value = w.get(idx)
    print(value)


myListBox.bind('<<ListboxSelect>>', onselect)


# openning file dialog
def do_dialog():
    my_dir=os.getcwd()
    name=fd.askopenfilename(initialdir=my_dir)
    return name

#getting content of column
def get_column(df,column_ix):
    cnt_rows=df.shape[0]
    lst=[]
    for i in range(cnt_rows):
        lst.append(df.iat[i,column_ix])
    return lst

# getting num of columns
def colSelection():
    selection=MyListBox.curselection()
    print(selection)
    num_selection=MyListBox[0]

################################## finish of functions ###################################




# Create names of fields for output
label_00=tk.Label(text=" Name of file:")
label_00.grid(row=1, column=0,padx=10, pady=10, sticky="e")

label_01=tk.Label(text="")
label_01.grid(row=1, column=1, sticky="w")
#-------------------
label_10=tk.Label(text=" Rows: ")
label_10.grid(row=2, column=0, padx=10, pady=10, sticky="e")

label_11=tk.Label(text="")
label_11.grid(row=2, column=1, sticky="w")
#-------------------
label_20=tk.Label(text=" Columns: ")
label_20.grid(row=3, column=0, padx=10, pady=10, sticky="e")

label_21=tk.Label(text="")
label_21.grid(row=3, column=1, sticky="w")

# Create text field for general output
output_text=st(height=28,width=60)
output_text.grid(row=5, column=1,padx=10, pady=10, sticky="w")
'''
# Create listbox for choosing field  @@@@@@@@@@@@@@@@@@@
myListBox=tk.Listbox(myWin,selectmode="single")
myListBox.grid(row=5,column=0)
'''


# Create menu $$$$$$$$$$$$$$$$$$$$$$$$$
menubar = Menu(myWin)
myWin.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)

filemenu.add_command(label="Find file", command=open_csv_file)
#filemenu.add_command(label="Read file", command=do_something)
filemenu.add_command(label='Exit', command=myWin.destroy)
filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu)
 
searchmenu = Menu(menubar, tearoff=0) 
searchmenu.add_command(label="Criteria") 
searchmenu.add_command(label="Picking")
searchmenu.add_separator()
menubar.add_cascade(label="Searching", menu=searchmenu) 


  
# Create button
#myBut=tk.Button(myWin,text="Read num column",command=colSelection)
#myBut.grid(row=4, column=1)



# Cycle mainloop
myWin.mainloop()
