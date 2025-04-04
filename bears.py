from PIL import Image, ImageDraw

# Nastavení velikosti obrázku
width, height = 400, 400
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Funkce pro vykreslení medvídka
def draw_bear(x, y, color):
    """ Vykreslí medvídka na dané souřadnice """
    # Tělo
    draw.ellipse((x-50, y, x+50, y+100), fill=color, outline="black")
    # Hlava
    draw.ellipse((x-40, y-50, x+40, y+30), fill=color, outline="black")
    # Uši
    draw.ellipse((x-45, y-55, x-15, y-25), fill=color, outline="black")
    draw.ellipse((x+15, y-55, x+45, y-25), fill=color, outline="black")
    # Oči
    draw.ellipse((x-15, y-30, x-5, y-20), fill="black")
    draw.ellipse((x+5, y-30, x+15, y-20), fill="black")
    # Čumák
    draw.ellipse((x-5, y-10, x+5, y), fill="black")
    # Packy
    draw.ellipse((x-60, y+50, x-20, y+90), fill=color, outline="black")
    draw.ellipse((x+20, y+50, x+60, y+90), fill=color, outline="black")

# Funkce pro vykreslení srdíčka mezi medvídky
def draw_heart(x, y, size, color):
    """ Vykreslí srdíčko na dané souřadnice """
    draw.polygon([(x, y), (x-size, y+size), (x+size, y+size)], fill=color, outline="black")
    draw.ellipse((x-size, y-size, x, y+size), fill=color, outline="black")
    draw.ellipse((x, y-size, x+size, y+size), fill=color, outline="black")

# Vykreslení dvou medvídků
draw_bear(140, 180, "brown")  # Levý medvídek
draw_bear(260, 180, "brown")  # Pravý medvídek

# Srdíčko mezi nimi
draw_heart(200, 230, 30, "red")

# Uložení obrázku
img.save("hugging_bears.png")

# Zobrazení obrázku
img.show()

print("Obrázek dvou medvídků se srdíčkem byl vytvořen jako 'hugging_bears.png'.")
