import pytesseract
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup


def extract_image_sources(url):
    try:
        response = requests.get(url, verify=False)
        print(response.text)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            image_sources = []
            for img_tag in soup.find_all('img'):
                src = img_tag.get('src')
                if src:
                    image_sources.append(src)
            print(image_sources[:1])
            return image_sources[:1]
        else:
            print(f"Failed to fetch HTML. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def read_text_from_image(image_path):
    try:
        # Open the image using Pillow
        image = Image.open(image_path)

        # Use Tesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(image)

        return extracted_text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def load_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image_content = BytesIO(response.content)
            return image_content
        else:
            print(f"Failed to load image. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_html_source(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            return html_content
        else:
            print(f"Failed to fetch HTML. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
