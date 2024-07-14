import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
import time
import keyboard


def key_handler(event):
    print(event.keycode)
    if event.keycode == 27:
        base.destroy()
        exit()
    
        
def phase2():
    print("Hi")

    start_canvas.destroy()
    game_canvas.pack(fill = 'both', expand = True)

    base.update()
    
    x = 8
    z = 0
    
    while True:
        time.sleep(0.02)
        game_canvas.move(bird_image, 0, x)
        base.update()
        print("x = ",x)
        if keyboard.is_pressed("space") == True:
            while True:
                y = 0
                while True:
                    time.sleep(0.02)
                    if y < 11:
                        y = y + 1
                        print("y = ",y)
                        game_canvas.move(bird_image, 0 , -12)
                        base.update()
                    else:
                        print("c")
                        break
                        
                    if keyboard.is_pressed("space") == True:
                        y = 0
                        print("d")
                
                if y >= 11:
                    print("e")
                    break

            x = 0
        while True:
            print("x = ",x)
            time.sleep(0.02)
            if x < 8:
                x = x + 0.25
            elif x < 12:
                x = x + 0.125
            elif x < 20:
                x = x + 0.0625 
            else:
                break
            game_canvas.move(bird_image, 0, x)
            base.update()
            if keyboard.is_pressed("space") == True:
                break

            


        base.update()


def main():    

    global bird_image, game_canvas, start_canvas, base

    base = tk.Tk()
    base.title("Game")
    base.configure(bg = 'white', )
    base.attributes('-fullscreen' ,True)
    base.minsize(1920,1080)
    base.maxsize(1920,1080)


    start_canvas = tk.Canvas(base)
    start_canvas.configure(bg = 'white', width = 1920, height = 1080)
    start_canvas.pack(fill = 'both', expand = True)

    game_canvas = tk.Canvas(base)
    game_canvas.configure(bg = 'red', width = 1920, height = 1080)
    game_background_img = tk.PhotoImage(file = 'game background.png')
    game_canvas.create_image(960,540, image = game_background_img, anchor = CENTER)

    frame = tk.Frame(start_canvas, width = 1920, height = 1080, bg = 'blue')
    frame.pack()

    settings_button = Button(frame, anchor = CENTER, text = "SETTINGS")
    settings_button.place(x = 960, y = 620, height = 60, width = 200, anchor = CENTER)

    birb_img = tk.PhotoImage(file = "birb4.png")
    bird_image = game_canvas.create_image(320,600, image = birb_img, anchor = CENTER)

    start_button = Button(frame, text = "Start", anchor = 'center', command = phase2)
    start_button.place(x = 960, y = 460, height = 60, width = 200, anchor = CENTER)

    base.bind("<Key>", key_handler)







    base.mainloop()

main()