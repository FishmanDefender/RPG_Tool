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

'''
All TAGS:
	- TODO: Header denotes comment sections that list elements that still must be added or features that need to be completed.
	- FUTURE: Header denotes comment sections that list potential future expansions of the code (after 1.0 stable release)
	- EFFICIENCY: Header denotes comment sections that deal with code efficiency
	- DONE: Used to denote a subline comment, typically in a 'TODO' block, that has been completed.
'''

root = tk.Tk()
home_path = os.getcwd()
os.chdir(home_path+'\images')
photo = tk.PhotoImage(file = 'knight.gif')
os.chdir(home_path)
'''
This program has two global variables:
	- home_path: This is the path to the location of RPG_Tool.py
	- photo: This is the logo photo 'knight.gif' that is used as the logo for all windows
'''
menu_font = Font(family = 'Segoe UI', size = 9)
'''
This sets the fonts used in the application as global variables.
'''

class player_handler():
	'''
	Handles all player additions, subtractions, edits, and deletions.
	'''

	def __init__(self,parent):
		'''
		Builds all of the handler componenets.
		'''

		#Defining the character dictionary.
		self.character_dict = {}

		#Iteration dictionary for name equivelence
		self.it_dict = {}

	def add_player(self,tuple):
		'''
		Takes the first entry of the passed tuple and adds an entry to character_dict of the form ('entry0' : tuple) so the 'name' entry is the key and the tuple is the value.
		'''

		name = str(tuple[0])
		self.character_dict[name] = tuple

	def get_keys(self):
		'''
		Returns the keys of the character dictionary in alphabetical order
		'''

		char_keys = sorted(self.character_dict.keys())
		print (char_keys)
		return char_keys

	def get_entry(self,key):
		'''
		Returns an entry in character_dict that corresponds to the key that is passed as an argument
		'''
		strkey = str(key)
		char_tup = self.character_dict[strkey]

		return char_tup

	def set_entry(self,oldkey,newkey,tuple):
		'''
		Delets the entry assigned to oldkey and enters a player tuple assigned to newkey. If oldkey == newkey, then the entry is merely replaced.
		'''

		if oldkey == newkey:
			self.character_dict[str(oldkey)] = tuple
		else:
			del self.character_dict[str(oldkey)]
			self.character_dict[str(newkey)] = tuple

	def check_dict(self,key):
		'''
		Returns a boolean True if the key is an element of character_dict.
		'''

		#Gets all current keys
		char_keys = self.get_keys()

		#Checking the existence of 'key'
		if key in char_keys:
			return True
		else:
			return False


	def check_dict_add(self,key):
		'''
		Checks all keys currently in the character_dict and checks to see if any are identical to the passed key. If an identity equivelence is found, then (i) is appended to the end of the name (where i is an int) and i is iterated by 1.
		'''

		#Checking for equivelence
		if self.check_dict(key):

			#If a match is found, tries to get the current iteration dictionary for the name
			try:

				it = self.it_dict[key]
				it = it+1
				self.it_dict[key] = it

			#If the key isn't in the dictionary, a KeyError is thrown and, when caught, creates a new it_dict entry with it = 0
			except KeyError:

				it = 0
				self.it_dict[key] = it

			#Append (it) to end of key; returns key
			newkey = key + ' (' + str(it) +')'
			return newkey

		else:
			#If no match is found, it returns the original key
			return key

		'''
		TODO:
			- DONE: Add the check_dict_add method to AddChar class
			- DONE: Since this returns a key, return handling shouldn't need editing
		'''

	def rem_entry(self,key):
		'''
		Removes an entry, whose key is passed as 'key' from character_dict.
		'''	

		#Deletes the entry passed as 'key'
		del self.character_dict[str(key)]


class Edit_warn(tk.Toplevel):
	'''
	Creates a transient, top-level window that interupts the edit-push process of EditChar. It gives the user options to overwrite, iterate, or cancel the edit action.
	'''

	def __init__(self,parent,key):
		'''
		Constructs the new top-level componenet
		'''

		#Inherets from tk.Toplevel
		tk.Toplevel.__init__(self,parent)

		#defining the 'top'
		top = self.winfo_toplevel()
		top.columnconfigure(0, weight=1)
		top.rowconfigure(0, weight=1)

		#Setting 'top' characteristics
		self.title('Overwrite Warning!')
		self.geometry('300x250+600+200')
		self.tk.call('wm','iconphoto',self._w,photo)

		self.transient()
		self.lift(aboveThis=parent)
		self.focus()

		#Grabbing the focus(??). Supposed to make it so the dialogue box MUST be answered before continuing.
		self.grab_set()

		#Building the new Frame object
		self.top_frame = tk.Frame(self)

		#Defining frame characteristics
		self.top_frame.grid(sticky=tk.N+tk.E+tk.S+tk.W)
		self.top_frame.rowconfigure(5,weight=1)
		self.top_frame.columnconfigure(5,weight=1)

		#Building the 'warning message' widget
		self.warn_msg = tk.Message(self.top_frame,text='The following action will overwrite '+str(key)+'!'+'\nAre you sure you want to continue?',justify=tk.CENTER)

		#Building option buttons
		self.overwrite = tk.Button(self.top_frame,text='Overwrite', command= lambda: self.set_res(parent,'over'))
		self.duplicate = tk.Button(self.top_frame,text='Duplicate', command= lambda: self.set_res(parent,'dupe'))
		self.cancel = tk.Button(self.top_frame,text='Cancel', command= lambda: self.set_res(parent,'can'))

		#Adding everything to grid manager
		self.warn_msg.grid(row=0,column=0,rowspan=2,columnspan=3,padx=5,pady=5)
		self.overwrite.grid(row=1,column=0,padx=5,pady=5)
		self.duplicate.grid(row=1,column=1,padx=5,pady=5)
		self.cancel.grid(row=1,column=2,padx=5,pady=5)

		'''
		TODO:
			- Impliment Edit_warn inside the EditChar class.
			- NOTE: The player_handler class check_dict_add cannot be edited since it's used in AddChar
			- TEST!! (This class is untested!)
		'''

		'''
		TODO:
			- The methods below need actual code in them that can pass into a method in EditChar
		'''

	def set_res(self,parent,response):
		'''
		Sets the response veariable for Edit_warn
		'''
		#Pushing res_var back to parent
		parent.res_var = str(response)

		#Destroy Window
		self.destroy()



class Rem_warn(tk.Toplevel):
	'''
	Brings up a warning window whenever a user tries to delete a character asking for a confirmation.
	'''

	def __init__(self,parent):
		'''
		Constructor for the class
		'''

		#Inherets from tk.Toplevel
		tk.Toplevel.__init__(self,parent)

		#defining the 'top'
		top = self.winfo_toplevel()
		top.columnconfigure(0, weight=1)
		top.rowconfigure(0, weight=1)

		#Setting 'top' characteristics
		self.title('Overwrite Warning!')
		self.geometry('300x250+600+200')
		self.tk.call('wm','iconphoto',self._w,photo)

		self.transient()
		self.lift(aboveThis=parent)
		self.focus()

		#Grabbing the focus(??). Supposed to make it so the dialogue box MUST be answered before continuing.
		self.grab_set()

		#Building the new Frame object
		self.top_frame = tk.Frame(self)

		#Defining frame characteristics
		self.top_frame.grid(sticky=tk.N+tk.E+tk.S+tk.W)
		self.top_frame.rowconfigure(5,weight=1)
		self.top_frame.columnconfigure(5,weight=1)


class EditChar(tk.Toplevel):
	'''
	Builds the new top-level window for editing a specific character
	'''

	def __init__(self,parent):
		'''
		The constructor for the edit window. It runs as a child of whatever is passed as the parent.
		'''

		#Inherets from tk.Toplevel
		tk.Toplevel.__init__(self,parent)

		#defining the 'top'
		top = self.winfo_toplevel()
		top.columnconfigure(0, weight=1)
		top.rowconfigure(0, weight=1)

		#Setting 'top' characteristics
		self.title('Edit Character')
		self.geometry('300x250+600+200')
		self.tk.call('wm','iconphoto',self._w,photo)

		self.transient()
		self.lift(aboveThis=parent)
		self.focus()

		#Building the new Frame object
		self.top_frame = tk.Frame(self)

		#Defining frame characteristics
		self.top_frame.grid(sticky=tk.N+tk.E+tk.S+tk.W)
		self.top_frame.rowconfigure(5,weight=1)
		self.top_frame.columnconfigure(5,weight=1)

		#Setting things up for the Option Menu
		chars = parent.player_handler.get_keys()
		chars.insert(0, 'Select Character')
		self.char_var = tk.StringVar()
		self.char_var.set(chars[0])

		#Adding the Option Menu
		self.options = tk.OptionMenu(self.top_frame, self.char_var, *chars, command = lambda _:self.set_entries(parent))
		self.options.config(bg = '#fff')

		#Adding labels and Entries
		self.name = tk.Label(self.top_frame,text='Name')
		self.type = tk.Label(self.top_frame,text='Type')
		self.focus = tk.Label(self.top_frame,text='Focus')

		self.entry_name = tk.Entry(self.top_frame,state='disabled')
		self.entry_type = tk.Entry(self.top_frame,state='disabled')
		self.entry_focus = tk.Entry(self.top_frame,state='disabled')

		#Adding the button at the bottom
		self.button = tk.Button(self.top_frame,text='Save Changes',state='disabled',command= lambda : self.push_changes(parent))	

		#Aligning all widgets to the grid
		self.options.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

		self.name.grid(row=1,column=0,padx=5,pady=5)
		self.type.grid(row=2,column=0,padx=5,pady=5)
		self.focus.grid(row=3,column=0,padx=5,pady=5)

		self.entry_name.grid(row=1,column=1,padx=5,pady=5)
		self.entry_type.grid(row=2,column=1,padx=5,pady=5)
		self.entry_focus.grid(row=3,column=1,padx=5,pady=5)

		self.button.grid(row=4,column=0,columnspan=2,padx=5,pady=5)

	def build_tuple(self):
		'''
		Constructs the tuple of form (name,type,focus) and returns it. This was copied from AddChar since the process to 'edit' character_dict is just to replace the entry with a new tuple.
		'''

		charname = str(self.entry_name.get())
		chartype = str(self.entry_type.get())
		charfocus = str(self.entry_focus.get())

		chartuple = (charname, chartype, charfocus)

		return chartuple


	def push_changes(self,parent):
		'''
		Pushes all edits to the character dictionary
		'''

		#Instantiate default res_var value
		self.res_var = 'over'

		#Constructing a new tuple in case one of the entries changed
		newtup = self.build_tuple()

		#Checking to see if newtup will overwrite any current entries
		if parent.player_handler.check_dict(newtup[0]):
			Edit_warn(self,newtup[0])

		#Here I'm actually pushing the new tuple into the character_dict. Since the option menu has to be used in order for the button to activate, there's no chance for self.selection to be undefined so it's safe to use.
		if self.res_var == 'over':
			parent.player_handler.set_entry(self.selection,newtup[0],newtup)
		elif self.res_var == 'dupe':
			parent.player_handler.set_entry(self.selection,parent.player_handler.check_dict_add(newtup[0]),newtup)

		#The only thing left to do is kill the window.
		self.destroy()

		'''
		TODO:
			- DONE: Finish the 'EditChar' class by making this command actually push changes to player_handler
			- Add confirmation pop-up before push is completed
				- This methid WILL overwrite character 'a' if a character 'b's name is changed to 'a'
				- Throw a warning window when editing names that currently exist!

		FUTURE:
			- Add 'change buffer' so ctrl+z can undo an edit
			- Add 'change confirmation' redundancy to disable the button if no changes are detected.
		'''

	def set_entries(self,parent):
		'''
		This updates all of the entry widgets each time the option menu is accessed/changed.
		'''

		#Getting the current Selection
		self.selection = str(self.char_var.get())

		#Setting all of the entry widgets
		if self.selection != 'Select Character':
			char_tup = parent.player_handler.get_entry(self.selection)

			#If the key submitted isn't the 'dummy key', then the entries will be enabled and will display the stats of the character selected.
			cont_1 = tk.StringVar()
			cont_1.set(char_tup[0])

			cont_2 = tk.StringVar()
			cont_2.set(char_tup[1])

			cont_3 = tk.StringVar()
			cont_3.set(char_tup[2])

			self.entry_name.config(textvariable=cont_1,state='normal')
			self.entry_type.config(textvariable=cont_2,state='normal')
			self.entry_focus.config(textvariable=cont_3,state='normal')
			self.button.config(state='normal')

		else:

			#Otherwise, the entry widgets will display nothing and the widgets will be disabled.
			control = tk.StringVar()
			control.set('')

			self.entry_name.config(textvariable=control)
			self.entry_type.config(textvariable=control)
			self.entry_focus.config(textvariable=control)

			self.entry_name.config(state='disabled')
			self.entry_type.config(state='disabled')
			self.entry_focus.config(state='disabled')

			self.button.config(state='disabled')



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

		#Adding the button at the bottom
		self.button = tk.Button(self.top_frame,text='Add Character',command= lambda : self.complete(parent)) #Command here is a Lambda so I can pass a tuple as an argument.	

		#Aligning all widgets to the grid
		self.name.grid(row=0,column=0,padx=5,pady=5)
		self.type.grid(row=1,column=0,padx=5,pady=5)
		self.focus.grid(row=2,column=0,padx=5,pady=5)

		self.entry_name.grid(row=0,column=1,padx=5,pady=5)
		self.entry_type.grid(row=1,column=1,padx=5,pady=5)
		self.entry_focus.grid(row=2,column=1,padx=5,pady=5)

		self.button.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

	def build_tuple(self):
		'''
		Constructs the tuple of form (name,type,focus) and returns it.
		'''

		charname = str(self.entry_name.get())
		chartype = str(self.entry_type.get())
		charfocus = str(self.entry_focus.get())

		chartuple = (charname, chartype, charfocus)

		return chartuple

	def complete(self,parent):
		'''
		Completes the purpose of the window
		'''

		#Instantiates the new player tuple constructor
		char_tup = self.build_tuple()

		#Checks to make sure the new player doesn't already exist; returns the new 'name' element
		new_key = parent.player_handler.check_dict_add(char_tup[0])

		#Since tuples are immutable, we construct a new tuple. This is done regardless of whether the tuple was actually changed
		'''
		EFFICIENCY:
			- Would it be best to use an if function here?
		'''
		new_tup = (new_key,char_tup[1],char_tup[2])

		#Add the tuple to the character dictionary
		parent.player_handler.add_player(new_tup)

		#Kills the window
		self.destroy()


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
		parent.menuBar.add_cascade(label='Test', menu=parent.test)

		'''
		FUTURE:
			- Multi-System Support (ie, D&D, etc)? Can this be built into the design without needing a whole new Charaacter Creation page?
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
        
		self.canvas = Canvas(self,1,1)
		self.menu = MainMenu(self)
		self.info = InfoColumn(self,1,0)

		self.player_handler = player_handler(self)

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
	DONE: Add Player Manager to add players from the character_dict
	Player_handler needs to be able to remove players from the character_dict
	Add Canvas writing handler for all new characters
	Add Save/Load support

Beautification Stuff:
	Add Minimum Size to each frame

	...probably a bunch of other stuff, too.
'''