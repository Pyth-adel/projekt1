from PIL import Image, ImageDraw
import math

# Nastavení rozměrů obrázku
width, height = 300, 300
frames = 20  # Počet snímků v GIFu

# Funkce pro vykreslení srdce
def draw_heart(draw, t, color):
    """ Vykreslí srdce pomocí parametrické rovnice """
    scale = 15
    points = [(width//2 + scale * 16 * math.sin(i) ** 3,
               height//2 - scale * (13 * math.cos(i) - 5 * math.cos(2 * i) - 2 * math.cos(3 * i) - math.cos(4 * i)))
              for i in [x * 0.1 for x in range(0, 63)]]
    draw.polygon(points, fill=color, outline="black")

# Vytvoření snímků GIFu
image_frames = []
for i in range(frames):
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # Plynulá změna barvy srdce (od červené k růžové a zpět)
    r = int(255 * (0.5 + 0.5 * math.sin(i / frames * 2 * math.pi)))
    g = int(50 + 100 * (0.5 + 0.5 * math.sin(i / frames * 2 * math.pi)))
    b = int(50 + 150 * (0.5 + 0.5 * math.sin(i / frames * 2 * math.pi)))
    heart_color = (r, g, b)

    # Vykreslení srdce
    draw_heart(draw, i, heart_color)

    image_frames.append(img)

# Uložení GIFu
image_frames[0].save(
    "beautiful_heart.gif",
    save_all=True,
    append_images=image_frames[1:],
    duration=100,  # Rychlost animace (ms)
    loop=0
)

print("GIF s krásným srdcem byl vytvořen jako 'beautiful_heart.gif'.")
