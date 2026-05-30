# QR Code Generator

A simple Python app that converts URLs into QR codes.

## What is this?

This app takes a URL (like https://www.google.com) and generates a QR code image that you can scan with your phone.

## How to Use

**Step 1: Install**
```bash
pip install -r requirements.txt
```

**Step 2: Run**
```bash
python3 qr_generator.py
```

**Step 3: Enter URLs**
```
Enter URL (or 'quit' to exit): https://www.google.com
✓ QR code saved to: qr_codes/www.google.com.png
```

That's it! Your QR codes are saved in the `qr_codes/` folder as PNG files.

## Requirements

- URL must start with `https://` or `http://`
- Python 3.7+

## Quick Example

```python
from qr_generator import QRCodeGenerator

gen = QRCodeGenerator()
gen.generate_qr_code("https://github.com")
```

Done!
