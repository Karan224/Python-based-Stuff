

import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#creating a global dataframe
data = pd.read_csv("data.csv",encoding = 'latin1',sep = '\t')
#getting data start
def get_data():
    inpt = entry_field.get()
    selection = var.get()
    print(type(inpt))#only  for testing purpose
    print(selection)#only  for testing purpose
    display(inpt,selection)

def display(inpt,selection):
    #display window start
    rt = Tk()#creating root window for search results
    result = data[data[selection].astype('str')==inpt]#retrieving data from dataframe
    print(len(result))#only for testing purpose
    if(len(result)>0):
        result_li = result.values.tolist()
        print(result_li)#only for  testing purpose
        columns_li = data.columns.values#listing column names
        heading_lbl = Label(rt,text = "\t\t".join(columns_li))#heading display label
        heading_lbl.pack(side = TOP)
        #result display start
        
        
        #general student information start
        rs_li_str = [str(i) for i in result_li[0]]
        print(rs_li_str)#only for testing purpose
        result_lbl = Label(rt, text = "\t\t".join(rs_li_str))
        result_lbl.pack(side = TOP)
        #general student information end
        
        #starting numpy work
        
        #displaying rank of c
        c = np.array(data["C"])
        c = np.sort(c)
        print(c)#only for testing purpose
        a = result["C"].values
        print(c[::-1])#only for  testing purpose 
        c_rnk = len(c) - np.searchsorted(c,a) + 1#calculating rank in c
        print(a)#only for testing purpose
        txt = "Rank in C : "+str(c_rnk)
        c_lbl = Label(rt,text = txt)
        c_lbl.pack(side =TOP)
        
        #displaying rank in c++
        cpp = np.array(data["C++"])
        cpp = np.sort(cpp)
        a = result["C++"].values
        cpp_rnk = len(cpp)-np.searchsorted(cpp,a)
        print(a)#only for testing purpose
        cpp_lbl = Label(rt,text = "Rank in C++ : "+str(cpp_rnk))
        cpp_lbl.pack(side =TOP)
        
        #displaying rank in python
        python = np.array(data["Python"])
        python = np.sort(python)
        a = result["Python"].values
        py_rnk = len(python)-np.searchsorted(python,a)
        print(np.searchsorted(python,a))#only for testing purpose
        py_lbl = Label(rt,text = "Rank in Python : "+str(py_rnk))
        py_lbl.pack(side =TOP)
        
        #displaying rank java
        java = np.array(data["Java"])
        java = np.sort(java)
        a = result["Java"].values
        java_rnk = len(java)-np.searchsorted(java,a)
        print(np.searchsorted(java,a))#only for testing purpose
        java_lbl = Label(rt,text = "Rank in Java : "+str(java_rnk))
        java_lbl.pack(side =TOP)
        
        #displaying rank in cst
        cst = np.array(data["CST"])
        cst = np.array(cst)
        a = result["CST"].values
        cst_rnk = len(cst)-np.searchsorted(cst,a)
        print(np.searchsorted(cst,a))#only for testing purpose
        cst_lbl = Label(rt,text = "Rank in CST : "+str(cst_rnk)) +1
        cst_lbl.pack(side =TOP)
        
        #displaying rank in ds
        ds = np.array(data["Data Structures"])
        ds = np.sort(ds)
        a = result["Data Structures"].values
        ds_rnk = len(ds)-np.searchsorted(ds,a) 
        print(np.searchsorted(cst,a))#only for testing purpose
        ds_lbl = Label(rt,text = "Rank in Data  Structures : "+str(ds_rnk))
        ds_lbl.pack(side =TOP)
        
        #ending numpy work
        
        #result display end
    else:#this condition works when there is no match
        no_result_found = Label(rt, text= "NO RESULT FOUND")
        no_result_found.pack(side = TOP)
        
        
    
    


def graph_work():
    select = var1.get()
    select2 = var2.get()
    print(select)  #for checking
    print(select2) #for checking
    win = Tk()
    
    #bar graph
    figure = plt.Figure(figsize=(9,8), dpi=100)
    ax2 = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, win)
    chart_type.get_tk_widget().pack(side=LEFT, fill=BOTH)
    data.plot(kind='bar', legend=True, ax=ax2, x= select , y = select2)

    win.mainloop()






#create root object
root = Tk()
#search data start
top_frame = Frame(root)
top_frame.pack(side = TOP)
#column name dropdown for selection start
columns_li = data.columns.values#listing column names
columns_tple = (columns_li[0],columns_li[1])
var = StringVar(top_frame)#conveting tple to usable form for dropdown
var.set(columns_tple[0])
columns_menu = OptionMenu(top_frame,var,*columns_tple)#creating option menu
columns_menu.pack(side = LEFT)
#column name dropdown end

#graphing work start
mid_frame = Frame(root)#creating mid frame for ploting of graph
mid_frame.pack(side = TOP)
#dimension menu
columns_li = data.columns.values
columns_tple = (columns_li[0],columns_li[1])
var1 = StringVar(top_frame)#converting tple to usable form for dropdown
var1.set(columns_tple[0])
columns_menu = OptionMenu(mid_frame,var1,*columns_tple)#creating option menu
columns_menu.pack(side = LEFT)

#measures menu
columns_li = data.columns.values
columns_tple = (columns_li[2],columns_li[3],columns_li[4],columns_li[5],columns_li[6],columns_li[7])

var2 = StringVar(top_frame)#converting tple to usable form for dropdown
var2.set(columns_tple[0])
columns_menu = OptionMenu(mid_frame,var2,*columns_tple)#creating option menu
columns_menu.pack(side = LEFT)

#graph Button start
graph_button = Button(mid_frame , text = "Plot Graph",command = graph_work,fg = 'white',bg = 'black', relief = RAISED)
graph_button.pack(side = LEFT)
#graph button end


#graphing work end
#input field start
entry_field = Entry(top_frame)#creating input field for search using Entry widget
entry_field.pack(side =  LEFT)
#input field end

#search  button start
search_button =  Button(top_frame , text = "SEARCH", command = get_data,fg = 'white',bg = 'black', relief = RAISED)
search_button.pack(side = LEFT)
#search  button end


#search data over


#data dispay start 
bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)
bottom_frame.pack()
df_list = data.values.tolist()
heading_lbl = Label(bottom_frame,text = "\t\t".join(columns_li))
heading_lbl.pack(side = TOP)
for df in df_list:
    li = [str(i) for i in df]
    lbl = Label(bottom_frame,text = "\t\t".join(li))
    lbl.pack()
root.mainloop()
