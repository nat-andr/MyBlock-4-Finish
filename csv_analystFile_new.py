# Analyst csv files
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import Menu #$$$$$$$$$$$$$$$
import os
import pandas as pd

df=[]
my_lst=[]
lst2=[]
idx=0
cnt_rows=0
cnt_columns=0
file_name=""

# Create main window
myWin=tk.Tk()
myWin.geometry("650x650")
myWin.title("Analyst of .csv files")
myListBox=tk.Listbox(myWin,selectmode='browse')
myListBox.grid(row=5,column=0)



##############################   functions    #################################


# menu file
def open_and_read_csv():
    my_dir=os.getcwd()
    file_name=fd.askopenfilename(initialdir=my_dir)
    label_01['text']=file_name
    df=pd.read_csv(file_name,header=None,sep=';')
    
    cnt_rows=df.shape[0]
    cnt_columns=df.shape[1]
    label_11['text']=cnt_rows
    label_21['text']=cnt_columns
    
    row = df.iloc[0] 
    print(row[0])

    #print(cols)
    
    for j in range(cnt_columns-1):
        print(row[j])
        myListBox.insert(tk.END,row[j])   

    onselect(myListBox.selection_set)
    myListBox.bind('<<ListboxSelect>>', clickEvent)     
    sel_col=idx
    lst=get_column(df,sel_col)
    for item in get_column(df,5):
        output_text.insert(tk.END, str(item)+os.linesep)

    return df,lst, file_name, cnt_rows, cnt_columns

#getting content of column
def get_column(df,num_col):
    cnt_rows=df.shape[0]
#    kol_rows=df.shape[0]
#    print(kol_rows)
    my_lst=[]
    for i in range(cnt_rows):
        my_lst.append(df.iat[i,num_col])
    return my_lst
'''
# handle click on Listbox

def clickEvent:
  #insert code that will execute here
    w = event.widget
    idx = int(w.curselection()[0])
    value = w.get(idx)
    print(value,idx) 
#lb = Listbox(main)

    myListBox.bind('<<ListboxSelect>>', clickEvent)
    return idx
'''
# handle event
def onselect(event):
    w = event.widget
    idx = int(w.curselection()[0])
    value = w.get(idx)
    print(value,idx)
    
    return idx



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


# Create listbox for choosing field  @@@@@@@@@@@@@@@@@@@

#get_headers(df)

#myListBox.bind('<<ListboxSelect>>', onselect)
'''
# button-click_message
def process_button():
    file_name=do_dialog()
    label_01['text']=file_name
    df=pandas_read_csv(file_name)
    lst=get_column(df,2)
    for item in lst:
        output_text.insert(tk.END, str(item)+os.linesep)
'''


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
#myBut=tk.Button(myWin,text="Read num column",command=colSelection)
#myBut.grid(row=4, column=1)



# Cycle mainloop
myWin.mainloop()
