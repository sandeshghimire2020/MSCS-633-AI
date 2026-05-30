"""
QR Code Generator
Simple app to convert URLs to QR codes
"""

import qrcode
import os
from pathlib import Path
from urllib.parse import urlparse


class QRCodeGenerator:
    """Generates QR codes from URLs"""
    
    def __init__(self, output_dir="qr_codes"):
        self.output_dir = output_dir
        # Create folder if it doesn't exist
        Path(self.output_dir).mkdir(exist_ok=True)
    
    def validate_url(self, url):
        """Check if URL is valid"""
        try:
            result = urlparse(url)
            return bool(result.scheme and result.netloc)
        except:
            return False
    
    def generate_qr_code(self, url, filename=None):
        """Generate QR code from URL"""
        
        # Check if URL is valid
        if not self.validate_url(url):
            raise ValueError(f"Invalid URL: {url}")
        
        # Create QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        
        # Convert to image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Generate filename from URL if not provided
        if filename is None:
            filename = self._make_filename(url)
        
        # Add .png if needed
        if not filename.endswith(".png"):
            filename += ".png"
        
        # Save the file
        file_path = os.path.join(self.output_dir, filename)
        img.save(file_path)
        
        return file_path
    
    def _make_filename(self, url):
        """Convert URL to safe filename"""
        # Remove protocol
        name = url.replace("https://", "").replace("http://", "")
        
        # Replace bad characters
        for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
            name = name.replace(char, "_")
        
        # Keep it short
        return name[:50]


def main():
    """Run the app"""
    print("=" * 50)
    print("QR Code Generator - Biox Systems")
    print("=" * 50)
    print()
    
    gen = QRCodeGenerator()
    
    while True:
        url = input("Enter URL (or 'quit' to exit): ").strip()
        
        if url.lower() == 'quit':
            print("Thanks for using QR Code Generator!")
            break
        
        if not url:
            print("Please enter a valid URL")
            continue
        
        try:
            path = gen.generate_qr_code(url)
            print(f"✓ QR code saved to: {path}")
            
        except ValueError as e:
            print(f"✗ Error: {e}")
            print("  (Make sure URL starts with https:// or http://)")
        except Exception as e:
            print(f"✗ Something went wrong: {e}")


if __name__ == "__main__":
    main()
