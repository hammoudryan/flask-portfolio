from flask import Flask, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = picFolder

#name portfolio?
@app.route('/')
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'1.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'2.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'],'3.jpg')

    return render_template("index.html", user_image = [pic1,pic2,pic3])

if __name__ == "__main__":
    app.run(debug=True)
