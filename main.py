from tkinter import *

PIXEL_SIZE = 10

colors = ["black", "white", "purple", "green", "blue", "red", "cyan"]
current_color = "black"

def change_color(color):
    global current_color
    current_color = color

root =  Tk()
root.title("PixelArt")
root.geometry("250x250")
instruments_panel = Frame(root, height= 100, bg='gray')
work_area = Canvas(root, bg='white')
instruments_panel.pack(side = "top", anchor=NW, fill=X, padx=5, pady=5)

buttons = [
Button(instruments_panel, height = 1, width = 1, bg="black", activebackground="black", command = lambda: change_color("black")),
Button(instruments_panel, height = 1, width = 1, bg="white", activebackground="white", command = lambda: change_color("white")),
Button(instruments_panel, height = 1, width = 1, bg="purple", activebackground="purple", command = lambda: change_color("purple")),
Button(instruments_panel, height = 1, width = 1, bg="green", activebackground="green", command = lambda: change_color("green")),
Button(instruments_panel, height = 1, width = 1, bg="blue", activebackground="blue", command = lambda: change_color("blue")),
Button(instruments_panel, height = 1, width = 1, bg="red", activebackground="red", command = lambda: change_color("red")),
Button(instruments_panel, height = 1, width = 1, bg="cyan", activebackground="cyan", command = lambda: change_color("cyan"))]
for but in buttons:
    but.config(highlightbackground="black")
    but.pack(side = "left", padx = 5)
work_area.pack(fill="both", side = "top", expand=1)

def set_point(event):
    x = (event.x)//PIXEL_SIZE*PIXEL_SIZE
    y = event.y//PIXEL_SIZE*PIXEL_SIZE
    work_area.create_rectangle((x, y, x+PIXEL_SIZE, y+PIXEL_SIZE), fill=current_color)


#id = work_area.create_rectangle((60, 60, 100, 100), fill="yellow")
work_area.bind("<Button-1>", set_point)
#work_area.bind("<Button-3>", change_color)

root.mainloop()