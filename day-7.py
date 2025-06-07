#This a qr code generator
#install this module , pip install "qrcode[pil]"
import qrcode
import time
import pyttsx3
engine = pyttsx3.init()

gap = time.sleep
print("QR code generator 🛠️💻")
gap(0.5)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr_data = input("Enter the text or URL for the QR Code: ")

qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
print("Genarating...", end='', flush=True)
gap(2)
print(f"\rGenarated         \r")
engine.say("Genarated")
engine.runAndWait()


filename = input("Enter file name:")
print("Saving...", end='', flush=True)
gap(1)
print(f"\rdone         \r")
img.save(filename)

print(f"✅ QR Code saved as {filename}")
engine.say(f"QR Code saved as {filename}")
engine.runAndWait()
img.show()
