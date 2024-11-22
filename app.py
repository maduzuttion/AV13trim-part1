from flask import Flask, render_template, request, redirect, url_for
import os

app=Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def  upload_image():
    if request.method == "POST":
        
        if 'file' not in request.files:
            return "Nenhum arquivo foi enviado!"
        file = request.files['file']
        
        
        if file.filename == '':
            return "Nenhum arquivo selecionado!"
        
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        
        return render_template("index.html", image_url=url_for('static', filename=f'uploads/{file.filename}'))
    
    return render_template("index.html", image_url=None)

if __name__ == "__main__":
    app.run(debug=True)