# Analyst csv files

import tkinter as tk
from tkinter.scrolledtext import ScrolledText as St
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import Menu
from tkinter import Canvas, BOTH
from tkinter import Frame
import os
from typing import Union, Any, Pattern

import pandas as pd
from pandas import Series, DataFrame
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader
from tkinter import messagebox as mb
from tkinter import ttk
import re



#желтый
foregroundColor = "#FFFACD"
#коричневыq
backgroundColor = "#800000"
font="Times New Roman, 12"

df = ()
content_col = []
content=[]
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
#myWin.configure(background="#555")
myWin.resizable(False,True)
myWin.geometry("600x535")
myWin.title("Analyse of .csv files")
myWin["bg"]=foregroundColor






# Create names of fields for output
label_00=tk.Label(text=" Name of file:",bg=foregroundColor)
label_00.grid(row=1, column=0,padx=10, pady=10, sticky="e")

label_01=tk.Label(text="",bg=foregroundColor)
label_01.grid(row=1, column=1, sticky="w")
#-------------------
label_10=tk.Label(text=" Rows: ",bg=foregroundColor)
label_10.grid(row=2, column=0, padx=10, pady=10, sticky="e")

label_11=tk.Label(text="",bg=foregroundColor)
label_11.grid(row=2, column=1, sticky="w")
#-------------------
label_20=tk.Label(text=" Columns: ",bg=foregroundColor)
label_20.grid(row=3, column=0, padx=10, pady=10, sticky="e")

label_21=tk.Label(text="",bg=foregroundColor)
label_21.grid(row=3, column=1, sticky="w")
#myWin["titlebg"]="#800000"


myCanvas = Canvas(myWin)



myListBox = tk.Listbox(myWin, selectmode='browse')
#myListBox.grid(row=5, column=0)
myListBox.place(x=50, y=190, width=160, height=310)

output_text = St(height=28, width=60)
#output_text.place(row=5, column=1, padx=10, pady=10, sticky="w")
output_text.place(x=250, y=125, width=310, height=375)





entry_shablon = tk.Entry(width=25)
entry_shablon.place(x=35, y=562)
entry_shablon.insert(0,"")


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
    
    label_Click = tk.Label(text="Кликните по строке",bg=foregroundColor, fg="red")
    label_Click.place(x=50, y=170, width=160, height=20)
   
    return df, cnt_rows, cnt_columns, file_name

def resize():
    #myWin.geometry("")
    myWin.geometry("600x700")

# menu file
filemenu = Menu(my_menu,  tearoff=0)
filemenu.add_command(label="Open and read .csv file", command=open_and_read_csv, background="#800000",foreground="#FFFACD")

filemenu.add_separator()
filemenu.add_command(label='Exit', command=myWin.destroy, background="#800000",foreground="#FFFACD")
my_menu.add_cascade(label="File", menu=filemenu)


searchmenu = Menu(my_menu, tearoff=0)
searchmenu.add_command(label="Searching", command=resize, background="#800000",foreground="#FFFACD")

my_menu.add_cascade(label="Searching", menu=searchmenu)



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
        content=content_col
    return content
 # handle event
def callback(event):
    global sel_col
    global df
    global cnt_rows
    global content
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

countOK_label=tk.Label(text="",bg=foregroundColor)
countOK_label.place(x=100,y=660,width=50,height=13)

countOK_name_label=tk.Label(text="Найдено записей",bg=foregroundColor)
countOK_name_label.place(x=50,y=640,width=150,height=13)

dostover_label=tk.Label(text="",bg=foregroundColor)
dostover_label.place(x=350,y=660,width=40,height=13)

dostover_name_label = tk.Label(text="Доля записей, соответствующих шаблону",bg=foregroundColor)
dostover_name_label.place(x=250, y=640, width=300, height=13)

def check():
    global sel_col
    global content_col
    global counter_OK
    global cnt_rows
    global valChoice
    global content

    print("cnt_rows from start=",cnt_rows)
    my_shab: str=""
    counter_OK = 0
    reliability_data=0
    n_records=0
    my_shab = entry_shablon.get()

    if len(my_shab) == 0:
         mb.showinfo(title=None, message="")
    else:
        print("shablon=", my_shab)
        #regex=re.compile(my_shab)
        if valChoice==1:
            n_records = cnt_rows
            content=content_col
            for i in range(cnt_rows):
                content.append(df.iat[i, 1])
        else:
            n_records = cnt_rows * cnt_columns
            for i in range(cnt_columns-1):
                for j in range(cnt_rows):
                    content.append(df.iat[i,j])

        print("after vybor n_records=", n_records)
        for item in content:
            if str.__contains__(str(item), my_shab):
                counter_OK += 1

    countOK_label['text']= str(counter_OK)
    reliability_data= round((counter_OK/n_records)*100, 2)
    dostover_label['text']=str(reliability_data)+"%"
    print("  counter_OK=",counter_OK, "  cnt_rows=",cnt_rows, "reliability_data=",reliability_data)
    return counter_OK


but_check = tk.Button(myWin, text="Найти", command=check,background="#800000",foreground="#FFFACD", relief="raised")
but_check.place(x=420,y=562,width=108,height=30)







label_line1=tk.Label(text=".",bg='black')
label_line1.place(x=0,y=537,width=600,height=3)

label_line2=tk.Label(text=".",bg='black')
label_line2.place(x=0,y=608,width=600,height=3)

valChoice = tk.IntVar()
valChoice.set(1)

choices=[("Поиск по одному столбцу",1), ("Поиск по всему файлу",2)]
def ShowChoice():
    print(valChoice.get())

for choice, val in choices:
    tk.Radiobutton(myWin,
                   text=choice,
                   variable=valChoice,
                   command=ShowChoice,
                   value=val, bg=foregroundColor).place(x=200,y=520+val*20)


#Label(frame, text='Color-Demo').pack()

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