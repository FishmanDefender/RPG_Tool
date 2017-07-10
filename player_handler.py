'''
Created on July 6, 2017

@author : Michael
'''
#!/usr/bin/env python
import tkinter as tk
import os
from tkinter.font import Font

root = tk.Tk()
home_path = os.getcwd()
os.chdir(home_path+'\images')
photo = tk.PhotoImage(file = 'knight.gif')
os.chdir(home_path)
'''
This program has two global variables:
home_path: This is the path to the location of RPG_Tool.py
photo: This is the logo photo 'knight.gif' that is used as the logo for all windows
'''
menu_font = Font(family = 'Segoe UI', size = 9)
'''
This sets the fonts used in the application as global variables.
'''

class AddChar(tk.Frame):
	'''
	This is the class that builds the new top-level window for the character addition wondow
	'''

	def __init__(self,parent=root):
		'''
		The constructor for the player window
		'''
		tk.Frame.__init__(self,parent)

		top = self.winfo_toplevel()
		top.columnconfigure(0, weight=1)
		top.rowconfigure(0, weight=1)

		self.grid(sticky=tk.N+tk.E+tk.S+tk.W)
		self.rowconfigure(1,weight=1)
		self.columnconfigure(1, weight=1)

	def run():

		app = AddChar(root)
		app.master.title('RPG Assistant')
		app.master.geometry('400x400+100+100')
		app.master.tk.call('wm','iconphoto',app.master._w,photo)

		app.mainloop()

	if __name__ == '__main__':
		main()