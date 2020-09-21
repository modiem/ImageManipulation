# import all liberies
import PIL
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageEnhance
from PIL import ImageFilter

# read image and convert to RGB
image=Image.open("mybest.JPG")
image=image.convert('RGB')



# split the image into bands and apply different intensity to each band
# put modified pic into a list
bands = image.split()
images = []
intensity = [0.1, 0.5, 0.9]

for count in range(len(bands)):
  for intens in intensity:
    bands_new = list(bands)
    bands_new[count] = bands_new[count].point(lambda i: i * intens)
    image = Image.merge('RGB', tuple(bands_new))

    # draw black box as background
    drawing_object = ImageDraw.Draw(image)
    drawing_object.rectangle((0, int(image.height)-150, int(image.width),int(image.height)), fill="black")
    
    # write description with designated font
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Apple Chancery.ttf", 100)
    drawing_object.text((20,int(image.height)-140), "channel {} intensity {}".format(count,intens), font=font)
    
    images.append(image)


#create a contact sheet
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width*3, first_image.height*3))
x = 0
y = 0


for img in images:
  contact_sheet.paste(img, (x, y))
  if x+first_image.width == contact_sheet.width:
    x = 0
    y += first_image.height
  else:
    x += first_image.width

#resize and display the contact sheet
contact_sheet = contact_sheet.resize( (int(contact_sheet.width/2), int(contact_sheet.height/2)) )
contact_sheet.show()

   
    



