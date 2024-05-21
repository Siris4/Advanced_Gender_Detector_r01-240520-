import pytesseract
from PIL import Image
import gender_guesser.detector as gender
import os

# Set the Tesseract executable path if it's not in the system PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Function to extract text from an image
def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")

    # Open the image and convert it to a format compatible with pytesseract
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure the image is in RGB format

    # Extract text using pytesseract
    text = pytesseract.image_to_string(img)
    return text


# Function to predict gender from a list of names
def predict_gender(names):
    d = gender.Detector()
    gender_predictions = []
    for name in names:
        first_name = name.split()[0]
        gender_prediction = d.get_gender(first_name)
        gender_predictions.append((name, gender_prediction))
    return gender_predictions


# Function to process the extracted text and predict genders
def process_text_and_predict_gender(text):
    lines = text.split('\n')
    names = [line.strip() for line in lines if line.strip()]
    gender_predictions = predict_gender(names)
    return gender_predictions


# Main function
def main(image_path):
    # Extract text from image
    text = extract_text_from_image(image_path)
    print("Extracted Text:", text)

    # Process text and predict gender
    gender_predictions = process_text_and_predict_gender(text)
    for name, gender_prediction in gender_predictions:
        print(f"Name: {name}, Predicted Gender: {gender_prediction}")


# Example usage
if __name__ == "__main__":
    # Replace this with the actual path to your scanned image
    image_path = r"C:\Users\guber\Downloads\IMG_7141.jpg"  # Use raw string or forward slashes
    main(image_path)
