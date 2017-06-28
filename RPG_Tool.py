'''
Created on Mar 7, 2017

@author: Michael
'''
#!/usr/bin/env python
import tkinter as tk
import os
from tkinter.font import Font

'''
TODO:
    - need a character dictionary saved in Application namespace
    - need a getter method to make player dictionary accessible
    - info columns still need to be able to import data into character dictionary
    - canvas needs to be able to draw players / logos using info in player dictionary [PlayerHandler]
'''





class Application(tk.Frame):
    '''
    This is the primary class for the RPGTool script. It's responsible for building the UI.
    '''
    
    def __init__(self, master=None):
        '''
        Constructor. Initializes the application.
        '''
        tk.Frame.__init__(self, master)
        
        top = self.winfo_toplevel()
        top.columnconfigure(0,weight=1)
        top.rowconfigure(0,weight=1)
        
        self.grid(sticky=tk.N+tk.E+tk.S+tk.W)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.entry_dict = {}
        self.character_dict = {}
        
        self.infoColumn = InfoColumn(self)
        self.add_canvas(self)
        self.add_menu(self)
        
        
        '''
        children = self.get_children(self)
        self.config(bg='#696969')
        for entry in children:
            entry.config(bg = '#696969')
        '''
        
    def add_canvas(self,parent):
        '''
        This method adds the canvas to the frame passed as "parent" to grid location r0,c1.
        The canvas occupies a 5 x 5 gridspace.
        '''
        can_1 = tk.Canvas(parent, bg = '#fff', bd=2, relief='groove')
        can_1.grid(row=0,column=1,rowspan= 5, columnspan=5, sticky=tk.N+tk.S+tk.E+tk.W ,pady=5,padx=5)
        can_1.columnconfigure(1, weight=1)
        can_1.rowconfigure(1, weight=1)
        
    def add_menu(self,parent):
        '''
        This method adds the menu bar to the top level window of the frame passed as "parent".
        '''       
        
        #Devnote: Use "top Level Menu" for these commands!
        
        menu_font = Font(family = 'Segoe UI', size = 9)
        
        top = parent.winfo_toplevel()
        parent.menuBar = tk.Menu(top, activebackground = '#00a1f1', activeforeground = '#ffffff', font = menu_font)
        top['menu'] = parent.menuBar
        
        '''
        TODO: These menu elements need action listeners!
        '''
        
        parent.subMenu_file = tk.Menu(parent.menuBar, activebackground = '#00a1f1', activeforeground = '#ffffff', font = menu_font, tearoff=0)
        parent.menuBar.add_cascade(label = 'File', menu=parent.subMenu_file)
        
        self.new_menu = tk.Menu(activebackground = '#00a1f1', activeforeground = '#ffffff', font = menu_font, tearoff=0)
        self.new_menu.add_command(label='Numenera Player', command = lambda:parent.playerwindow(parent))
        self.new_menu.add_command(label='Numenera NPC', command= lambda:parent.npcwindow(parent))
        
        parent.subMenu_file.add_cascade(label = 'New', menu = self.new_menu)
        
        parent.subMenu_file.add_command(label='Load Charater', command=None)
        parent.subMenu_file.add_separator()
        parent.subMenu_file.add_command(label = 'Save', command=None)
        parent.subMenu_file.add_command(label='Save As...', command=None)
        parent.subMenu_file.add_command(label='Open', command=None)
        
        parent.subMenu_edit = tk.Menu(parent.menuBar, activebackground = '#00a1f1', activeforeground = '#ffffff', font = menu_font, tearoff=0)
        parent.menuBar.add_cascade(label='Edit', menu=parent.subMenu_edit)
        parent.subMenu_edit.add_command(label='Undo      [Ctrl+Z]', command=None)
        parent.subMenu_edit.add_command(label='Redo      [Ctrl+Y]', command=None)
        parent.subMenu_edit.add_separator()
        parent.subMenu_edit.add_command(label='NewCommandHere', command=None)
        
        parent.subMenu_sys = tk.Menu(parent.menuBar, activebackground = '#00a1f1', activeforeground = '#ffffff', font = menu_font, tearoff=0)
        parent.menuBar.add_cascade(label='System', menu=parent.subMenu_sys)
        parent.subMenu_sys.add_command(label='NewSystemCommandHere', command=None)

    def playerwindow(self,parent):
        '''
        Generates a new window inside which the user may enter the stats for a new Numenera Player.
        '''
        
        self.new_window = tk.Toplevel(takefocus=True)
        self.new_window.focus()
        self.new_window.geometry('400x300+300+150')
        self.new_window.title('New Numenera Player')
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        
        top = self.new_window.winfo_toplevel()
        top.columnconfigure(0,weight=1)
        top.rowconfigure(0,weight=1)
        
        self.frame = tk.Frame(self.new_window)
        self.frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        
        self.info = InfoColumn(self.frame)
        
        self.entry_dict = self.info.get_entrydict()
        self.label_dict = self.info.get_labeldict()
        
        edict = self.entry_dict.values()
        
        for key in edict:
            key.config(state='normal', validate='key')
        
        self.label_dict['level'].destroy()
        self.entry_dict['level'].destroy()
                
                
        '''
        TODO: This method is incomplete and needs to be able to read the inputs from the infocolumn.
        '''
        
    def npcwindow(self,parent):
        '''
        Generates a new window inside which the user may enter the stats for a new Numenera NPC.
        '''
        
        self.new_window = tk.Toplevel(takefocus=True)
        self.new_window.focus()
        self.new_window.geometry('400x500+300+150')
        self.new_window.title('New Numenera NPC')
        
        top = self.new_window.winfo_toplevel()
        top.columnconfigure(1,weight=1)
        top.rowconfigure(0,weight=1)
        
        '''
        TODO: Fix the logo call at the NPC Window and PC Window levels. I think the problem is that
        I'm changing the directory to cwd+'image', so when that gets done below, we change directory
        AGAIN.
        '''
        
        
        #photo = WindowLogo()
        #top.master.tk.call('wm','iconphoto',top.master._w,photo)
        
        self.frame = tk.Frame(self.new_window)
        self.frame.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        
        self.info = InfoColumn(self.frame)
        
        self.entry_dict = self.info.get_entrydict()
        self.label_dict = self.info.get_labeldict()
        
        edict = self.entry_dict.values()
        
        name_list = ['name','level']
        
        for key in edict:
            key.config(state='normal', validate='key')
        
        for key, value in self.entry_dict.items():
            if key not in name_list:
                value.destroy()
                
        for key, value in self.label_dict.items():
            if key not in name_list:
                value.destroy()
        
        new_frame = tk.Frame(self.frame)
        new_frame.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        
        soc_lvl = tk.Label(new_frame,text = 'Social Level', name='soclvl')
        intatk_lvl = tk.Label(new_frame,text = 'Int Attack Level', name='intatklvl')
        intdef_lvl = tk.Label(new_frame,text = 'Int Defense Level', name='intdeflvl')
        spd_lvl = tk.Label(new_frame,text = 'Speed Level', name='spdlvl')
        rgdatk_lvl = tk.Label(new_frame,text = 'Ranged Attack Level', name='rgdatklvl')
        hthatk_lvl = tk.Label(new_frame,text = 'Melee Attack Level', name='hthatklvl')
        physdef_lvl = tk.Label(new_frame,text = 'Physical Defense Level', name='physdeflvl')
        envdef_lvl = tk.Label(new_frame,text = 'Environment Defense Level', name='envdeflvl')
        slth_lvl = tk.Label(new_frame,text = 'Stealth Level', name='slthlvl')
        dgd_lvl = tk.Label(new_frame,text = 'Speed Defense Level', name='dgdlvl')
        
        soc_lvl.grid(row=0,column=0,sticky=tk.W, pady=5, padx=5)
        intatk_lvl.grid(row=1,column=0,sticky=tk.W, pady=5, padx=5)
        intdef_lvl.grid(row=2,column=0,sticky=tk.W, pady=5, padx=5)
        spd_lvl.grid(row=3,column=0,sticky=tk.W, pady=5, padx=5)
        rgdatk_lvl.grid(row=5,column=0,sticky=tk.W, pady=5, padx=5)
        hthatk_lvl.grid(row=6,column=0,sticky=tk.W, pady=5, padx=5)
        physdef_lvl.grid(row=7,column=0,sticky=tk.W, pady=5, padx=5)
        envdef_lvl.grid(row=8,column=0,sticky=tk.W, pady=5, padx=5)
        slth_lvl.grid(row=9,column=0,sticky=tk.W, pady=5, padx=5)
        dgd_lvl.grid(row=4,column=0,sticky=tk.W, pady=5, padx=5)
        
        
        '''
        TODO: Add additional "optional level" stats to NPCs.
        '''
        
        
        
        
        
        '''
        for entry in bottomframe.winfo_children():
            if entry.winfo_class() == 'Label':
                entry.config(text = 'General Level')   
        '''
        
        '''
        TODO: This method is incomplete and needs to be able to read the inputs from the infocolumn.
        
            - It would be nice to have different level attributes for basic actions so users can specify
            thinks like a level 3 NPC does physical attacks as a level 2 NPC but resists mental attacks
            at a level 5, or something of that ilk.
        '''
        
    def get_children(self,parent):
        '''
        Returns a list of all of the children in all of the widgets inside of the frame or 
        window passed as "parent".
        '''
        child_list = parent.winfo_children()
        for item in child_list:
            if item.winfo_children():
                child_list.extend(item.winfo_children())
                
        return child_list        
        
    def get_canvas(self,parent):
        '''
        This method makes the assumption that there is only one canvas. It returns the canvas object.
        '''
        for item in parent.winfo_children():
            if item.winfo_children() == 'Canvas':
                return item
        
        
        
        
class PlayerHandler:
    '''
    This class will handle all the manipulation of the player dictionary as well as draw all of the
    characters onto the canvas.
    '''
    def __init__(self,application):
        '''
        This constructs the PlayerHandler. Not sure what needs to go here yet, but I do know that it
        needs to have the application class passed to it in order for it to be able to do anything.
        '''
        self.canvas = application.get_canvas()
    
    
class WindowLogo:
    
    '''
    This class returns the window logo object to be added to the parent.tk.call() method.
    '''
    def __init__(self):
        
        '''
        cwd = os.getcwd() 
        #You must change directory or Python can't find the image. This will likely happen with save files, too.
        os.chdir(cwd+'\images')
        photo = tk.PhotoImage(file = 'knight.gif')
        
        return photo
        '''
    
class InfoColumn:
    
    def __init__(self,parent):
        
        '''
        This method adds the infocolumn widgets to frame passed as "parent".
        '''
        
        self.entry_dict = {}
        self.label_dict = {}
        
        new_frame = tk.Frame(parent)
        new_frame.grid(row = 0, column = 0, sticky=tk.N+tk.S+tk.E+tk.W)
        
        statl_frame = tk.Frame(new_frame)
        statl_frame.grid(row=3, column=0, sticky=tk.W+tk.N)
        statn_frame = tk.Frame(new_frame)
        statn_frame.grid(row=3, column=1,sticky=tk.W+tk.N)
        
        char_name = tk.Label(new_frame,text = 'Name', name='nameLabel')
        char_type = tk.Label(new_frame,text = 'Class', name='classLabel')
        char_focus = tk.Label(new_frame,text = 'Focus', name='focusLabel')
        char_might = tk.Label(statl_frame, text = 'Might', name='mightLabel')
        char_speed = tk.Label(statl_frame, text = 'Speed', name='speedLabel')
        char_int = tk.Label(statl_frame, text = 'Intellect', name='intLabel')
        npc_lvl = tk.Label(statl_frame, text = 'Level', name='levelLabel')
        char_name.grid(row=0,column=0,sticky=tk.W,pady=5, padx=5)
        char_type.grid(row=1,column=0,sticky=tk.W,pady=5, padx=5)
        char_focus.grid(row=2,column=0,sticky=tk.W,pady=5, padx=5)
        char_might.grid(row=0,column=0,sticky=tk.W,pady=5, padx=5)
        char_speed.grid(row=1,column=0,sticky=tk.W,pady=5, padx=5)
        char_int.grid(row=2,column=0,sticky=tk.W,pady=5, padx=5)
        npc_lvl.grid(row=3,column=0,sticky=tk.W,pady=5, padx=5)
        
        self.label_dict['name'] = char_name
        self.label_dict['type'] = char_type
        self.label_dict['focus'] = char_focus
        self.label_dict['might'] = char_might
        self.label_dict['speed'] = char_speed
        self.label_dict['int'] = char_int
        self.label_dict['level'] = npc_lvl

        ent_n = tk.Entry(new_frame,bg = '#fff', state='readonly', name='nameEntry')
        ent_t = tk.Entry(new_frame,bg = '#fff', state='readonly', name='typeEntry')
        ent_f = tk.Entry(new_frame,bg = '#fff', state='readonly', name='focusEntry')
        ent_m = tk.Entry(statn_frame,bg = '#fff', state='readonly', width = 3, name='mightEnty', validatecommand=(parent.register(self.validate_num),'%d','%S'))
        ent_s = tk.Entry(statn_frame,bg = '#fff', state='readonly', width = 3, name='speedEntry', validatecommand=(parent.register(self.validate_num),'%d','%S'))
        ent_i = tk.Entry(statn_frame,bg = '#fff', state='readonly', width = 3, name='intEntry', validatecommand=(parent.register(self.validate_num),'%d','%S'))
        ent_l = tk.Entry(statn_frame,bg = '#fff', state='readonly', width = 3, name='levelEntry', validatecommand=(parent.register(self.validate_num),'%d','%S'))
        
        self.entry_dict['name'] = ent_n
        self.entry_dict['type'] = ent_t
        self.entry_dict['focus'] = ent_f
        self.entry_dict['might'] = ent_m
        self.entry_dict['speed'] = ent_s
        self.entry_dict['int'] = ent_i
        self.entry_dict['level'] = ent_l
        
        ent_n.grid(row=0, column=1,pady=5, padx=5)
        ent_t.grid(row=1, column=1,pady=5, padx=5)
        ent_f.grid(row=2, column=1,pady=5, padx=5)
        ent_m.grid(row=0, column=0,pady=5, padx=5,sticky=tk.W)
        ent_s.grid(row=1, column=0,pady=5, padx=5,sticky=tk.W)
        ent_i.grid(row=2, column=0,pady=5, padx=5,sticky=tk.W)
        ent_l.grid(row=3, column=0, pady=5, padx=5,sticky=tk.W)
        
        slash_label1 = tk.Label(statn_frame,text='/', name='slashLabel1')
        slash_label2 = tk.Label(statn_frame,text='/', name='slashLabel2')
        slash_label3 = tk.Label(statn_frame,text='/', name='slashLabel3')
        slash_label1.grid(row=0,column=1)
        slash_label2.grid(row=1,column=1)
        slash_label3.grid(row=2,column=1)
        
        self.label_dict['slash1'] = slash_label1
        self.label_dict['slash2'] = slash_label2
        self.label_dict['slash3'] = slash_label3
        
        tot_m = tk.Entry(statn_frame,bg = '#fff', state='readonly', width = 3, name='mightEntryTot', validatecommand=(parent.register(self.validate_num),'%d','%S'))
        tot_s = tk.Entry(statn_frame,bg = '#fff', state='readonly', width = 3, name='speedEntryTot', validatecommand=(parent.register(self.validate_num),'%d','%S'))
        tot_i = tk.Entry(statn_frame,bg = '#fff', state='readonly', width = 3, name='intEntryTot', validatecommand=(parent.register(self.validate_num),'%d','%S'))
        tot_m.grid(row=0, column=3,pady=5, padx=5,sticky=tk.W)
        tot_s.grid(row=1, column=3,pady=5, padx=5,sticky=tk.W)
        tot_i.grid(row=2, column=3,pady=5, padx=5,sticky=tk.W)
        
        self.entry_dict['mightTot'] = tot_m
        self.entry_dict['speedTot'] = tot_s
        self.entry_dict['intTot'] = tot_i
         
    def validate_num(self, action, text):
        '''
        A validation method for the infocolumn entry widgets. This validation class prevents
        users from being able to type in any non-numerical character.
        '''
        int_list = '0123456789'
        
        if text in int_list:
            try:
                float(text)
                return True
            except ValueError:    
                return False
        else:
            return False 
        
        
    def get_entrydict(self):
        
        return self.entry_dict
    
    def get_labeldict(self):
        
        return self.label_dict
    
    
    
    
    

def main():
    
    app = Application()
    app.master.title('RPG Assistant')
    app.master.geometry('1200x600+100+100')
    
    cwd = os.getcwd() 
    #You must change directory or Python can't find the image. This will likely happen with save files, too.
    os.chdir(cwd+'\images')
    photo = tk.PhotoImage(file = 'knight.gif')
    app.master.tk.call('wm','iconphoto',app.master._w,photo)
    
    app.mainloop()

if __name__ == '__main__':
    main()