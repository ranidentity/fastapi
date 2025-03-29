import spacy
from my_spacy_model.custom_component import create_custom_matcher  # Import the factory

# Load the base model, add the custom component, and save
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("custom_matcher", last=True)
nlp.to_disk("my_spacy_model/custom_nlp_model")
print("Custom model saved to 'my_spacy_model/custom_nlp_model'!")

#RUN spacy_usecase.py for testing