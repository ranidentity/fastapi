import spacy
from my_spacy_model.custom_components import create_custom_matcher

# Load the transformer-based model
nlp = spacy.load("en_core_web_trf")

# Add your custom matcher to the pipeline
nlp.add_pipe("custom_matcher", last=True)

# Save the modified model
nlp.to_disk("my_spacy_model/custom_nlp_model_trf")
print("Custom transformer model saved to 'my_spacy_model/custom_nlp_model_trf'!")