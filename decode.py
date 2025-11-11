from PIL import Image

def find_repeating_pattern(data):
    max_check_length = len(data) // 2
    
    for length in range(1, max_check_length + 1):
        
        segment_1 = data[0:length]
        segment_2 = data[length : length * 2]
        
        if segment_1 == segment_2:
            return segment_1 
            
    return None

def decode_steganography_auto(image_path):
    try:
        im = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image not found at '{image_path}'.")
        return None
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

    extracted_ascii_values = []
    width, height = im.size

    for dot_j in range(20, height, 20):
        for dot_i in range(20, width, 20):
            try:
                r, g, b = im.getpixel((dot_i, dot_j))
                extracted_ascii_values.extend([r, g, b])
            except IndexError:
                break
        else:
            continue
        break

    if not extracted_ascii_values:
        print("Error: No data was extracted. Check image and coordinates.")
        return None


    secret_values = find_repeating_pattern(extracted_ascii_values)

    if secret_values is None:
        print("Error: Could not find a repeating pattern.")
        print("This might mean the image was too small to hold the secret twice,")
        print("or the data is corrupted.")
        
        print(f"Sample of data read: {extracted_ascii_values[:50]}")
        return None

    try:
        decoded_message = ''.join(chr(val) for val in secret_values)
        return decoded_message
    except ValueError:
        print(f"Error: Found pattern but could not convert to text: {secret_values}")
        return None

image_to_decode_path = "ADDRESS_OF_YOUR_IMAGE"

print("Attempting to auto-decode message...")
decoded_secret = decode_steganography_auto(image_to_decode_path)

if decoded_secret:
    print(f"\n--- Secret message successfully extracted (Auto) ---")
    print(f"Message: {decoded_secret}")
    print(f"Length Found: {len(decoded_secret)}")
else:
    print("\n--- Message extraction failed ---")
