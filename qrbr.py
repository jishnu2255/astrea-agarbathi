import qrcode
import barcode
from barcode.writer import ImageWriter

# Function to generate QR Code
def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Function to generate Barcode using user-entered data
def generate_barcode(data, filename="barcode.png"):
    barcode_format = barcode.get_barcode_class("code128")
    barcode_obj = barcode_format(data, writer=ImageWriter())
    barcode_obj.save(filename.split(".")[0], options={"text": ""})
    print(f"Barcode saved as {filename}")

if __name__ == "__main__":
    print("Enter the data for QR and Barcode (press Enter twice to finish):")
    user_data = "\n".join(iter(input, ""))
    generate_qr(user_data, "qrcode.png")
    generate_barcode(user_data, "barcode.png")
