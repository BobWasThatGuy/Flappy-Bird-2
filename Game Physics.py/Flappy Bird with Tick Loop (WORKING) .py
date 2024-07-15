import tkinter as tk
from tkinter import *
import keyboard
import time
import random

def main():

    global base, menu_canvas, game_canvas


    def key_handler(event):
        if event.keycode == 27:
            base.destroy()
            time.sleep(2)

            exit()
            

    def game():

        z = True

        global score

        score = 0
        

        menu_canvas.destroy()
        game_canvas.pack(fill = 'both', expand = True)

        base.update()

        bird = game_canvas.create_image(320, 600, image = flappy.image, anchor = CENTER)
        pipe_x = random.randint(-435, -165)
        pipe_x2 = random.randint(-435, -165)
        top_pipe1 = game_canvas.create_image(1900, pipe_x, image = top_pipe.image, anchor = CENTER)
        bottom_pipe1 = game_canvas.create_image(1900, pipe_x + 1420, image = bottom_pipe.image, anchor = CENTER)
        

        print(game_canvas.coords(top_pipe1))

        descent = False
        checker = True
        checker2 = 0
        tick = 0
        b = True

        time.sleep(0.1)

        temp_time1 = time.time()
        while b == True:
            temp_time2 = time.time()
            if (temp_time2 - temp_time1) > 0.02:
                print(tick)
                tick = tick + 1
                temp_time1 = time.time()

                if tick % 2 == 0:
                    game_canvas.move(bird , 0 , flappy.speed)
                    game_canvas.move(top_pipe1, top_pipe.speed, 0)
                    game_canvas.move(bottom_pipe1, bottom_pipe.speed, 0)

                    if z == False:
                        game_canvas.move(top_pipe2, top_pipe.speed, 0)
                        game_canvas.move(bottom_pipe2, bottom_pipe.speed, 0)

                base.update()


                # 132 x 94

                if (tick % 240  < 202 and tick % 240 > 182):
                    
                    if game_canvas.coords(bird)[1] < (pipe_x + 587) or game_canvas.coords(bird)[1] > (pipe_x + 833):
                        game_canvas.destroy()
                        death_canvas.pack(fill = 'both', expand = True)

                        end_frame = Frame(death_canvas, width = 1920, height = 1080, bg = "red")
                        end_frame.pack()
                        score_button = Button(end_frame, anchor = CENTER, text = ("Score =", score), command = end)
                        score_button.place(x = 960, y = 860, height = 100, width = 320, anchor = CENTER)

                    print("HERE")

                if (tick % 240 < 82 and tick % 240 > 62):
                    if checker2 < 21:
                        checker2 = checker2 + 1
                    
                    elif game_canvas.coords(bird)[1] < (pipe_x2 + 587) or game_canvas.coords(bird)[1] > (pipe_x2 + 833):
                        b = False

                        game_canvas.destroy()
                        death_canvas.pack(fill = 'both', expand = True)

                        end_frame = Frame(death_canvas, width = 1920, height = 1080, bg = "red")
                        end_frame.pack()
                        score_button = Button(end_frame, anchor = CENTER, text = ("Score =", score), command = end)
                        score_button.place(x = 960, y = 860, height = 100, width = 320, anchor = CENTER)

                        print("SCORE",score)

                    print("CHECKER",checker2)

                if tick % 240 == 82 or tick % 240 == 203:
                    if checker == True and tick % 240 == 82:
                        checker = False
                    
                    else:
                        score = score + 1
                        
                        



                    base.update()

                
                if keyboard.is_pressed("space") == True or descent == True:
                    if descent == False:
                        flappy.speed = (-20)
                    descent = True
                    if flappy.speed < 16:
                        flappy.speed = flappy.speed + 1.2
                    
                    elif flappy.speed < 32:
                        flappy.speed = flappy.speed + 0.7

                    else:
                        descent = False

                    if keyboard.is_pressed("space"):
                        if flappy.speed < -40:
                            flappy.speed = flappy.speed - 1
                        elif flappy.speed > 4:
                            flappy.speed = -20
                        elif flappy.speed < 12.1:
                            pass
                        else:
                            flappy.speed = flappy.speed - 12

                if tick % 240 == 0:
                    game_canvas.move(top_pipe1, 0, -pipe_x)
                    game_canvas.move(bottom_pipe1, 0, -pipe_x)
                    pipe_x = random.randint(-500, -165)
                    game_canvas.move(top_pipe1, 1920, pipe_x)
                    game_canvas.move(bottom_pipe1, 1920, pipe_x)

                    base.update()
                
                if tick % 240 == 120:
                    if z == True:
                        pipe_x2 = random.randint(-500, -165)
                        top_pipe2 = game_canvas.create_image(1900, pipe_x2, image = top_pipe.image, anchor = CENTER)
                        bottom_pipe2 = game_canvas.create_image(1900, pipe_x2 + 1420, image = bottom_pipe.image, anchor = CENTER)
                        z = False
                    else:
                        game_canvas.move(top_pipe2, 0, -pipe_x2)
                        game_canvas.move(bottom_pipe2, 0, -pipe_x2)
                        pipe_x2 = random.randint(-500, -165)
                        game_canvas.move(top_pipe2, 1920, pipe_x2)
                        game_canvas.move(bottom_pipe2, 1920, pipe_x2)



    def end():
        base.destroy()
        time.sleep(2)

        exit()
            
        
    base = tk.Tk()
    base.title("Game")
    base.attributes("-fullscreen", True)
    base.minsize(1920,1080)
    base.maxsize(1920,1080)
    base.configure(bg = 'white')

    menu_canvas = tk.Canvas(base)
    menu_canvas.configure(bg = 'white', width = 1920, height = 1080)
    menu_img = tk.PhotoImage(file = 'flaps.png')
    menu_canvas.create_image(960, 540, image = menu_img, anchor = CENTER)
    menu_canvas.pack(fill = 'both', expand = True)

    start_frame = Frame(menu_canvas, width = 1920, height = 1080, bg = 'white')
    start_frame.pack()

    start_button = Button(start_frame, anchor = CENTER, text = "START", command = game)
    start_button.place(x = 960, y = 860, height = 100, width = 320, anchor = CENTER)

    game_canvas = tk.Canvas(base)
    game_canvas.configure(width = 1920, height = 1080)
    game_background = tk.PhotoImage(file = "game background.png")
    game_canvas.create_image(960, 540, image = game_background, anchor = CENTER)

    death_canvas = tk.Canvas(base)
    death_canvas.configure(width = 1920, height = 1080, bg = "red")



    speed = 32
    bird_img = tk.PhotoImage(file = "birb4.png")

    class flap():

        def __init__(self, speed, bird_img):
            self.image = bird_img
            self.speed = speed

    screen_speed = (-16)
    pipe_img = tk.PhotoImage(file = "pipe.png")

    class obstacle():

        def __init__(self, pipe_img, screen_speed):
            self.image = pipe_img
            self.speed = screen_speed

    flappy = flap(speed, bird_img)

    top_pipe = obstacle(pipe_img, screen_speed)
    bottom_pipe = obstacle(pipe_img, screen_speed)

    base.bind("<Key>", key_handler)

    base.mainloop()

main()

