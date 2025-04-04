from PIL import Image, ImageDraw, ImageFont
import os

# Nastavení rozměrů obrázku a základních parametrů
width, height = 300, 300
font_size = 30
frames = []

# Zkontrolujte, zda máte vhodné písmo
font_path = "arial.ttf"  # Můžete nahradit cestou k jinému TTF souboru
if not os.path.exists(font_path):
    raise FileNotFoundError("Prosím, stáhněte a umístěte soubor 'arial.ttf' do stejné složky jako tento skript.")

font = ImageFont.truetype(font_path, font_size)

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
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = 200
    draw.text((text_x, text_y), text, font=font, fill="black")

    # Přidání obrázku do seznamu snímků
    frames.append(img)

# Uložení GIFu
frames[0].save(
    "blinking_heart.gif",
    save_all=True,
    append_images=frames[1:],
    duration=500,  # Doba trvání jednoho snímku v milisekundách
    loop=0  # Nekonečná smyčka
)

print("GIF s blikajícím srdíčkem a textem 'Miluji tě' byl vytvořen jako 'blinking_heart.gif'.")