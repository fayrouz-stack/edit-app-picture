from PIL import Image, ImageFilter, ImageEnhance
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from shutil import copyfile
import colorsys
def load_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print('image est pas encore téléchargé')
def dupe_image(image_path, options):
    if options == 'copy':
        copyfile(image_path, image_path + '.copy')
    elif options == 'replace':
        copyfile(image_path + '.copy', image_path)
def get_default_slider():
    return {'color': 1, 'bright': 1, 'contrast': 1, 'sharp': 1}
def get_image_size(image):
    return image.width, image.height
#brightness
def améliération_qualité(image, image_path):
    # Opens the image file
    image = Image.open(image_path)
    # charger l'image
    image = load_image(image_path)
    # shows image in image viewer
    image.show()
    # Enhance Sharpness
    curr_sharp = ImageEnhance.Sharpness(image)
    new_sharp: float = 8.3

    # Sharpness enhanced by a factor of 8.3
    image_sharped = curr_sharp.enhance(new_sharp)

    # shows updated image in image viewer
    image_sharped.show()

    # color
    # Enhance Color Level
    curr_col = ImageEnhance.Color(image)
    new_col = 2.5

    # Color level enhanced by a factor of 2.5
    image_colored = curr_col.enhance(new_col)
    # shows updated image in image viewer
    image_colored.show()

    # contrast
    # Enhance Contrast
    curr_con = ImageEnhance.Contrast(image)
    new_con = 0.3

    # Contrast enhanced by a factor of 0.3
    image_contrasted = curr_con.enhance(new_con)

    # shows updated image in image viewer
    image-contrasted-contrasted.show()

    # sharpness
    # Enhance Sharpness
    curr_sharp = ImageEnhance.Sharpness(image)
    new_sharp = 8.3

    # Sharpness enhanced by a factor of 8.3
    image_sharped_sharped = curr_sharp.enhance(new_sharp)

    # shows updated image in image viewer
    image_sharped.show()
    image.save(image_path)

# HUE [ inspired by: https://stackoverflow.com/questions/24874765 ]
def get_dominant_colors(image_path, colors_count=5):
    image = load_image(image_path)
    width, height = get_image_size(image)
    colors = image.getcolors(maxcolors=width * height)
    return sorted(colors, reverse=True)[:colors_count]
def apply_hue_shift(image_path, hue_angle):
    image = load_image(image_path)
    image = image.convert('RGB')
    width, height = get_image_size(image)
    ld = image.load()

    for i in range(width):
        for j in range(height):
            r, g, b = ld[i, j]
            h, s, v = colorsys.rgb_to_hsv(r/255., g/255., b/255.)
            h = (h + hue_angle/360.0) % 1.0
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            ld[i, j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
    image.save(image_path)
#filter
def appliquer_filtre(image_path,options):
    
    # Create image object
    image = image.open(image_path)
    image = load_image(image_path)
    
    if options == "0":
        # Applying the blur filter
        image = image.filter(BLUR)
        image.save(image_path)
        image.show()
    elif  options =="1" :
        # contour
        # Applying the contour filter
        image = image.filter(CONTOUR)
        image.save(image_path)
        image.show()
    elif options =="2" :
        # detail

        # Applying the detail filter
        image = image.filter(DETAIL)
        image.save(image_path)
        image.show()
    elif options =="3" :
        # EDGE_ENHANCE

        # Applying the enhance filter
        image = image.filter(EDGE_ENHANCE)
        image.save(image_path)
        image.show()
    elif options =="4" :
        # EDGE_ENHANCE_MORE

        # Applying the enhance more filter
        image = image.filter(EDGE_ENHANCE_MORE)
        image.save(image_path)
        image.show()
    elif options =="5" :
        # EMBOSS

        # Applying the emboss filter
        image = image.filter(EMBOSS)
        image.save(image_path)
        image.show()
    elif options =="6" :
        # FIND_EDGES
        # Applying the find_edge filter
        image = image.filter(FIND_EDGES)
        image.save(image_path)
        image.show()
    elif options =="7" :
        # SMOOTH
        # Applying the smooth filter
        image = image.filter(SMOOTH)
        image.save(image_path)
        image.show()
    elif options =="8" :
        # SMOOTH_MORE

        # Applying the smooth more filter
        image = imaage.filter(SMOOTH_MORE)
        image.save(image_path)
        image.show()
    elif options == "9" :
        # sharpen

        # Applying the sharpen filter
        image = image.filter(SHARPEN)
        image.save(image_path)
        image.show()
        image.save(image_path)
# flouter une image
def flouter_image(image_path , options() ):
    # Opens a image in RGB mode
    image = Image.open(image_path)
    image = load_image(image_path)
 # Blurring the image
if options=="0":
    image.filter(ImageFilter.GaussianBlur(4))
elif options =="1" :
    image.filter(ImageFilter.BLUR)
elif options == "2" :
    image.filter(ImageFilter.BoxBlur(1))

# Shows the image in image viewer
image.show()
#enregistrer l'image
image.save(image_path)

  #rotation/pivoter
def retourner_image (image_path , options):
    image = Image.open(image_path)
    image = load_image(image_path)
if options =="0" :
    # flip anti-clockwise
    flip_image = image.transpose(Image.TRANSPOSE)
    flip_image.show()
    image = Image.save(image_path)
elif options =="1" :
    # transverse
    # flip clockwise
    flip_image = image.transpose(Image.TRANSVERSE)
    flip_image.show()
elif options =="2" :
    # flip

    # flip horizontal
    flip_image = image.transpose(Image.FLIP_LEFT_RIGHT)

    flip_image.show()
    # flip_top_bottom
elif options =="3" :
    # flip vertical
    flip_image = image.transpose(Image.FLIP_TOP_BOTTOM)

    flip_image.show()
image.save(image_path)
def rotation_image (image_path , options ) :
    image = Image.open(image_path)
    image =load_image(image_path)
if options =="0" :
    # rotate by 90 degrees
    rot_image = image.transpose(Image.ROTATE_90)
    rot_image.show()
elif options == "1" :
    # rotate by 180 degrees
    rot_image = image.transpose(Image.ROTATE_180)
    rot_image.show()
elif options =="2" :
    # rotate by 270 degrees
    rot_image = image.transpose(Image.ROTATE_270)

    rot_image.show()
image.save(image_path)
def redimensionner_image(image_path ,left , top , right , bottom) :
    image = Image.open(image_path)
    load_image= (image_path)
    width, height = image.size

    left = 4
    top = height / 5
    right = 154
    bottom = 3 * height / 5

    image = image.crop((left, top, right, bottom))
    newsize = (300, 300)
    image = image.resize(newsize)
    image.show()
    image.save(image_path)