from tkinter.ttk import *
from tkinter import *

from pygame import mixer
from datetime import datetime
from time import sleep

window=Tk()
window.title("")
window.geometry('350x150')


def sound_alarm():
    alaram="C:/Users/Kushal Sai/Downloads/Project-K-BGM.mp3"
    mixer.music.load(alaram)
    mixer.music.play()
    
    
def alarm():
    while True:
        control=1
        alarm_hour='09'
        alarm_minute='39'
        alarm_sec='00'
        alarm_period='PM'.upper()
        
        now=datetime.now()
        
        hour=now.strftime("%I")
        minute=now.strftime("%M")
        second=now.strftime("%S")
        period=now.strftime("%p")
        
        
        if control ==1:
            if alarm_period ==period:
                if alarm_hour ==hour:
                    if alarm_minute ==minute:
                        if alarm_sec == second:
                            print("Time to take a break! ")
                            sound_alarm()
        sleep(1)

        
                            
        
        
    
    
mixer.init()
alarm()

window.mainloop()

