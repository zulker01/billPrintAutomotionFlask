from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    files = request.files.getlist("images")
    print("FILES RECEIVED:", len(files))
    W, H = 3508, 2480  # A4 landscape
    cols, rows = 3, 2
    margin = 50

    cell_w = (W - margin*(cols+1)) // cols
    cell_h = (H - margin*(rows+1)) // rows

    canvas = Image.new("RGB", (W, H), "white")

    for i, file in enumerate(files[:6]):
        img = Image.open(file)
        img = img.resize((cell_w, cell_h))

        x = margin + (i % cols) * (cell_w + margin)
        y = margin + (i // cols) * (cell_h + margin)

        canvas.paste(img, (x, y))

    output = io.BytesIO()
    canvas.save(output, format="PDF")
    output.seek(0)
    pdf_bytes = output.getvalue()

    print("PDF size (bytes):", len(pdf_bytes))

    output.seek(0)
    return send_file(output, mimetype="application/pdf")