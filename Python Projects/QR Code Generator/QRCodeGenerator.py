import qrcode

def generate_qr(data):
    qr = qrcode.make(data)
    qr.save("qr_code.png")

generate_qr("https://www.google.com")
