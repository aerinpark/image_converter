from image_converter import *
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

FONT = ("Times", 20, "bold")
screen = Tk()
screen.title("Image Converter")
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
screen.geometry("%dx%d" % (screen_width, screen_height))

image_converter = ImageConverter()

left_image = Label(screen, text="LEFT IMAGE", width=int(screen_width/2), height=int(screen_width/2))
left_image.place(relx=0.02, rely=0.1)

right_image = Label(screen, width=int(screen_width / 2), height=int(screen_height / 2))
right_image.place(relx=0.5, rely=0.1)


def open_file():
	global left_image, img, image_converter
	path = filedialog.askopenfilename(
		title="Select an image file",
		initialdir="/image_converter/images",
		filetypes=[('Image Files', ('.jpeg', '.jpg', '.png', '.bmp', '.webp'))])
	if path:
		path = path.replace('\\', '/')
		image_original = Image.open(path)
		image_original = image_original.resize((int(image_original.width / 3), int(image_original.height / 3)))
		img = ImageTk.PhotoImage(image_original)
		left_image = Label(screen, image=img, width=int(screen_width / 2), height=int(screen_height / 2))
		left_image.place(relx=0.02, rely=0.1)
		image_converter = ImageConverter(path)
	
	
btn_image_change = Button(text="SELECT FILE", font=FONT, padx=5, pady=5, command=open_file)
btn_image_change.place(relx=0.1, rely=0.75)


def grayscale():
	global image_converter, right_image, img_new
	gray_image = image_converter.gray_scale()
	gray_image = gray_image.resize((int(gray_image.width / 3), int(gray_image.height / 3)))
	img_new = ImageTk.PhotoImage(gray_image)
	right_image.configure(image=img_new)
	right_image.place(relx=0.5, rely=0.1)


btn_grey = Button(text="GRAYSCALE", font=FONT, padx=5, pady=5, command=grayscale)
btn_grey.place(relx=0.31, rely=0.75)


def dithering():
	global image_converter, right_image, img_new
	dither_image = image_converter.dithering()
	dither_image = dither_image.resize((int(dither_image.width / 3), int(dither_image.height / 3)))
	img_new = ImageTk.PhotoImage(dither_image)
	right_image.configure(image=img_new)
	right_image.image = img_new
	right_image.place(relx=0.5, rely=0.1)


btn_dither = Button(text="DITHERING", font=FONT, padx=5, pady=5, command=dithering)
btn_dither.place(relx=0.52, rely=0.75)


def autoscale():
	global image_converter, right_image, img_new
	auto_level = image_converter.auto_level()
	auto_level = auto_level.resize((int(auto_level.width / 3), int(auto_level.height / 3)))
	img_new = ImageTk.PhotoImage(auto_level)
	right_image.configure(image=img_new)
	right_image.image = img_new
	right_image.place(relx=0.5, rely=0.1)
	
	
btn_auto = Button(text="AUTOSCALE", font=FONT, padx=5, pady=5, command=autoscale)
btn_auto.place(relx=0.73, rely=0.75)

screen.mainloop()
