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





UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
INPUT_FILENAME = ''

app = Flask(__name__) 
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
def refresh_parameters(image_path):
    global image, slider, hue_angle, colors, width, height
    image = load_image(image_path)
    


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
@app.route('/uploaded', methods=[ 'POST', 'GET'])
#database

#...
def display():
    image.show()
def uploaded():
    global image, slider
def load_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print( " l'image est pas encore téléchargé ")

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
    return améliération_qualité
#filter

def appliquer_filtre(image_path,options):
    
    # Create image object
    image = image.open(image_path)
    image = load_image(image_path)
    
    if options == "0":
        # Applying the blur filter
        return image.filter(BLUR)
    elif  options =="1" :
        # contour
        # Applying the contour filter
        return image.filter(CONTOUR)
    elif options =="2" :
        # detail
        # Applying the detail filter
        return image.filter(DETAIL)
    elif options =="3" :
        # EDGE_ENHANCE
        # Applying the enhance filter
        return image.filter(EDGE_ENHANCE)
    elif options =="4" :
        # EDGE_ENHANCE_MORE
        # Applying the enhance more filter
        return image.filter(EDGE_ENHANCE_MORE)
    elif options =="5" :
        # EMBOSS
        # Applying the emboss filter
       return  image.filter(EMBOSS)
    elif options =="6" :
        # FIND_EDGES
        # Applying the find_edge filter
        return image.filter(FIND_EDGES)
    elif options =="7" :
        # SMOOTH
        # Applying the smooth filter
        return image.filter(SMOOTH)
    elif options =="8" :
        # SMOOTH_MORE
        # Applying the smooth more filter
        return image.filter(SMOOTH_MORE)
    elif options == "9" :
        # sharpen
        # Applying the sharpen filter
        return image.filter(SHARPEN)
# flouter une image
def flouter_image(image_path , options ):
    # Opens a image in RGB mode
    image = Image.open(image_path)
    image = load_image(image_path)
 # Blurring the image
    if options=="0":
       return image.filter(ImageFilter.GaussianBlur(4))
    elif options =="1" :
      return  image.filter(ImageFilter.BLUR)
    elif options == "2" :
       return image.filter(ImageFilter.BoxBlur(1))
  #rotation/pivoter
def retourner_image (image_path , options):
    image = Image.open(image_path)
    image = load_image(image_path)
    if options =="0" :
        # flip anti-clockwise
        return image.transpose(Image.TRANSPOSE)  
    elif options =="1" :
        # transverse
        # flip clockwise
        return image.transpose(Image.TRANSVERSE)
    elif options =="2" :
        # flip
        # flip horizontal
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    # flip_top_bottom
    elif options =="3" :
        # flip vertical
        return image.transpose(Image.FLIP_TOP_BOTTOM)
def rotation_image (image_path , options ) :
    image = Image.open(image_path)
    image =load_image(image_path)
    if options =="0" :
        # rotate by 90 degrees
        return image.transpose(Image.ROTATE_90)
    elif options == "1" :
        # rotate by 180 degrees
        return image.transpose(Image.ROTATE_180)
    elif options =="2" :
        # rotate by 270 degrees
        return image.transpose(Image.ROTATE_270)
def redimensionner_image(image_path , width ,left , top , right , bottom) :
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
    return redimensionner_image



if INPUT_FILENAME:
    if request.method == 'POST':
            # Sliders
            enhance_button = request.form.get('enhance_button')
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
    if any([ blur_button, sharpen_button,contour_button,
                    detail_button, smooth_button, TRANSPOSE_button,TRANSVERSE_button ,edge_enhance_button,
                edge_enhance_more_button,emboss_button,find_edge_button,smooth_more_button,sharpen_button,
                    ROTATE_270_button,ROTATE_180_button,ROTATE_90_button,resize_button]):
                refresh_parameters(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME))
                

if __name__ == "__main__":
    app.run(debug=True , port=5000 , host="localhost=127.0.0.1")


