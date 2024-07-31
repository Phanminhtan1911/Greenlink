from flask import Flask, render_template, request, jsonify, make_response
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
    #model =  tf.keras.models.load_model("model/convnext.h5")
    model = tf.keras.models.load_model('model/new2.h5')
    # model = tf.keras.models.load_model('my_models_name.h5', custom_objects={'KerasLayer':hub.KerasLayer , 'AdamWeightDecay': optimizer})
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
    class_names = ['Cây bách hợp - Là loài cây quý hiếm', 'Cây bách xanh - Là loài cây quý hiếm','Cây cà te - Là loài cây quý hiếm','Cây giáng hương - Là loài cây quý hiếm','cayrac','Cây phi lao - Là loài cây quý hiếm"','caypomu','caythong2la','caythong5la','caythongdo','caythuytung','caytrucduiga','caytungru','khungcanh']
    #class_names = ['Có','Không']
    result = class_names[np.argmax(prediction)]
    print(prediction)
    return result
app = Flask(__name__)
model = load_model()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        # Lưu file vào thư mục trên server
        uploaded_file.save('uploads/' + uploaded_file.filename)
        return 'File đã được tải lên thành công!'
    else:
        return 'Không có file được tải lên.'


# @app.route('/upload_file', methods=['GET','POST'])
# def upload_file():
#     print(request)
#     if request.method == 'POST':
#         # if 'fileToUpload' not in request.files:
#         #     name = 'Không có file nào được tải lên.'
#         #     # return make_response(jsonify(data), 201)
#         # else:
#             if 'file' in request.files:
#                 print(request.files['file'])
            

# # # Your Base64 encoded string
# #             base64_string = request.values

# # # Decode the Base64 string, getting the binary image data
# #             image_data = base64.b64decode(base64_string)
#         #     if file.filename == '':

#         #         name = 'Không có file nào được chọn để tải lên.'
#         #         # return make_response(jsonify(data), 201)
#             file = "uploads/input.jpg"
#             name = 'Kết quả dự đoán :' + processing_uploader(file,model)

            

#             data = {'message': 'Done', 'code': 'name'}
            
#             # data = processing_uploader(file,model)
#             return make_response(jsonify(data), 201)
    
# @app.route('/create_file', methods=['GET','POST'])
# def create_file():
#     if request.method == 'POST':
#         # name=request.form.get('name')
#         file = "uploads/input.jpg"
#         name = 'Kết quả dự đoán :' + processing_uploader(file,model)

        

#         data = {'message': 'Done', 'code': name}
        
#         # data = processing_uploader(file,model)
#         return data

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True
        
    )

