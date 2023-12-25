from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
model = load_model('dog_cat_classifier_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    file = request.files['image']

    if file:
        img = image.load_img(file, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        prediction = model.predict(img_array)
        result = 'Dog' if prediction[0][0] > 0.5 else 'Cat'

        return jsonify({'prediction': result})
    else:
        return jsonify({'prediction': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)
