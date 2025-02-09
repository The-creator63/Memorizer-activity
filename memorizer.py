from tkinter import*
from tkinter.filedialog import*

root = Tk()
root.title("Memorizer")

save_btn = Button(root,text = "Save",width = 15)
save_btn.pack(padx = 5,pady = 5)
task = Entry(root,width = 35)
task.pack(padx = 5,pady = 5)
add_btn = Button(root,text = "Add",width = 15)
add_btn.pack(padx = 5,pady = 5)
open_btn = Button(root,text = "Open",width = 15)
open_btn.pack(side = LEFT,padx = 5,pady = 5)
delete_btn = Button(root,text = "Delete",width = 15)
delete_btn.pack(side = RIGHT,padx = 5,pady = 5)
frame = Frame(root)
frame.pack(side = RIGHT)
scrollbar = Scrollbar(frame,orient = "vertical")
scrollbar.pack(side = RIGHT,fill = Y)
root.mainloop()