from tkinter import *

BACKGROUND = "#755c33"
FONT= ("#ced2d4",15,"italic")
# --------------------------task ------------------------------
# Define the save function to add tasks
def save():
    task = entry.get()
    if task:  # Check if there is text
        list_box.insert(END, task)
        entry.delete(0, END)

# Define the delete function to remove selected task
def delete():
    # Get the currently selected task
    selected_task_index = list_box.curselection()
    if selected_task_index:  # Check if a selection exists
        list_box.delete(selected_task_index)  # Delete the selected item
# -------------------------- store the data -------------------------------
def save_to_file():
    # Open the file in write mode
    with open("store.txt", "w") as memory:
        # Get all items from the Listbox
        tasks = list_box.get(0, END)
        # Write each item to the file
        for task in tasks:
            memory.write(task + "\n")

# -------------------------- UI -------------------------------
win = Tk()
win.config(padx=20, pady=20,bg=BACKGROUND)
win.geometry("300x400+800+100")
win.resizable()
win.title("To Do App")

frame = Frame(width=200,height=200,pady=20)
frame.grid(row=0, column=0, columnspan=2)
frame.grid_propagate(False)  # Prevent frame from resizing to fit contents


# Create a Listbox widget with vertical scrolling support
list_box = Listbox(frame, yscrollcommand=lambda *args: scroll_box.set(*args), width=40, height=10)
list_box.grid(row=0, column=0)

# Create a Scrollbar widget and attach it to the Listbox
scroll_box = Scrollbar(frame, orient=VERTICAL, command=list_box.yview)
scroll_box.grid(row=0, column=1, sticky='ns')

# Sample list of tasks
list_text = [
    "Pray and Read Qur'an",
    "Code", "Touch Type",
    "Maths", "Project",
    "Teach", "Research"
]

# Insert each item from the list into the Listbox
for item in list_text:
    list_box.insert(END, item)


add=Button(text="Add Task",bg="#408994",font=FONT,command=save)
add.grid(column=0,row=1,pady=10)

delete=Button(text="Delete Task",bg="#f25a1d",font=FONT,command=delete)
delete.grid(column=1,row=1,pady=10)

entry =Entry(width=40,)
entry.grid(row=2,column=0, columnspan=2,padx=5,pady=10,ipady=10)

save_to_file()
win.mainloop()