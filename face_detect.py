from zipfile import ZipFile
import io

from PIL import Image, ImageDraw
import pytesseract
import cv2 as cv
import numpy as np

# Section I: build database

# define function to convert image into bytes array
# image passed in is a PIL image and cv.imread expects a image path.
def cv_imgByArr(image):
  image.save("cv_{}".format(filename))
  image=cv.imread(("cv_{}".format(filename)), cv.IMREAD_GRAYSCALE)
  return image

def PIL_imgByArr(image):
  gray_image = image.convert('L')
  
  return image_BytArr


# function to check gap space
def gap_check(image, location):
  '''Checks the image in a given (x,y) location to see if it fits the description of a gap box
  :param image: A PIL.Image file
  :param location: A tuple (x,y) which is a pixel location in that image
  :return: True if that fits the definition of a gap box, otherwise False
  '''
  image = black_and_white_image(image)
  pass


# define function to create bounding box
def get_bounding_boxes(image):
  pass


# define function to detect text
def image_to_string(image):
  pass


# open zipfile and form structured data
global_lst = []

file_name = 'small_img.zip'
with ZipFile(file_name, 'r') as archive:
  # iterate through the list of zipinfo objects
  for entry in archive.infolist():
    with archive.open(entry) as file:
      image = Image.open(file)
      filename = entry.filename
      # print(image.size, image.mode, len(image.getdata()))
      # image.show()
      data_dict = {}
      data_dict['filename'] = filename
      data_dict['image'] = image
      data_dict['text'] = image_to_string(image)
      global_lst.append(data_dict)
      array = cv_imgByArr(image)
      image = Image.fromarray(array, "L")
      image.show()


# Section II: data usage--detect and display

# face detectation function

# search keyword make inference to the file

# create the contact sheet

# paste the face image in the contact sheet and show 

# loading the face detection classifier
# face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')