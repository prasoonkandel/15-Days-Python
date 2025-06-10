#Calculator with gui


import tkinter as tk

root = tk.Tk()
root.title("First GUI")
root.geometry("600x400")
  # Note: geometry takes a string in the format "widthxheight"
 
click_count = 0
label1_text = tk.StringVar()
label1_text.set("You clicked the button 0 times")  # Initialize the text

def button_click():
    global click_count
    click_count += 1
    text = f"You clicked the button {click_count} times"
    label1_text.set(text)


button = tk.Button(
    root,
    text="Click Me!",
    bg="green",
    fg="white", 
    command=button_click,
    
).pack()

label1 = tk.Label(root, textvariable=label1_text).pack()  # Use textvariable

root.mainloop()
