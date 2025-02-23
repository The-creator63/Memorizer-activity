from tkinter import*
from tkinter.filedialog import*

root = Tk()
root.title("Memorizer")

#add function
def add_item():
    listbox.insert(END,task.get())
    task.delete(0,END)

#delete function
def delete_item():
    index = listbox.curselection()
    if index:
        listbox.delete(index)

def save_file():
    fout = asksaveasfile(defaultextension = ".txt")
    if fout is not None:
        for item in listbox.get(0,END):
            print(item.strip(),file = fout)
        listbox.delete(0,END)

def open_file():
    fin = askopenfile(title = "open file")
    if fin is not None:
        listbox.delete(0,END)
        items = fin.readlines()
        for item in items:
            listbox.insert(END,item.strip())


save_btn = Button(root,text = "Save",width = 15,command = save_file)
save_btn.pack(padx = 5,pady = 5)
task = Entry(root,width = 35)
task.pack(padx = 5,pady = 5)
add_btn = Button(root,text = "Add",width = 15,command = add_item)
add_btn.pack(padx = 5,pady = 5)
open_btn = Button(root,text = "Open",width = 15,command = open_file)
open_btn.pack(side = LEFT,padx = 5,pady = 5)
delete_btn = Button(root,text = "Delete",width = 15,command = delete_item)
delete_btn.pack(side = RIGHT,padx = 5,pady = 5)
frame = Frame(root)
frame.pack(side = RIGHT)
scrollbar = Scrollbar(frame,orient = "vertical")
scrollbar.pack(side = RIGHT,fill = Y)
listbox = Listbox(frame,width = 70,yscrollcommand = scrollbar.set,bg =  "red")
for i in range(1,51):
    listbox.insert(END, "List " + str(i))
listbox.pack(side = LEFT,padx = 5)
scrollbar.config(command = listbox.yview)
root.mainloop()