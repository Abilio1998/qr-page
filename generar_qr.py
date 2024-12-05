from PIL import Image
import qrcode
import os

# Crear una carpeta para guardar los códigos QR
output_folder = "qr_con_logotipo"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Ruta del logotipo (asegúrate de tener un archivo llamado 'logotipo.png' en la misma carpeta)
logotipo_path = "LOGO.png"

# Ruta de la página HTML local
pagina_html_path = "file:///C:/ruta/completa/a/tu/archivo/qr_page_template.html"

# Cargar el logotipo
logotipo = Image.open(logotipo_path)
logotipo_size = (80, 80)  # Tamaño del logotipo (ajusta según tus necesidades)
logotipo = logotipo.resize(logotipo_size)

# Generar los QR del 1 al 100
for numero in range(1, 101):
    # Crear el código QR con la URL local que contiene el número como parámetro
    url = f"{pagina_html_path}?numero={numero}"
    
    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección de errores
        box_size=10,
        border=4,
    )
    qr.add_data(url)  # Contenido del QR: la URL
    qr.make(fit=True)

    # Crear la imagen del QR
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Agregar el logotipo al QR
    pos = (
        (qr_img.size[0] - logotipo.size[0]) // 2,
        (qr_img.size[1] - logotipo.size[1]) // 2,
    )
    qr_img.paste(logotipo, pos, mask=logotipo)

    # Guardar el QR con el número como nombre
    qr_img.save(f"{output_folder}/qr_{numero}.png")

print("Códigos QR generados y guardados en la carpeta 'qr_con_logotipo'.")
