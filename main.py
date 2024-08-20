from image_converter import *
from tkinter import Tk, Frame, Label
from PIL import ImageTk

screen = Tk()
screen.title("Image Converter")
# screen.minsize(width=1250, height=750)

images = ImageConverter("test_image.jpeg")

# left_frame = Frame(screen, width=400, height=300)
# left_frame.pack()
# left_frame.place(anchor="w", relx=0.5, rely=0)
# left_image = Label(left_frame, image=images.original)
# left_image.pack()
# original_image = ImageTk.PhotoImage(images.original)
# left_image = tk.Label(screen, image=original_image)
# left_image.pack()

screen.mainloop()
