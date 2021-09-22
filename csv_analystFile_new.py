# Analyst csv files
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as St
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import Menu
import os
from typing import Union, Any, Pattern

import pandas as pd
from pandas import Series, DataFrame
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader
from tkinter import messagebox as mb

import re


df = ()
content_col = []
lst2 = []
idx = 0
cnt_rows = 0
cnt_columns = 0
file_name = ""
sel_col = 0
headers = []
counter_OK = 0
reliability_data=0

# Create main window
myWin = tk.Tk()
myWin.geometry("650x750")
myWin.title("Analyst of .csv files")

myListBox = tk.Listbox(myWin, selectmode='browse')
myListBox.grid(row=5, column=0)

output_text = St(height=28, width=60)
output_text.grid(row=5, column=1, padx=10, pady=10, sticky="w")


# Create names of fields for output
label_00 = tk.Label(text=" Name of file:")
label_00.grid(row=1, column=0, padx=10, pady=10, sticky="e")

label_01 = tk.Label(text="")
label_01.grid(row=1, column=1, sticky="w")

# -------------------
label_10 = tk.Label(text=" Rows: ")
label_10.grid(row=2, column=0, padx=10, pady=10, sticky="e")

label_11 = tk.Label(text="")
label_11.grid(row=2, column=1, sticky="w")

label_20 = tk.Label(text=" Columns: ")
label_20.grid(row=3, column=0, padx=10, pady=10, sticky="e")

label_21 = tk.Label(text="")
label_21.grid(row=3, column=1, sticky="w")


label_ent = tk.Label(text="Enter pattern for searching")
label_ent.place(x=100, y=600, width=200, height=30)

ent_search = tk.Entry(width=50)
ent_search.place(x=300, y=600)

my_menu = Menu(myWin)
myWin.config(menu=my_menu)


def open_and_read_csv():
    global df
    global cnt_columns
    global cnt_rows
    global headers

    global file_name

    my_dir = os.getcwd()
    file_name = fd.askopenfilename(initialdir = my_dir)
    my_df = pd.read_csv(file_name, header=None, sep=';')
    df=my_df
    cnt_rows = my_df.shape[0]
    cnt_columns = my_df.shape[1]

    label_01['text'] = file_name
    label_11['text'] = cnt_rows
    label_21['text'] = cnt_columns

    row = my_df.iloc[0]

    for j in range(cnt_columns-1):
        myListBox.insert(tk.END,row[j])

    myListBox.bind('<<ListboxSelect>>', callback)

    return df, cnt_rows, cnt_columns, file_name

# menu file
filemenu = Menu(my_menu, tearoff=0)
filemenu.add_command(label="Open and read .csv file", command=open_and_read_csv)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=myWin.destroy)
my_menu.add_cascade(label="File", menu=filemenu)

searchmenu = Menu(my_menu, tearoff=0)
searchmenu.add_command(label="Criteria")
searchmenu.add_command(label="Picking")
searchmenu.add_separator()
my_menu.add_cascade(label="Searching", menu=searchmenu)
#getting content of column

def get_column(n_col):
    global df
    global sel_col
    global content_col
    n_col=sel_col
    kol_rows=df.shape[0]
    content_col.clear()
#    print(kol_rows)
    for i in range(kol_rows):
        content_col.append(df.iat[i,sel_col])
    return content_col

 # handle event
def callback(event):
    global sel_col
    global df
    global cnt_rows
    global content_col
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        sel_col=index

        # Create text field for general output
        if output_text.compare("end", "==", "1.0")==False:
            clearTextInput()

    get_column(sel_col)
    for item in content_col:
        output_text.insert(tk.END, str(item) + os.linesep)
    return sel_col



def check():
    global sel_col
    global content_col
    global counter_OK
    global cnt_rows
    my_shab: str=""
    counter_OK = 0
    reliability_data=0
    my_shab = ent_search.get()

    if len(my_shab) == 0:
         mb.showinfo(title=None, message="This field cannot be empty! ")
    else:
        print("shablon=", my_shab)
        #regex=re.compile(my_shab)
        for item in content_col:
            #if (regex.match(my_shab)):

            if str.__contains__(str(item), my_shab):
                counter_OK+=1
        countOK_label['text']= str(counter_OK)
        reliability_data= round(counter_OK/cnt_rows*100, 2)
        dostover_label['text']=str(reliability_data)+"%"
        print("counter_OK=",counter_OK, "  cnt_rows=",cnt_rows, "reliability_data=",reliability_data)
    return counter_OK

but_check = tk.Button(myWin, text="Check", command=check)
but_check.place(x=150,y=650,width=50,height=30)

countOK_label=tk.Label(text="")
countOK_label.place(x=200,y=650,width=50,height=30)

dostover_label=tk.Label(text="")
dostover_label.place(x=350,y=650,width=250,height=30)

dostover_name_label = tk.Label(text="Reliability of data")
dostover_name_label.place(x=250, y=650, width=200, height=30)

def clearTextInput():
    output_text.delete("1.0","end")




################################## finish of functions ###################################

# Cycle mainloop
myWin.mainloop()


'''
s1 = 'Testing string'
s2 = '1234,12345$'

regex = re.compile('[0-9,$]+$')

if ( regex.match(s1) ):
   print "s1 matched"
else:
   print "s1 didn't match"

if ( regex.match(s2) ):
   print "s2 matched"
else:
   print "s2 didn't match"
'''