import os
import urllib.request
from flask import Flask, render_template, request, redirect, jsonify , redirect, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image , ImageFilter
from PIL import ImageEnhance
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from cleanup import remove_static_files

UPLOAD_FOLDER = 'C:/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
INPUT_FILENAME = ''

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
image, slider = None, None
colors = []
width, height = 0, 0

def refresh_parameters(image_path):
    global image, slider, hue_angle, colors, width, height
    image = load_image(image_path)
    slider = get_default_slider()
    width, height = get_image_size(image)
    colors = get_dominant_colors(image_path)
# So preview refreshes with any new change
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response
    @app.route('/', methods=['GET' , 'POST'])
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
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                resp = jsonify({'message' : 'File successfully uploaded'})
                resp.status_code = 201
                return resp
            else:
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
                resp.status_code = 400
                return resp
            if request.method == 'POST':
                for f in request.files.getlist('file_name'):
                    f = request.files['file_name']
                    f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
    return render_template ('app.js')
        @app.route('/uploaded', methods=['GET', 'POST'])
        def uploaded():
            global image, slider

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

            if original_button:
                dupe_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), 'replace')
            if download_button:
                return send_file(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), as_attachment=True)

            if enhance_button:
                slider = {key: float(request.form.get(key)) for key, value in slider.items()}
                apply_enhancers(image, os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), slider)
            if hue_button:
                hue_angle = float(request.form.get('hue_angle'))
                appliquer_hue_shift(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), hue_angle)
            if blur_button:
                appliquer_blur(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), blur_button)
            elif contour_button:
                appliquer_contour(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), contour_button)
            elif detail_button:
                appliquer_detail_button(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), detail_button)
            elif edge_enhance_button:
                appliquer_smooth(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), edge_enhance_button)
            elif edge_enhance_more_button:
                appliquer_sharpen(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), edge_enhance_more_button)
            elif emboss_button:
                appliquer_edge_enhance(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), emboss_button)
            elif find_edge_button:
                appliquer_find_edge(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), find_edge_button_button)
            elif sharpen_button:
                appliquer_sharpen(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), sharpen_button)
            elif edge_button:
                appliquer_edge(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), edge_button)
            elif smooth_button:
                appliquer_smooth(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), smooth_button)
            elif smooth_more_button:
                appliquer_edge_enhance(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), smooth_more_button)
            elif sharpen_button:
                appliquer_smooth(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), sharpen_button)

            if TRANSPOSE_button:
                flip_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), TRANSPOSE_button)
            elif TRANSVERSE_button:
                flip_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), TRANSVERSE_button)
            elif FLIP_LEFT_RIGHT_button:
                flip_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), FLIP_LEFT_RIGHT_button)
            elif FLIP_TOP_BOTTOM_button:
                flip_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), FLIP_TOP_BOTTOM_button)
            elif ROTATE_90_button:
                angle = int(request.form.get('angle'))
                rotate_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), angle)
            elif ROTATE_180_button:
                angle = int(request.form.get('angle'))
                rotate_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), angle)
            elif ROTATE_270_button:
                n_width = int(request.form.get('width'))
                n_height = int(request.form.get('height'))
                resize_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), n_width, n_height)
            if resize_button_button:
                left = int(request.form.get('left'))
                top = int(request.form.get('top'))
                right = int(request.form.get('right'))
                bottom = int(request.form.get('bottom'))
                crop_image(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME), left, top, right, bottom)
    if any([original_button, hue_button, blur_button, sharpen_button, edge_button,contour_button,
                        detail_button, smooth_button, TRANSPOSE_button,TRANSVERSE_button ,edge_enhance_button,
                    edge_enhance_more_button,emboss_button,find_edge_button,smooth_more_button,sharpen_button,
                        ROTATE_270_button,ROTATE_180_button,ROTATE_90_button,resize_button]):
                    refresh_parameters(os.path.join(UPLOAD_FOLDER, INPUT_FILENAME))
        return render_template('deuxiémeinterface.js')


