html_content = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moje první stránka</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; }
        h1 { color: #ff4081; }
    </style>
</head>
<body>
    <h1>Vítej na mojí první stránce!</h1>
    <p>Toto je webová stránka vytvořená v Pythonu.</p>
</body>
</html>
"""

# Uložení HTML souboru
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Soubor 'index.html' byl vytvořen! Otevři ho v prohlížeči.")
