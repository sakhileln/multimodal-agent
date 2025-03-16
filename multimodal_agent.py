import cv2
import numpy as np
import spacy
from tensorflow.keras.applications.mobilenet import (
	MobileNet,
	preprocess_input,
	decode_predictions,
)


# Load the small English model from spacy
nlp = spacy.load("en_core_web_sm")

# Load MobileNet model for image processing
mobilenet_model = MobileNet(weights="imagenet")


def process_text(text_input: str)->dict:
	"""
	Process text input using spaCy to extract intent or keywords.

	Args:
		text_input (str): The user-provided text
		(e.g "What is this image?")

	Returns:
		dict: A dictionary with extracted intent and keywords.
	"""
	# Process text with spaCy
	doc = nlp(text_input.lower())

	# Simple intent detection besed on keywords
	intent = "unkown"
	keywords = []

	for token in doc:
		# Basic intent detection: look for questuin words or key verbs
		if token.text in ["what", "describe"]:
			intent = "describe"
		elif token.text in ["classify", "identify"]:
			intent = "classify"
		# Collect nouns as keywords
		if token.pos_ == "NOUN":
			keywords.append(token.text)

	# Default intent if none detected
	if intent == "unkown" and keywords:
		intent = "describe" # Fallback to describe if nouns are present

	return {
		"intent": intent,
		"keywords": keywords,
	}


def process_image(image_path: str)-> str:
	"""
	Process an image using MobileNet to classify its content.

	Args:
		image_path (str): Path to the local image file
		(e.g "dog.jpg")
	Returns:
		str: The top predicted label for the image content.
	"""
	# Load and preprocess the image
	img = cv2.imread(image_path)
	if img is None:
		raise ValueError(f"Could not load image at {image_path}")

	# Resize to MobileNet's expected input size (224x224)
	img = cv2.resize(img, (224, 224))
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR to RGB
	img = np.expand_dims(img, axis=0) # add batch dimension
	img = preprocess_input(img) # Preprocess for MobileNet

	# Run prediction
	preds = mobilenet_model.predict(img)
	decoded_preds = decode_predictions(preds, top=1)[0] # Top prediction

	# Return the label (e.g "dog")
	label = decoded_preds[0][1]
	return label


def generate_response(text_input: str, image_path: str)-> str:
	"""
	Generate a coherent respinse by combining text and image processing.

	Args:
		text_input (str): The user-provided text prompt.
		image_path (str): Path to the local image file.

	Returns:
		str: A text response combining text intent and image content.
	"""
	# Process text to get intent and keywords
	text_result = process_text(text_input)
	intent = text_result["intent"]
	keywords = text_result["keywords"]

	# Process image to get the label
	image_label = process_image(image_path)

	# Generate response based on intent
	if intent == "describe":
		if "image" in keywords pr "this" in text_input.lower():
			return f"This image shows a {image_label}."
		return f"This is a {image_label}."
	elif intent == "classify":
		return f"The object is classified as a {image_label}."
	else:
		return f"I see a {image_label} in the image."


def main()-> None:
	# Test text processing function
	sample_text = "What is in this image?"
	result = process_text(sample_text)
	print(f"Input: {sample_text}")
	print(f"Output: {result}")

	# Test image processing
	sample_image = "sample_images/dog.jpg" # Make sure you have dog.jog in sample_images/
	try:
		image_result = process_image(sample_image)
		print(f"Image Input: {sample_image}")
		print(f"Image Ouput: {image_result}")
	except Exception as e:
		print(f"Error processing image: {e}")
		

if __name__ == "__main__":
	main()
