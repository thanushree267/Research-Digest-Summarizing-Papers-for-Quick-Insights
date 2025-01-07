from flask import Flask, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for uploading a research paper
@app.route('/')
def index():
    return render_template('upload.html')

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        summary = "Your summarized paper goes here."  # You would process the file and generate a summary
        return render_template('summary.html', summary=summary)

# Route for downloading summary as DOCX
@app.route('/download/docx')
def download_docx():
    summary = request.args.get('summary', '')
    # Logic to create and return a DOCX file
    return send_file('path/to/generated/docx', as_attachment=True)

# Route for downloading summary as PDF
@app.route('/download/pdf')
def download_pdf():
    summary = request.args.get('summary', '')
    # Logic to create and return a PDF file
    return send_file('path/to/generated/pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
