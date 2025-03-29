
# Using self modified model
# # Sample result
# Match: BUY_PATTERN -> '5 dozen'
# Match: PRICE_PATTERN -> '10 cents an egg'

import spacy
from my_spacy_model.custom_component import create_custom_matcher  # Import the factory

# Load the saved model
nlp = spacy.load("my_spacy_model/custom_nlp_model")

# Test the model
text = "I want 5 dozen eggs at 10 cents an egg."
doc = nlp(text)

# Access the custom matches
for match_id, start, end in doc._.matches:
    match_label = nlp.vocab.strings[match_id]
    matched_text = doc[start:end].text
    print(f"Match: {match_label} -> '{matched_text}'")