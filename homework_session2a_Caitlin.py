# Howework session 2a - Caitlin Decuyper

from PIL import Image
from PIL import ImageFilter
import os

# Assignment:
# Create a new folder called "processed" where all images from "raw" are stored in .png.
# They are all cropped to ratio 4:3 (or 3:4) and resized to be all the same size.

# Notice:
# 1. There are different extensions
# 2. They are all different sizes
# 3. We have portrait and landscape orientated images

# Steps
# 0. Create a new folder
# 1. Define portrait and landscape images
# 2. Figure out on which side you have to crop the image
# 3. Crop the image
# 4. Resize the image
# 5. Save it to your new folder with the new extension. That's it!


original_folder = 'K:\\PhD\\IMPRScourses\\Python\\session2a-image\\raw'
assignment_folder = 'K:\\PhD\\IMPRScourses\\Python\\session2a-image\\processed'
# create the new folder
os.mkdir(assignment_folder)

# list files in old folder
img_list = os.listdir(original_folder)

# check file sizes (to pick something between smallest and largest picture as picture size for all pictures)
img_sizes = []
for img in img_list:
    img_path = os.path.join(original_folder, img)
    img = Image.open(img_path)
    img_sizes.append(img.size)
print(max(img_sizes)) # 4246, 3184
print(min(img_sizes)) # 200, 200


# try with one picture first
    #img = 'baby.jpg' #landscape example
    #img = 'scissors.jpg'  #portrait example

for img in img_list:

    # select and open picture
    img_path = os.path.join(original_folder, img)
    img_open = Image.open(img_path)

    # keep largest possible 3:4 or 4:3 rectangle
    width = img_open.width
    height = img_open.height
    # define center of picture
    center = (width/2, height/2)
    # check what is the shortest side (portrait or landscape)
    shortest_side = min([width, height])
    # calculate what long side should be based on short side (and 4:3 ratio)
    new_longest_side =  shortest_side *(4/3)

    distance_center_short = shortest_side/2
    distance_center_long = new_longest_side/2

    # calculate coordinates of region you want to crop (Python start with 0,0 in upper left corner)
        if height < width:  # landscape (4:3)
            left_x = center[0] - distance_center_long
            left_y = center[1] - distance_center_short
            right_x = center[0] + distance_center_long
            right_y = center[1] + distance_center_short
            #reg = (left_x, left_y, right_x, right_y) # print reg to check coordinates
            img_cropped = img_open.crop((left_x, left_y, right_x, right_y))
            img_rsz = img_cropped.resize((2000, 1500))
            # save changes into new folder (as .png)
            new_image_path = os.path.join(assignment_folder, img)
            filename, extension = os.path.splitext(new_image_path)
            img_rsz.save(os.path.join(filename + '.png'), 'PNG')
        else: # portrait (3:4)
            left_x = center[0] - distance_center_short
            left_y = center[1] - distance_center_long
            right_x = center[0] + distance_center_short
            right_y = center[1] + distance_center_long
            img_cropped = img_open.crop((left_x, left_y, right_x, right_y))
            img_rsz = img_cropped.resize((1500, 2000))
            new_image_path = os.path.join(assignment_folder, img)
            filename, extension = os.path.splitext(new_image_path)
            img_rsz.save(os.path.join(filename + '.png'), 'PNG')


#check if changes worked
#img_check = Image.open(os.path.join(assignment_folder, "whistle.png"))
#img_check.show()
#print(img_check.size)


