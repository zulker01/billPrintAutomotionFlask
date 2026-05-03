from PIL import Image
import os

W, H = 3508, 2480  # A4 landscape

cols, rows = 3, 2
margin = 50  # reduce gap

cell_w = (W - margin*(cols+1)) // cols
cell_h = (H - margin*(rows+1)) // rows

files = [f for f in os.listdir() if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
files = sorted(files)[:6]

canvas = Image.new("RGB", (W, H), "white")

for i, file in enumerate(files):
    img = Image.open(file)

    # 🔥 stretch to fill
    img = img.resize((cell_w, cell_h))

    col = i % cols
    row = i // cols

    x = margin + col*(cell_w + margin)
    y = margin + row*(cell_h + margin)

    canvas.paste(img, (x, y))

canvas.save("output_a4.jpg")