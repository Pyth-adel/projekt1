from PIL import Image, ImageDraw, ImageFont

# Nastavení rozměrů obrázku a základních parametrů
width, height = 300, 300
font_size = 30
frames = []

# Použití výchozího písma (nevyžaduje TTF soubor)
font = ImageFont.load_default()

# Vytvoření snímků GIFu
for i in range(10):
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)


    # Blikající srdce (zobrazeno nebo skryto podle indexu snímku)
    if i % 2 == 0:
        draw.polygon([(150, 100), (100, 50), (50, 100), (100, 150)], fill="red", outline="red")
        draw.ellipse((75, 50, 125, 100), fill="red", outline="red")
        draw.ellipse((125, 50, 175, 100), fill="red", outline="red")

    # Přidání textu
    text = "Miluji tě"
    draw.text((100, 200), text, font=font, fill="black")

    # Přidání obrázku do seznamu snímků
    frames.append(img)
from PIL import Image

img = Image.open("heart_16x9.avif")  # Nahraď názvem souboru
img.show()  # Zobrazí obrázek

# Uložení GIFu
frames[0].save(
    "blinking_heart.gif",
    save_all=True,
    append_images=frames[1:],
    duration=500,
    loop=0
)

print("GIF s blikajícím srdíčkem a textem 'Miluji tě' byl vytvořen jako 'blinking_heart.gif'.")
