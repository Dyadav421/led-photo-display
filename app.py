from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display')
def display():
    files = os.listdir(UPLOAD_FOLDER)
    image = files[-1] if files else None
    return render_template('display.html', image=image)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('image')
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return redirect('/display')

if __name__ == "__main__":
    app.run()
