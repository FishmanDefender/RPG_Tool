'''
Created on June 28, 2017

@author: Michael
'''
#!/usr/bin/env python
import tkinter as tk
import os
from tkinter.font import Font

'''
PRIMARY BRANCH

This is the primary branch of the RPG Tool.
'''

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

class AddChar(tk.Toplevel):
	'''
	Builds the new top-level window for the character addition window
	'''

	def __init__(self,parent):
		'''
		The constructor for the player window. It runs as a child of whatever is passed as the parent.
		'''

		#Inherets from tk.Toplevel
		tk.Toplevel.__init__(self,parent)

		#defining the 'top'
		top = self.winfo_toplevel()
		top.columnconfigure(0, weight=1)
		top.rowconfigure(0, weight=1)

		'''
		The following shouldn't be getting an "unexpected argument" error on 'grid' command.
		'''
		#self.grid(sticky=tk.N+tk.E+tk.S+tk.W)
		#self.rowconfigure(1,weight=1)
		#self.columnconfigure(1,weight=1)

		#Setting 'top' characteristics
		self.title('Add Character')
		self.geometry('250x200+600+200')
		self.tk.call('wm','iconphoto',self._w,photo)

		self.transient()
		self.lift(aboveThis=parent)
		self.focus()

		#Building the new Frame object
		self.top_frame = tk.Frame(self)

		#Defining frame characteristics
		self.top_frame.grid(sticky=tk.N+tk.E+tk.S+tk.W)
		self.top_frame.rowconfigure(4,weight=1)
		self.top_frame.columnconfigure(4,weight=1)

		#Adding labels and Entries
		self.name = tk.Label(self.top_frame,text='Name')
		self.type = tk.Label(self.top_frame,text='Type')
		self.focus = tk.Label(self.top_frame,text='Focus')

		self.entry_name = tk.Entry(self.top_frame)
		self.entry_type = tk.Entry(self.top_frame)
		self.entry_focus = tk.Entry(self.top_frame)

		self.button = tk.Button(self.top_frame,text='Add Character',command=None)		

		self.name.grid(row=0,column=0,padx=5,pady=5)
		self.type.grid(row=1,column=0,padx=5,pady=5)
		self.focus.grid(row=2,column=0,padx=5,pady=5)

		self.entry_name.grid(row=0,column=1,padx=5,pady=5)
		self.entry_type.grid(row=1,column=1,padx=5,pady=5)
		self.entry_focus.grid(row=2,column=1,padx=5,pady=5)

		self.button.grid(row=3,column=0,columnspan=2,padx=5,pady=5)			

class Canvas(tk.Canvas):
	'''
	This class creates a canvas object.
	'''

	def __init__(self,parent,r0,c0):
		'''
		Constructor initiates the canvas. The parent must be a frame or a method that inherits from the frame class
		'''

		#Setting the canvas properties
		self.can = tk.Canvas(parent, bg = '#fff', bd=2, relief='groove')
		self.can.grid(row=r0, column=c0, rowspan=5, columnspan=5, sticky=tk.N+tk.S+tk.E+tk.W, pady=5, padx=5)
		self.can.columnconfigure(1,weight=1)
		self.can.rowconfigure(1, weight=1)


class MainMenu(tk.Menu):
	'''
	This creates a menu in the top level window, which must be passed as 'parent'.
	'''

	'''
	TODO:
		- All commands need a command function!
		- Can a grid with right-aligned shortcuts in column 2 be used as menu command labels?
	'''

	def __init__(self,parent):
		'''
		Constructor for the menu. It sets the element 'menuBar' of the parent frame to be a Menu widget.
		'''
		#Setting the Menu as a top level menu
		top = parent.winfo_toplevel()
		parent.menuBar = tk.Menu(top, font = menu_font)
		top['menu'] = parent.menuBar

		#Creating the 'File' submenu
		parent.file = tk.Menu(parent.menuBar, tearoff=0, font = menu_font)
		parent.file.add_command(label='New Campaign', command=None)
		parent.file.add_command(label='Open Campaign...', command=None)
		parent.file.add_command(label='Save Campaign', command=None)
		parent.file.add_command(label='Save Campaign as...', command=None)
		parent.file.add_separator()
		parent.file.add_command(label='Exit', command=top.destroy)

		#Creating the 'Edit' submenu
		parent.edit = tk.Menu(parent.menuBar, tearoff=0, font=menu_font)
		parent.edit.add_command(label='Undo', command=None)
		parent.edit.add_command(label='Redo', command=None)

		#Creating the 'Campaign' submenu
		parent.campaign = tk.Menu(parent.menuBar, tearoff=0, font=menu_font)
		parent.campaign.add_command(label='Edit Character...', command= lambda : EditChar(parent))#The command is a lambda so I can pass the 'Application' class as the parent.
		parent.campaign.add_command(label='Add Character...', command= lambda : AddChar(parent)) #The command here is a Lambda function so the AddChar isn't called at the startup of the script.
		#Could also use 'command = AddChar' without parenths.
		parent.campaign.add_command(label='Remove Character', command=None)
		parent.campaign.add_separator()
		parent.campaign.add_command(label='Export Character...', command=None)
		parent.campaign.add_command(label='Import Character...', command=None)

		#Creating the 'Test' submenu
		parent.test = tk.Menu(parent.menuBar, tearoff=0, font=menu_font)
		'''
		Put all toplevel windows here to test them.
		'''

		#Adding all submenus to the toplevel menu as cascades
		parent.menuBar.add_cascade(label='File', menu=parent.file)
		parent.menuBar.add_cascade(label='Edit', menu=parent.edit)
		parent.menuBar.add_cascade(label='Campaign', menu=parent.campaign)

		'''
		FUTURE:
			- Multi-System Support? Can this be built into the design without needing a whole new Charaacter Creation page?
		'''

class InfoColumn(tk.Frame):
	'''
	The infocolumn displays all of the relevent information regarding the selected character.
	'''

	def __init__(self,parent,r0,c0):
		'''
		The infocolumn is created within a parent frame class.
		'''

		#Declaring the frame bit
		info = tk.Frame(parent)
		info.grid(row=r0, column=c0, sticky=tk.N+tk.E+tk.S+tk.W, padx=5, pady=5)

		#Creating all of the labels
		self.char_name = tk.Label(info, text='Name')
		self.char_type = tk.Label(info, text='Type')
		self.char_focus = tk.Label(info, text='Focus')

		self.char_name.grid(row=0,column=0,padx=5,pady=5)
		self.char_type.grid(row=1,column=0,padx=5,pady=5)
		self.char_focus.grid(row=2,column=0,padx=5,pady=5)

		#Creating all of the entry widgets
		self.entry_name = tk.Entry(info,state='disabled')
		self.entry_type = tk.Entry(info,state='disabled')
		self.entry_focus = tk.Entry(info,state='disabled')

		self.entry_name.grid(row=0,column=1,padx=5,pady=5)
		self.entry_type.grid(row=1,column=1,padx=5,pady=5)
		self.entry_focus.grid(row=2,column=1,padx=5,pady=5)

		#Creating the test panel
		text = tk.Text(info, state=tk.DISABLED, height=15,width=22)

		text.grid(row=3,column=0,rowspan=2,columnspan=2,padx=5,pady=5)

	def set_activity(self,input):
		'''
		Sets the activity of the entry widgets in the infocolumn
		'''
		if input == 'active':
			self.entry_name.grid_configure(state='normal')
			self.entry_type.grid_configure(state='normal')
			self.entry_focus.grid_configure(state='normal')
		elif input == 'inactive':
			self.entry_name.grid_configure(state='disabled')
			self.entry_type.grid_configure(state='disabled')
			self.entry_focus.grid_configure(state='disabled')			


class Application(tk.Frame):
	'''
	This is the primary class for the RPGTool script. It's responsible for building the UI.
	'''
    
	def __init__(self, parent=root):
		'''
        Constructor. Initializes the application.
        '''
		tk.Frame.__init__(self, parent)
        
		top = self.winfo_toplevel()
		top.columnconfigure(0,weight=1)
		top.rowconfigure(0,weight=1)
        
		self.grid(sticky=tk.N+tk.E+tk.S+tk.W)
		self.rowconfigure(1, weight=1)
		self.columnconfigure(1, weight=1)
        
		self.entry_dict = {}
		self.character_dict = {}
        
		self.canvas = Canvas(self,1,1)
		self.menu = MainMenu(self)
		self.info = InfoColumn(self,1,0)

		#self.info.get_labeldict

def main():
    
    app = Application(root)
    app.master.title('RPG Assistant')
    app.master.geometry('1200x600+100+100')
    app.master.tk.call('wm','iconphoto',app.master._w,photo)
    
    app.mainloop()

if __name__ == '__main__':
    main()

    '''
TODO:
Mechanical Stuff
	DONE: Toplevel menu needs commnds
	DONE: Add InfoColumn on the left side of the Canvas
		How to display PC vs NPC character info?
		Is all player stats necessary?
		Could we generalize the whole application to use just the following
			Name, Age, Level, Alignment?
	Add Player Manager to add and remove players from the player dictionary
	Add Canvas writing handler for all new characters
	Add Save/Load support

Beautification Stuff:
	Add Minimum Size to each frame

	...probably a bunch of other stuff, too.
'''