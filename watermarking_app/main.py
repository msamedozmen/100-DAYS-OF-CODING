    from tkinter import *
    from tkinter import filedialog as fd
    from PIL import Image,ImageTk,ImageDraw,ImageFont
    from tkinter.filedialog import askopenfile
    import cv2
    import numpy as np

    root = Tk()

    root.withdraw()
    filename = fd.askopenfilename(initialdir="C://Users//MONSTER//Desktop",title="Select Image")
    image = Image.open(filename)
    x_cor,y_cor = image.size
    font = ImageFont.truetype("arial.ttf",50)
    ImageDraw.Draw(image).text((int(x_cor/2),int(y_cor/2)),text="Created by Samed" ,font=font,stroke_width =3,anchor="ms")
    image.show()








