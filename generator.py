import qrcode
from PIL import Image, ImageDraw, ImageFont

# URL für den QR-Code
# ENTER URL HERE
url = "https://www.booklooker.de/B%C3%BCcher/Angebote/showAlluID=3117445"

# QR-Code-Objekt erstellen
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# URL zum QR-Code hinzufügen
qr.add_data(url)
qr.make(fit=True)

# QR-Code generieren
qr_img = qr.make_image(fill='black', back_color='white')
qr_width, qr_height = qr_img.size
new_img_height = qr_height + 50  # Platz für den Text
new_img = Image.new('RGB', (qr_width, new_img_height), 'white')
new_img.paste(qr_img, (0, 0))

# canvas
draw = ImageDraw.Draw(new_img)

# font
try:
    font = ImageFont.truetype("arial.ttf", 20)  # Versuche, eine TTF-Schrift zu laden
except IOError:
    font = ImageFont.load_default()  # Fallback, wenn die TTF nicht geladen wird

# Text "Scan me" unter dem QR-Code hinzufügen
text = "Scan me"
text_bbox = draw.textbbox((0, 0), text, font=font)  # Bounding Box des Textes berechnen
text_width = text_bbox[2] - text_bbox[0]  # Textbreite
text_height = text_bbox[3] - text_bbox[1]  # Texthöhe
text_position = ((qr_width - text_width) // 2, qr_height + 10)  # Zentrierung

# Text zeichnen
draw.text(text_position, text, font=font, fill='black')

# Bild speichern
new_img.save("url_qr_code_with_text.png")
