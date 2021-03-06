# Analyst csv files
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import pandas as pd

# Create main window
myWin=tk.Tk()
myWin.geometry("650x650")
myWin.title("Analyst of .csv files")

# Create names of fields output
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

# reading csv
def pandas_read_csv(file_name):
        df=pd.read_csv(file_name,header=None,sep=';')
        cnt_rows=df.shape[0]
        cnt_columns=df.shape[1]
        label_11['text']=cnt_rows
        label_21['text']=cnt_columns
        return df

#getting content of column
def get_column(df,column_ix):
    cnt_rows=df.shape[0]
    lst=[]
    for i in range(cnt_rows):
        lst.append(df.iat[i,column_ix])
    return lst

# button-click_message
def process_button():
    file_name=do_dialog()
    label_01['text']=file_name
    df=pandas_read_csv(file_name)
    lst=get_column(df,2)
    for item in lst:
        output_text.insert(tk.END, str(item)+os.linesep)
    mb.showinfo(title=None, message="Ready!")

# openning file dialog
def do_dialog():
    my_dir=os.getcwd()
    name=fd.askopenfilename(initialdir=my_dir)
    return name
    
# Create button
myBut=tk.Button(myWin,text="Read file",command=process_button)
myBut.grid(row=6, column=1)



# Cycle mainloop
myWin.mainloop()
