# PixelVault: A Python Steganography Tool

![A visual representation of data hidden in pixels]


PixelVault is a simple command-line steganography tool written in Python. It uses the LSB (Least Significant Bit) method—*Correction: It uses a direct pixel-overwrite method*—to hide a repeating secret message directly within the pixel data of an image.

This project consists of two main scripts:
* `encode.py`: Hides the secret message in a source image.
* `decode.py`: Automatically extracts the hidden message from the modified image.

## ⚠️ Important Note
This tool is **not** cryptographically secure and is intended for educational purposes only. The hidden data is not encrypted and can be easily detected with simple analysis.

## Requirements

Before you begin, ensure you have the required library installed:

```bash
pip install Pillow
```

# How to Use

## 1. Encoding (Hiding the Message)
The `encode.py` script reads a source image, embeds your secret message, and saves a new `.png` file.

**Why PNG?** This script requires a lossless format like PNG. Using `.jpg` will corrupt the data due to its lossy compression.

To run:

1. Place your source image (e.g., `source.jpg`) in the project folder.

2. Open `encode.py` and change the `secret_message` variable to your desired secret.

3. Run the script:

   ```bash
   python encode.py


## 2. Decoding (Finding the Message)
The `decode.py` script reads the `modified_image.png` file, analyzes the pixel data to find a repeating pattern, and prints the secret.

To run:

`python decode.py`

**Example Output:**
```
textAttempting to auto-decode message...

--- Secret message successfully extracted (Auto) ---
Message: My_name_is_hasan_shahroodi
Length Found: 26
```

# How It Works
This tool does not use traditional LSB steganography. Instead, it employs a more direct (and more visible) method:

* Encoder: It iterates through the image pixels at a 20x20 interval, starting at (20, 20). It overwrites the entire R, G, and B values of that pixel with the ASCII values of the secret message. The message is repeated infinitely to fill all available pixels.
* Decoder: It reads the exact same pixels, collecting all the R, G, and B values into a long list. It then analyzes this list to find the first sequence that repeats itself. This repeating sequence is the original secret message.
