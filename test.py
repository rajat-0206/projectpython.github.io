# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 22:41:33 2019

@author: pc
"""

from tkinter import * 
import tkinter as tk
  
# creating tkinter window 
root = tk.Tk() 
photo= PhotoImage(file=r"arrow.png")
bt=Button(root,image=photo,height=50,width=50)
bt.pack()

mainloop()