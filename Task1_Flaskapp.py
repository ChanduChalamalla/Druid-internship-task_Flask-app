#importing recquired libraries
from flask import Flask, request, jsonify
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route("/convert", methods=["POST"])
def convert():
    files = request.files.getlist("file")
    #raising error message if file limit exceeds more than 5
    if len(files) > 5:
        return jsonify({"error": "Too many files. Maximum limit is 5."}), 400
    
    results = []
    for file in files:
        #loading image
        image = Image.open(file)
        #extracting text form the image using pytesseract
        text = pytesseract.image_to_string(image)
        results.append(text)
    
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run()
