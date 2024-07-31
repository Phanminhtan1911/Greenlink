from flask import Flask, request, render_template
from flask import Flask, render_template, request, jsonify, make_response
import  PIL 
from PIL import Image, ImageOps
import tensorflow as tf
import numpy as np
import keras
from tensorflow.keras.preprocessing.image import img_to_array
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import base64

def load_model():
    model =  tf.keras.models.load_model("new2.h5")
    #model = tf.keras.models.load_model('model/convnext')
    #model = tf.keras.models.load_model('my_models_name.h5', custom_objects={'KerasLayer':hub.KerasLayer , 'AdamWeightDecay': optimizer})
    return model
def processing_uploader(file, model):
    inputShape = (224, 224)
    bytes_data = Image.open(file)
    image = bytes_data
    #image = tach_kenh_mau(bytes_data,'R')
    #image = image.convert("RGB")
    image = image.resize(inputShape)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image) 
    class_names = ['Cây bách hợp - Là loài cây quý hiếm',
                    'Cây bách xanh - Là loài cây quý hiếm',
                    'Cây cà te - Là loài cây quý hiếm',
                    'Cây giáng hương - Là loài cây quý hiếm',
                    'Không phải loài cây quý hiếm hoặc không có trong cơ sở dữ liệu',
                    'Cây phi lao - Là loài cây quý hiếm',
                    'Cây pơ mu - Là loài cây quý hiếm',
                    'Cây thông 2 lá - Là loài cây quý hiếm',
                    'Cây thông 5 lá - Là loài cây quý hiếm',
                    'Cây thông đỏ - Là loài cây quý hiếm',
                    'Cây thủy tùng - Là loài cây quý hiếm',
                    'Cây trúc đùi gà - Là loài cây quý hiếm',
                    'Cây tùng rủ - Là loài cây quý hiếm',
                    'Không phải cây hoặc không có trong cơ sở dữ liệu']
    result = class_names[np.argmax(prediction)]
    res = 'Kết quả dự đoán :' + result
    print(prediction)
    return res
app = Flask(__name__)
model = load_model()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        # Lưu file vào thư mục trên server
        file_dic = 'uploads/' + uploaded_file.filename
        uploaded_file.save(file_dic)
        
            
            # data = processing_uploader(file,model)
        name = processing_uploader(file_dic,model)
        print(name)
        return name
        
    else:
        name = 'Không có file được tải lên.'
        return name

if __name__ == '__main__':
    app.run(
        host='127.0.0.3',
        port=8000,
        debug=True
        
    )
