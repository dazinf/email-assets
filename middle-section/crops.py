from PIL import Image

src = Image.open('middle-section/middle-section-bg.png').convert('RGBA')
W, H = src.size
S = W / 380.0
assert abs(H / S - 95) <= 1, f"unexpected panel size {W}x{H}"

def crop(name, box):
    # box = (l, t, r, b) w pikselach DISPLAY (canvas 380x100; panel na y+5)
    l, t, r, b = [int(round(v * S)) for v in box]
    pad = int(round(5 * S))
    img = src.crop((l, t - pad, r, b - pad))
    disp_w = box[2] - box[0]
    disp_h = box[3] - box[1]
    if S != 1:
        img = img.resize((disp_w, disp_h), Image.LANCZOS)
    img.save('middle-section/' + name, 'PNG', optimize=True)
    print("saved", name, img.size)

crop('middle-top-left.png',   (0, 0, 36, 22))     # 36 x 22 (5 rz. przezroczystych + panel 0-16)
crop('middle-top-right.png',  (258, 0, 380, 22)) # 122 x 22
crop('middle-side-left.png',  (0, 22, 12, 95))   # 12 x 73
crop('middle-side-right.png', (368, 22, 380, 95))# 12 x 73
crop('middle-bottom.png',    (0, 95, 380, 100))  # 380 x 5
