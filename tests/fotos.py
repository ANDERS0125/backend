#convertir photos a base64
import base64

def load_photo_base64(photo_path):
    with open(photo_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def save_photo_base64(photo_base64, output_path):
    with open(output_path, "w") as text_file:
        text_file.write(photo_base64)

def main():
    photo_path = "tests/images/photo11.jpg"
    output_path = "tests/base64/photo11.txt"
    
    photo_base64 = load_photo_base64(photo_path)
    save_photo_base64(photo_base64, output_path)

if __name__ == "__main__":
    main()
