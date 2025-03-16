import spacy


# Load the small English model from spacy
nlp = spacy.load("en_core_web_sm")

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



def main()-> None:
	# Test text processing function
	sample_text = "What is in this image?"
	result = process_text(sample_text)
	print(f"Input: {sample_text}")
	print(f"Output: {result}")

if __name__ == "__main__":
	main()
