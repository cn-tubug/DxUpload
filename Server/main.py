from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Set the upload directory
UPLOAD_FOLDER = 'uploads'

# Define the route for the main page
@app.route('/')
def upload_form():
    return render_template('upload.html')

# Define the route for handling file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the request has a file part
    if 'file' not in request.files:
        return redirect(url_for('upload_form'))

    # Get the uploaded file
    file = request.files['file']

    # Check if the file has a valid filename
    if file.filename == '':
        return redirect(url_for('upload_form'))

    # Save the file to the upload directory
    filename = file.filename
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    # Return a success message
    return render_template('upload_success.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

