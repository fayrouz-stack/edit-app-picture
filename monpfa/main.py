from fileinput import filename
import os
from urllib import request, response 
from flask import Flask,  render_template, request, redirect, jsonify , redirect, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image , ImageFilter
from PIL import ImageEnhance
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from shutil import copyfile
import colorsys
import glob
from flask_cors import CORS
from logging import FileHandler,WARNING




UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
INPUT_FILENAME = ''

app = Flask(__name__) 
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
CORS(app)

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#class data 

#......................    
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
image, slider = None, None
colors = []
width, height = 0, 0


# So preview refreshes with any new change
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response
@app.route('/upload', methods=[ 'POST'])
#database

    #......
def upload_file():
    # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
           
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
            resp.status_code = 400
            return resp       
@app.route('/uploaded', methods=[  'GET'])
#database

#...
def uploaded():
    global image, slider
def load_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print( " l'image est pas encore téléchargé ")
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
    image_contrasted.show()

    # sharpness
    # Enhance Sharpness
    curr_sharp = ImageEnhance.Sharpness(image)
    new_sharp = 8.3

    # Sharpness enhanced by a factor of 8.3
    image_sharped = curr_sharp.enhance(new_sharp)

    # shows updated image in image viewer
    image_sharped.show()
    image.save(image_path)
    return jsonify(ImageEnhance)

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
    return jsonify (image)
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
        image = image.filter(SMOOTH_MORE)
        image.save(image_path)
        image.show()
    elif options == "9" :
        # sharpen

        # Applying the sharpen filter
        image = image.filter(SHARPEN)
        image.save(image_path)
        image.show()
        image.save(image_path)
        return jsonify(image.filter)
# flouter une image
def flouter_image(image_path , options ):
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
    Image._show(image)
    #enregistrer l'image
    Image.save(image_path)
    return jsonify(image)
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
    return jsonify(image)
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
    return jsonify (image)
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
    return jsonify(image)



if INPUT_FILENAME:
    if request.method == 'POST':
            # Nav
            original_button = request.form.get('original_button')
            download_button = request.form.get('download_button')
            # Sliders
            enhance_button = request.form.get('enhance_button')
            # Hue
            hue_button = request.form.get('hue_button')
            # Filters
            blur_button = request.form.get('blur_button')
            contour_button = request.form.get('contour_button')
            detail_button = request.form.get('detail_button')
            edge_enhance_button = request.form.get('edge_enhance_button')
            edge_enhance_more_button = request.form.get('edge_enhance_more_button')
            emboss_button = request.form.get('emboss_button')
            find_edge_button = request.form.get('find_edge_button')
            smooth_button = request.form.get('smooth_button')
            smooth_more_button = request.form.get('smooth_more_button')
            sharpen_button = request.form.get('sharpen_button')
            # Retourner
            TRANSPOSE_button = request.form.get('TRANSPOSE_button')
            TRANSVERSE_button = request.form.get('TRANSVERSE_button')
            FLIP_LEFT_RIGHT_button = request.form.get('FLIP_LEFT_RIGHT_button')
            FLIP_TOP_BOTTOM_button = request.form.get('FLIP_TOP_BOTTOM_button')
            #rotate
            ROTATE_90_button = request.form.get('ROTATE_90_button')
            ROTATE_180_button = request.form.get('ROTATE_180_button')
            ROTATE_270_button = request.form.get('ROTATE_270_button')
            #redimensionner
            resize_button = request.form.get('resize_button')
    
if enhance_button:
        slider = {key: float(request.form.get(key)) for key, value in slider.items()}
        améliération_qualité(image, os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), slider)
if hue_button:
        hue_angle = float(request.form.get('hue_angle'))
        apply_hue_shift(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), hue_angle)
if blur_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), blur_button)
elif contour_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), contour_button)
elif detail_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), detail_button)
elif edge_enhance_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), edge_enhance_button)
elif edge_enhance_more_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), edge_enhance_more_button)
elif emboss_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), emboss_button)
elif find_edge_button:
       appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), find_edge_button)
elif sharpen_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), sharpen_button)
elif smooth_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), smooth_button)
elif smooth_more_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), smooth_more_button)
elif sharpen_button:
        appliquer_filtre(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), sharpen_button)

if TRANSPOSE_button:
        retourner_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), TRANSPOSE_button)
elif TRANSVERSE_button:
        retourner_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), TRANSVERSE_button)
elif FLIP_LEFT_RIGHT_button:
        retourner_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), FLIP_LEFT_RIGHT_button)
elif FLIP_TOP_BOTTOM_button:
        retourner_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), FLIP_TOP_BOTTOM_button)
if ROTATE_90_button:
        angle = int(request.form.get('angle'))
        rotation_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), angle)
elif ROTATE_180_button:
        angle = int(request.form.get('angle'))
        rotation_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), angle)
elif ROTATE_270_button:
        n_width = int(request.form.get('width'))
        n_height = int(request.form.get('height'))
        rotation_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), n_width, n_height)
if resize_button:
        left = int(request.form.get('left'))
        top = int(request.form.get('top'))
        right = int(request.form.get('right'))
        bottom = int(request.form.get('bottom'))
        redimensionner_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), left, top, right, bottom)
if __name__ == "__main__":
    
    app.run(debug=True , port=5000 , host="localhost=127.0.0.1")


