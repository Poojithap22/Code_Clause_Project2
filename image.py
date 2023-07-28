from tkinter import *
window=Tk()
window.title('add image')
window=Canvas(window, width=450, height=450)
window.pack()
image=PhotoImage(file="C:/Users/Kushal Sai/Downloads/alrm.png")
window.create_image(0,0, anchor=NW, image=image)

window.mainloop()
