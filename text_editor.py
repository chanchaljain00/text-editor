import tkinter as tk
from tkinter.ttk import *
from tkinter import * 
from tkinter import font,colorchooser,messagebox
from tkinter.filedialog import askopenfilename,asksaveasfile
import os 

main_application = Tk()
main_application.geometry('800x800')
main_application.title("text editor")

############################################ main menu ################################################
#......................................&&&&&&&&&&End main menu &&&&&&&&&.................................

main_menu = Menu(main_application)

#file icons
new_icon = PhotoImage(file='img/new.png')
open_icon = PhotoImage(file='img/open.png')
save_icon = PhotoImage(file='img/save.png')
save_as_icon = PhotoImage(file='img/save_as.png')
exit_icon = PhotoImage(file='img/exit.png')

file = Menu(main_menu,tearoff=0)



#edit icons
copy_icon = PhotoImage(file='img/copy.png')
paste_icon = PhotoImage(file='img/paste.png')
cut_icon = PhotoImage(file='img/cut.png')
clear_all_icon = PhotoImage(file='img/clear_all.png')
find_icon = PhotoImage(file='img/find.png')

edit = Menu(main_menu,tearoff=0)



# view icons
tool_bar_icon = PhotoImage(file='img/tool_bar.png')
status_bar_icon = PhotoImage(file='img/status_bar.png')

view = Menu(main_menu,tearoff=0)




##########color theme
lightdefault_icon = PhotoImage(file='img/light_default.png')
lightplus_icon = PhotoImage(file='img/light_plus.png')
lightdark_icon = PhotoImage(file='img/dark.png')
red_icon = PhotoImage(file='img/red.png')
monokai_icon = PhotoImage(file='img/monokai.png')
nightblue_icon = PhotoImage(file='img/night_blue.png')


color_theme = Menu(main_menu,tearoff=0)

theme_choice = StringVar()
color_icons = (lightdefault_icon,lightplus_icon,lightdark_icon,red_icon,monokai_icon,nightblue_icon)
color_dict ={
	'Light Default': ('#000000','#ffffff'),
	'Light Plus': ('#474747','#e0e0e0'),
	'Dark': ('#c4c4c4','#2d2d2d'),
	'Red': ('#F92672','#ffe8e8'),
	'Monokai':('#d3b774','#474747'),
	'Night Blue':('#ededed','#6b9dc2')
}



#cascade
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color Theme",menu=color_theme)
############################################ toolbar ################################################

tool_bar = Label(main_application,bg="#F0F0F0")
tool_bar.pack(side=TOP,fill=X)

#font box
font_tuple = font.families()
font_family = StringVar()
font_box = Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)


#size box

size_var = IntVar()
font_size = Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(6,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)


bold_icon = PhotoImage(file="img/bold.png")
italic_icon = PhotoImage(file="img/italic.png")
underline_icon = PhotoImage(file="img/underline.png")
colorpicker_icon = PhotoImage(file="img/font_color.png")
left_align_icon = PhotoImage(file="img/align_left.png")
center_align_icon = PhotoImage(file="img/align_center.png")
right_align_icon = PhotoImage(file="img/align_right.png")





b1 = Button(tool_bar,image=bold_icon)
b1.grid(row=0,column=2,padx=5)
b2 = Button(tool_bar,image=italic_icon)
b2.grid(row=0,column=3,padx=5)
b3 = Button(tool_bar,image=underline_icon )
b3.grid(row=0,column=4,padx=5)
b4 = Button(tool_bar,image=colorpicker_icon)
b4.grid(row=0,column=5,padx=5)
b5 = Button(tool_bar,image=left_align_icon)
b5.grid(row=0,column=6,padx=5)
b6 = Button(tool_bar,image=center_align_icon)
b6.grid(row=0,column=7,padx=5)
b7 = Button(tool_bar,image=right_align_icon)
b7.grid(row=0,column=8,padx=5)
#......................................&&&&&&&&&&End toolbar &&&&&&&&&.................................


############################################text editor ################################################


text_editor = Text(main_application,wrap='word',relief=FLAT)
# text_editor.config(relief=FLAT)

scroll_bar = Scrollbar(main_application)
scroll_bar.pack(side=RIGHT,fill=Y)
text_editor.focus_set()
text_editor.pack(fill=BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size
current_font_family = 'Arial'
current_font_size  = 14

def change_font(self):
	global current_font_family
	current_font_family = font_family.get()
	text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)


def change_size(self):
	global current_font_size
	current_font_size = size_var.get()
	text_editor.configure(font=(current_font_family,current_font_size))

font_size.bind("<<ComboboxSelected>>",change_size)

text_editor.configure(font=('Arial',14))

#button functionality
# print(font.Font().actual())
def change_bold():
 	text_property = font.Font(font=text_editor['font']) 
 	if text_property.actual()['weight'] == 'normal':
 		text_editor.configure(font=(current_font_family,current_font_size,'bold'))
 	else:
 		text_editor.configure(font=(current_font_family,current_font_size,'normal'))

b1.configure(command=change_bold)

#italic functionality
def change_italic():
	text_property = font.Font(font=text_editor['font'])
	if text_property.actual()['slant'] == 'roman':
		text_editor.configure(font=(current_font_family,current_font_size,'italic'))
	else:
		text_editor.configure(font=(current_font_family,current_font_size,'roman'))

b2.configure(command=change_italic)

def change_underline():
	text_property = font.Font(font=text_editor['font'])
	if text_property.actual()['underline'] == 0:
		text_editor.configure(font=(current_font_family,current_font_size,'underline'))
	else:
		text_editor.configure(font=(current_font_family,current_font_size,'normal'))

b3.configure(command=change_underline)
# print(font.Font(font=text_editor).actual())


#font color funtionality
def change_font_color():
	color_var = colorchooser.askcolor()
	# print(color_var)
	text_editor.configure(fg=color_var[1])

b4.configure(command=change_font_color)

#align funtionality

def align_left():
	text_content = text_editor.get('1.0','end')
	text_editor.tag_config('left',justify="left")
	text_editor.delete('1.0','end')
	text_editor.insert(INSERT,text_content,('left'))

b5.configure(command=align_left)

def align_center():
	text_content = text_editor.get('1.0','end')
	text_editor.tag_config('center',justify="center")
	text_editor.delete('1.0','end')
	text_editor.insert(INSERT,text_content,('center'))

b6.configure(command=align_center)

def align_right():
	text_content = text_editor.get('1.0','end')
	text_editor.tag_config('right',justify="right")
	text_editor.delete('1.0','end')
	text_editor.insert(INSERT,text_content,('right'))

b7.configure(command=align_right)
#......................................&&&&&&&&&&End text editor &&&&&&&&&.................................


############################################ status bar ################################################

status_bar = Label(main_application,text="status bar")
status_bar.pack(side=BOTTOM)

text_changed = False

def changed(event=None):
	global text_changed
	if text_editor.edit_modified():
		text_changed = True
		words = len(text_editor.get(1.0,'end-1c').split())
		characters = len(text_editor.get(1.0,'end-1c'))
		lines = len(text_editor.get(1.0,'end-1c').split('\n'))
		col = len(text_editor.get(f'{lines}.0','end'))
		status_bar.config(text=f'Characters: {characters}  Words: {words}  Lines: {lines} col: {col}')
	text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)

#......................................&&&&&&&&&&End status bar &&&&&&&&&.................................


############################################ main menu functionality ################################################

url = ""

##new funtionality

def new_file(event=None):
	global url
	url= ''
	text_editor.delete(1.0,'end')


# file command
file.add_command(label='New',image=new_icon,compound=LEFT,accelerator='Ctrl+N',command=new_file)


## open functionality
def open_file(event=None):
	global url
	url = askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All files',"*.*")))
	try:
		with open(url,'r') as fr:
			text_editor.delete(1.0,'end')
			text_editor.insert(1.0,fr.read())
	except FileNotFoundError:
		return
	except:
		return
	main_application.title(os.path.basename(url))

file.add_command(label='Open',image=open_icon,compound=LEFT,accelerator='Ctrl+O',command=open_file)

##save file
def save_file(event=None):
	global url
	data = text_editor.get(1.0,'end')
	try:
		if url:
			with open(url,'w') as file:
				file.write(data)
		else:
			url=asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
			# print(url)
			url.write(data)
			url.close()
	except:
		return


file.add_command(label='Save',image=save_icon,compound=LEFT,accelerator='Ctrl+S',command=save_file)

#save_as functionality
def save_as(event=None):
	global url
	try:
		data=text_editor.get(1.0,'end')
		url = asksaveasfile(mode='w',default='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
		url.write(data)
		url.close()
	except:
		return

file.add_command(label='Save as',image=save_as_icon,compound=LEFT,accelerator='Ctrl+Alt+S',command=save_as)

# exit functionality

def exit(event=None):
	global url,text_changed
	data = text_editor.get(1.0,'end')

	try:
		if text_changed:
			choice=messagebox.askyesnocancel("Warning","Do you want to save the changes in the file?")
			if choice==True:
				if url:
					with open(url,'w') as file:
						file.write(data)
						main_application.destroy()
				else:
					url = asksaveasfile(mode='w',default='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
					url.write(data)
					url.close()
					main_application.destroy()
			elif choice == False:
				main_application.destroy()
		else :
			main_application.destroy()
		
	except:
		return	

file.add_command(label='Exit',image=exit_icon,compound=LEFT,accelerator='Ctrl+Q',command=exit)


########find functionality
# global find_input

def find():
	word = find_input.get()
	text_editor.tag_remove('match','1.0','end')
	matches = 0
	if word:
		start_pos = '1.0'
		while True:
			start_pos = text_editor.search(word,start_pos,stopindex='end')
			if not start_pos:
				break
			end_pos = f'{start_pos}+{len(word)}c'
			text_editor.tag_add('match',start_pos,end_pos)
			matches += 1
			start_pos = end_pos
			text_editor.tag_config('match',foreground='red',background='yellow')


def replace():
	word = find_input.get()
	replace_text = replace_input.get()
	content = text_editor.get(1.0,'end')
	new_content = content.replace(word,replace_text)
	text_editor.delete('1.0','end')
	text_editor.insert('1.0',new_content)


def find_funct(event=None):
	global find_input
	global replace_input
	find_dialogue = Toplevel()
	find_dialogue.geometry('450x250+500+200')
	find_dialogue.title("Find")
	find_dialogue.resizable(0,0)

	####frame
	find_frame = LabelFrame(find_dialogue,text="Find/Replace")
	find_frame.pack(pady=20)

	#Label
	text_find_label = Label(find_frame,text='Find : ')
	text_replace_label = Label(find_frame,text='Replace : ')

	#entry 
	find_input = Entry(find_frame,width=30)
	replace_input = Entry(find_frame,width=30)


	#button
	find_button = Button(find_frame,text='Find',width=13,command=find)
	replace_button = Button(find_frame,text='Replace',width=13,command=replace)

	#Label grid
	text_find_label.grid(row=0,column=0,padx=4,pady=4)
	text_replace_label.grid(row=1,column=0,padx=4,pady=4)

	##entry grid
	find_input.grid(row=0,column=1,padx=4,pady=4)
	replace_input.grid(row=1,column=1,padx=4,pady=4)

	#button grid
	find_button.grid(row=2,column=0,padx=8,pady=4)
	replace_button.grid(row=2,column=1,padx=8,pady=4)

	find_dialogue.mainloop()


# edit command

edit.add_command(label='Copy',image=copy_icon,compound=LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear all',image=clear_all_icon,compound=LEFT,accelerator='Ctrl+Alt+C',command=lambda:text_editor.delete(1.0,'end'))
edit.add_command(label='Find',image=find_icon,compound=LEFT,accelerator='Ctrl+F',command=find_funct)


#view command
show_toolbar=StringVar()
show_toolbar.set(True)
show_statusbar=StringVar()
show_statusbar.set(True)

def hide_toolbar():
	global show_toolbar
	if show_toolbar:
		tool_bar.pack_forget()
		show_toolbar=False
	else:
		text_editor.pack_forget()
		status_bar.pack_forget()
		tool_bar.pack(side=TOP,fill=X)
		text_editor.pack(fill=BOTH,expand=True)
		status_bar.pack(side=BOTTOM)
		show_toolbar = True

def hide_statusbar():
	global show_statusbar
	if show_statusbar:
		status_bar.pack_forget()
		show_statusbar=False
	else:
		status_bar.pack(side=BOTTOM)
		show_statusbar=True


view.add_checkbutton(label='Tool bar',onvalue=True,offvalue=False,image=tool_bar_icon,variable=show_toolbar,compound=LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status bar',onvalue=True,offvalue=False,image=status_bar_icon,variable=show_statusbar,compound=LEFT,command=hide_statusbar)


# color theme
def change_theme():
	chosen_theme = theme_choice.get()
	color_tuple = color_dict[chosen_theme]
	fg_color,bg_color = color_tuple[0],color_tuple[1]
	text_editor.config(background=bg_color,fg=fg_color)


count = 0
for i in color_dict:
	color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=LEFT,command=change_theme)
	count+=1


#......................................&&&&&&&&&&End main menu functionality &&&&&&&&&.................................

main_application.config(menu=main_menu)

#bind shortcut keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as)
main_application.bind("<Control-q>",exit)
main_application.bind("<Control-f>",find_funct)


main_application.mainloop()