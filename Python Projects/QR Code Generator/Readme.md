# ⬜️⬛️QR Code Generator

## 📚 Description
The function `generate_qr` creates a QR code from a given data string (e.g., a URL) and saves it as an image file named `qr_code.png`.

---

## 📐 Function Definition

```python
import qrcode

def generate_qr(data):
    qr = qrcode.make(data)
    qr.save("qr_code.png")

generate_qr("https://www.google.com")
```
## ✅ Example Usage
```python
generate_qr("https://www.google.com")  # Generates a QR code and saves it as 'qr_code.png'
```
