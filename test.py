from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from datetime import datetime
from time import sleep
import threading

def draw_gradient(canvas, color1, color2):
    # Create a gradient from color1 to color2 on the canvas
    for i in range(0, 101):
        r = int(color1[0] + (color2[0] - color1[0]) * i / 100)
        g = int(color1[1] + (color2[1] - color1[1]) * i / 100)
        b = int(color1[2] + (color2[2] - color1[2]) * i / 100)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i * 5, 1000, i * 5, fill=color, width=5)

bg_color = '#ADD8E6'
bg2_color = '#FF0000'
co1 = '#F5F5DC'
co2 = '#7FFFD4'

window = Tk()
window.title("")
window.geometry('1000x550')

canvas = Canvas(window, width=1000, height=550)
canvas.pack()

# Gradient background colors
gradient_color1 = (21, 87, 151)
gradient_color2 = (21, 153, 87)

draw_gradient(canvas, gradient_color1, gradient_color2)

frame_line = Frame(window, width=1000, height=15, bg=co1)
frame_line.place(relx=0.5, rely=0.01, anchor=N)  # Using place() to center the frame

frame_body = Frame(window, width=800, height=450, bg=bg_color)  # Increased width and height
frame_body.place(relx=0.5, rely=0.5, anchor=CENTER)  # Using place() to center the frame

image = "C:/Users/Kushal Sai/Downloads/alrm.png"
img = Image.open(image)
img = img.resize((300, 300))  # Increased size of the image
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=300, image=img)  # Set the height of the label to match the image height
app_image.grid(row=0, column=1, columnspan=4)  # Adjusted columnspan for centering

name = Label(frame_body, text="Alarm", height=1, font=('Ivy 18 bold'))
name.grid(row=1, column=1, columnspan=4)  # Adjusted columnspan for centering

hour = Label(frame_body, text="hour", height=1, font=('Ivy 10 bold'))
hour.grid(row=2, column=1)

c_hour = Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.grid(row=2, column=2)  # Adjusted column for centering

min = Label(frame_body, text="min", height=1, font=('Ivy 10 bold'))
min.grid(row=2, column=3)  # Adjusted column for centering

c_min = Combobox(frame_body, width=2, font=('arial 15'))
c_min['values'] = tuple(f"{i:02}" for i in range(60))
c_min.current(0)
c_min.grid(row=2, column=4)  # Adjusted column for centering

sec = Label(frame_body, text="sec", height=1, font=('Ivy 10 bold'))
sec.grid(row=2, column=5)  # Adjusted column for centering

c_sec = Combobox(frame_body, width=2, font=('arial 15'))
c_sec['values'] = tuple(f"{i:02}" for i in range(60))
c_sec.current(0)
c_sec.grid(row=2, column=6)  # Adjusted column for centering

period = Label(frame_body, text="period", height=1, font=('Ivy 10 bold'))
period.grid(row=2, column=7)  # Adjusted column for centering

c_period = Combobox(frame_body, width=3, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.grid(row=2, column=8)  # Adjusted column for centering

def activate_alarm():
    t = threading.Thread(target=alarm)
    t.start()
    
def deactivate_alarm():
    print('deactivate alarm: ', selected.get())
    mixer.music.stop()
    

selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="Activate", bg=bg2_color, command=activate_alarm, variable=selected)
rad1.grid(row=3, column=1, columnspan=4)  # Adjusted columnspan for centering

def sound_alarm():
    alaram = "C:/Users/Kushal Sai/Downloads/Project-K-BGM.mp3"
    mixer.music.load(alaram)
    mixer.music.play()
    
    rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text="deactivate", bg=bg2_color, command=deactivate_alarm, variable=selected)
    rad2.grid(row=3, column=5, columnspan=4)  # Adjusted columnspan for centering
    
    
def alarm():
    while True:
        control = 1
        print(control)
        
        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()
        
        now = datetime.now()
        
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")
        
        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a break! ")
                            sound_alarm()
        sleep(1)
        

mixer.init()

window.mainloop()
