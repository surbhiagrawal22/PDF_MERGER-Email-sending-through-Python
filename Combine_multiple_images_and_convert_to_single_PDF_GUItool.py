#!/usr/bin/env python
# coding: utf-8

# # Combining Images and converting to PDF convertor Tool

# In[ ]:


# Import necssary library, tkinter for GUI and Pillow for image handling

import tkinter as tk
from tkinter import filedialog
from PIL import Image
root=tk.Tk()

frame=tk.Frame(master=root)

# defining function to select image 1 
def select_image1():
      # Read the Image 1
      global image1
      imagepath=filedialog.askopenfilename(defaultextension='.jpg')
      image1=Image.open(imagepath)  
 
# defining function to select image 2
def select_image2():
       # Read the Image 2
      global image2
      imagepath=filedialog.askopenfilename(defaultextension='.jpg')
      image2=Image.open(imagepath)      

def Combine_Both_Images():
    global image1,image2
    #resize, first image
    image1 = image1.resize((426, 240))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
    # asking the path to save the PDF file
    filepath=filedialog.asksaveasfilename(defaultextension=".pdf")
    new_image.save(filepath)

    
lbl_description=tk.Label(master=frame,text="Combine Images and Convert to PDF file",bg="white",fg="blue",relief="raised")

btn_select_image1=tk.Button(master=frame,text=" Select Image 1 ",command=select_image1,bg="white",fg="blue",relief="raised",width=50,height=5)

btn_select_image2=tk.Button(master=frame,text=" Select Image 2 ",bg="white",fg="blue",relief="raised",width=50,height=5,command=select_image2)

btn_combine_image=tk.Button(master=frame,text=" Combine Both Images ",bg="white",fg="blue",relief="raised",width=50,height=5,command=Combine_Both_Images)


frame.pack()
lbl_description.pack()
btn_select_image1.pack()
btn_select_image2.pack()
btn_combine_image.pack()
root.mainloop()


# In[ ]:




