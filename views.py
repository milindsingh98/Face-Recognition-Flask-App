from flask import render_template , request
from flask import redirect , url_for
import os
from PIL import Image
from utils import pipeline_model


UPLOAD_FOLDER = 'static/uploads'


def base():
    return render_template('base.html')

def index():
    return render_template('index.html')


def faceapp():
    return render_template('faceapp.html')

def getwidth(path):
    img = Image.open(path)
    size = img.size
    aspect = size[0]/size[1]
    w = 300 * aspect
    return int(w)


def gender():
    if request.method == 'POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER , filename)
        f.save(path)
        # Processing
        w = getwidth(path)
        # Prediction (pass to pipeline model)
        #pipeline_model(path , filename , color='bgr')
        return render_template('gender.html' , fileupload = True, img_name = filename , w = w)
    return render_template('gender.html' ,fileupload = False , img_name = 'NoImage', w = 300)
