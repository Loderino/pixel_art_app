from tkinter import *

PIXEL_SIZE = 10

status = "draw"
colors = ["black", "white", "purple", "green", "blue", "red", "cyan"]
current_color = "black"

def clear_mode():
    global status
    status = "clear"

def clear_screen():
    for pixel in elements:
        work_area.delete(elements[pixel])
    
def change_color(color):
    global current_color, status
    status = "draw"
    current_color = color

def pixel_click(event, id):
    if status == "clear":
        work_area.delete(id)

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

clear_button = Button(instruments_panel, height = 1, width = 1, text = "X", bg="white", activebackground="white", command = clear_mode)
clear_button.pack(side = "left", padx = 5)

clear_screen_button = Button(instruments_panel, height = 1, width = 8, text = "Очистить", bg="white", activebackground="white", command = clear_screen)
clear_screen_button.pack(side = "right", padx = 5)

elements = {}
def set_point(event):
    if status == "draw":
        x = (event.x)//PIXEL_SIZE*PIXEL_SIZE
        y = event.y//PIXEL_SIZE*PIXEL_SIZE
        if (x, y) in elements:
            work_area.delete(elements[(x, y)])
        id = work_area.create_rectangle((x, y, x+PIXEL_SIZE, y+PIXEL_SIZE), fill=current_color)
        work_area.tag_bind(id, "<Button-1>", lambda event: pixel_click(event, id))
        elements[(x, y)] = id

def big_draw(event):
    x = (event.x)//PIXEL_SIZE*PIXEL_SIZE
    y = event.y//PIXEL_SIZE*PIXEL_SIZE
    if status == "draw":
        set_point(event)
    
    elif status == "clear":
        if (x, y) in elements:
            pixel_click(event, elements[(x, y)])
            

work_area.bind("<B1-Motion>", big_draw)
work_area.bind("<Button-1>", set_point)

root.mainloop()