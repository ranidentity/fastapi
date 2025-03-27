import spacy
from my_spacy_model.custom_components import create_custom_matcher

# Load the saved transformer model
# nlp = spacy.load("my_spacy_model/custom_nlp_model_trf") 
# disable none relevant plugin for lighter weight
nlp = spacy.load("my_spacy_model/custom_nlp_model_trf", disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])
def process_conversation(input_text):
    """Process the input conversation and extract details."""
    doc = nlp(input_text)
    
    # Extract matches from your custom matcher
    buy_quantity = None
    egg_quantity = None
    price_per_egg = None
    
    for match_id, start, end in doc._.matches:
        match_label = nlp.vocab.strings[match_id]
        matched_text = doc[start:end].text
        if match_label == "BUY_PATTERN":
            buy_quantity = matched_text
        elif match_label == "QUANTITY_PATTERN":
            egg_quantity = matched_text
        elif match_label == "PRICE_PATTERN":
            price_per_egg = matched_text
    
    # Use NER from the transformer model for additional context
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    money = next((ent.text for ent in doc.ents if ent.label_ == "MONEY"), None)
    quantity = next((ent.text for ent in doc.ents if ent.label_ == "QUANTITY"), None)
    
    return {
        "buy_quantity": buy_quantity,
        "egg_quantity": egg_quantity,
        "price_per_egg": price_per_egg,
        "ner_money": money,
        "ner_quantity": quantity
    }
def generate_reply(details):
    """Generate a reply based on extracted details."""
    if details["buy_quantity"] and details["egg_quantity"]:
        return f"Sure, I can get you {details['buy_quantity']} of eggs ({details['egg_quantity']}). How would you like to proceed?"
    elif details["buy_quantity"]:
        return f"Got it, you want {details['buy_quantity']} of eggs. Any specific quantity or price in mind?"
    elif details["egg_quantity"] and details["price_per_egg"]:
        return f"You want {details['egg_quantity']} at {details['price_per_egg']}. Let me confirm availability and total cost."
    elif details["ner_quantity"] and details["ner_money"]:
        return f"Looks like you want {details['ner_quantity']} for {details['ner_money']}. Is that correct?"
    else:
        return "Could you clarify how many eggs you'd like and at what price?"
    
# Test with example conversations
conversations = [
    "I want 5 dozen eggs at 10 cents an egg.",
    "Can I get a dozen eggs?",
    "How much for 10 eggs at 50 cents each?",
    "I’d like 2 dozen for $1.20."
]

for conv in conversations:
    print(f"\nClient: {conv}")
    details = process_conversation(conv)
    reply = generate_reply(details)
    print(f"Reply: {reply}")