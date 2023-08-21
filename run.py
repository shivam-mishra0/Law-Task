from utils import *
from config import *


def main():
    src = ""
    url = web_url
    image_sources = extract_image_sources(url)

    if image_sources:
        print("Image sources:")
        for src in image_sources:
            print(src)
    else:
        print("Failed to fetch image sources.")
    image_url = web_url + "/"+src
    image_content = load_image_from_url(image_url)

    if image_content:
        # Save the image content to a local file
        image_path = "downloaded_image.jpg"
        with open(image_path, "wb") as f:
            f.write(image_content.getvalue())

        # Set up the Tesseract executable path for Ubuntu
        pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

        extracted_text = read_text_from_image(image_path)

        if extracted_text:
            print("Extracted text:")
            print(extracted_text)
        else:
            print("Text extraction failed.")
    else:
        print("Image loading failed.")


def getCaptcha(img):
    return img


if __name__ == "__main__":
    main()
