import cv2
import tkinter as tk
from PIL import Image, ImageTk
import tensorflow as tf

# initializing window and image properties
HEIGHT = 500
WIDTH = 500
IMAGE_HEIGHT = 500
IMAGE_WIDTH = 500

# loading mnist dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

def imageShow(index, q):
    root = tk.Tk()
    # resizing image into larger image
    # img_array = cv2.resize(x_train[index], (IMAGE_HEIGHT,IMAGE_WIDTH), interpolation = cv2.INTER_AREA)


    canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT)
    canvas.pack()
    get_image_button = tk.Button(text="View Image", width=10, command=lambda: testYes(q, canvas))
    get_image_button.place(x=0, y=0)

    # img_array = q.get() 
    # img =  ImageTk.PhotoImage(image=Image.fromarray(img_array))
    # print(img_array)
    # print(img_array.size)
    # print('img', img)
    # canvas.create_image(IMAGE_HEIGHT/2,IMAGE_WIDTH/2, image=img)

    root.mainloop()


def testYes(q, canvas):
    global img
    img_array = q.get() 
    img =  ImageTk.PhotoImage(image=Image.fromarray(img_array))
    # print(list(q.queue))
    # print(img_array)
    # print(img_array.size)
    # print('img', img)
    canvas.create_image(IMAGE_HEIGHT/2,IMAGE_WIDTH/2, image=img)


# imageShow(5)