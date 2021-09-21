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

import re


df=()
content_col=[]
lst2=[]
idx=0
cnt_rows=0
cnt_columns=0
file_name=""
sel_col=0
headers=[]
#search_row #=tk.StringVar()
search_row=""
counter_OK=0



# Create main window
myWin = tk.Tk()
myWin.geometry("650x650")
myWin.title("Analyst of .csv files")
myListBox = tk.Listbox(myWin, selectmode='browse')
myListBox.grid(row=5, column=0)

output_text = St(height=28, width=60)
output_text.grid(row=5, column=1, padx=10, pady=10, sticky="w")

##############################   functions    #################################


# menu file
def open_and_read_csv():
    global df
    global cnt_columns
    global cnt_rows
    global headers

    my_dir = os.getcwd()
    my_file_name = fd.askopenfilename(initialdir = my_dir)
    label_01['text'] = my_file_name
    my_df=pd.read_csv(my_file_name, header=None,sep=';')
    df=my_df
    cnt_rows= my_df.shape[0]
    cnt_columns = df.shape[1]
    label_11['text'] = cnt_rows
    label_21['text'] = cnt_columns
    
    row = df.iloc[0] 
    #for i in range(cnt_rows):
     #   headers.append(df.iat[i, sel_col])

    for j in range(cnt_columns-1):
        #print(row[j])
        myListBox.insert(tk.END,row[j])   

    myListBox.bind('<<ListboxSelect>>', callback)




    return df, cnt_rows, cnt_columns

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
        if output_text.compare("end", "==", "1.0"):
            print("the widget is empty")
        else:
            print("the widget is fool, clean it")
            clearTextInput()
    # print("sel_col=", sel_col)
    get_column(sel_col)
    for item in content_col:
        output_text.insert(tk.END, str(item) + os.linesep)

    return sel_col


  
         



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




# Create listbox for choosing field  @@@@@@@@@@@@@@@@@@@

# Create menu $$$$$$$$$$$$$$$$$$$$$$$$$
menubar = Menu(myWin)
myWin.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Open and read .csv file", command=open_and_read_csv)

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

#output_text.grid(row=6, column=2, padx=10, pady=10, sticky="w")
#ButAny.pack

ent_label=tk.Label(text="Enter pattern for searching")
ent_label.grid(row=6, column=2,padx=10, pady=10, sticky="e")
ent_search = tk.Entry(myWin, textvariable=search_row)
ent_search.pack

def check():
    global sel_col
    global content_col
    global search_row
    global counter_OK

    counter_OK=0
    shablon=search_row
#    numCol=sel_col

    regex=re.compile(shablon)
    for item in content_col:
        if (regex.match(shablon) ):
            counter_OK+=1
    countOK_label['text']=counter_OK
    return counter_OK

but_Search=tk.Button(myWin,text="Check", command = check)
but_Search.grid(row=6, column=1, padx=10, pady=10, sticky="w")
but_Search.pack

countOK_label=tk.Label(text="")
countOK_label.grid(row=7, column=1,padx=10, pady=10, sticky="e")
countOK_label.pack
countOK_label
def clearTextInput():
    output_text.delete("1.0","end")



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