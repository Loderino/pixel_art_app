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
Button(instruments_panel, height = 10, width = 10, bg="black", command = lambda: change_color("black")),
Button(instruments_panel, height = 10, width = 10, bg="white", command = lambda: change_color("white")),
Button(instruments_panel, height = 10, width = 10, bg="purple", command = lambda: change_color("purple")),
Button(instruments_panel, height = 10, width = 10, bg="green", command = lambda: change_color("green")),
Button(instruments_panel, height = 10, width = 10, bg="blue", command = lambda: change_color("blue")),
Button(instruments_panel, height = 10, width = 10, bg="red", command = lambda: change_color("red")),
Button(instruments_panel, height = 10, width = 10, bg="cyan", command = lambda: change_color("cyan"))]
for but in buttons:
    but.pack(side = "left")
work_area.pack(fill="both", side = "top", expand=1)

def set_point(event):
    x = (event.x)//PIXEL_SIZE*PIXEL_SIZE
    y = event.y//PIXEL_SIZE*PIXEL_SIZE
    work_area.create_rectangle((x, y, x+PIXEL_SIZE, y+PIXEL_SIZE), fill=current_color)


#id = work_area.create_rectangle((60, 60, 100, 100), fill="yellow")
work_area.bind("<Button-1>", set_point)
#work_area.bind("<Button-3>", change_color)

root.mainloop()