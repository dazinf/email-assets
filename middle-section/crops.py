from PIL import Image

src = Image.open('middle-section/middle-section-bg.png').convert('RGBA')
W, H = src.size
assert (W, H) == (380, 95), f"unexpected panel size {W}x{H}"
canvas = Image.new("RGBA", (W, H + 5), (0, 0, 0, 0))
canvas.paste(src, (0, 5))

def crop(name, box):
    img = canvas.crop(box)
    img.save('middle-section/' + name, 'PNG', optimize=True)
    print("saved", name, img.size)

crop('middle-top-left.png', (0, 0, 33, 22))       # 33 x 22 (5 rz. przezroczystych + panel 0-16)
crop('middle-top-right.png', (257, 0, 380, 22))  # 123 x 22
crop('middle-side-left.png', (0, 22, 12, 95))     # 12 x 73 (lewa krawedz, panel 17-89)
crop('middle-side-right.png', (368, 22, 380, 95)) # 12 x 73 (prawa krawedz, panel 17-89)
crop('middle-bottom.png', (0, 95, 380, 100))      # 380 x 5
