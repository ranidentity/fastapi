from spacy.language import Language
from spacy.matcher import Matcher
from spacy.tokens import Doc

@Language.factory("custom_matcher", default_config={})
def create_custom_matcher(nlp, name):
    def custom_matcher(doc):
        matcher = Matcher(nlp.vocab)
        buy_pattern = [{"LIKE_NUM": True}, {"LOWER": {"IN": ["dozen", "dozens", "dz", "bunch", "some"]}}]
        quantity_pattern = [{"LIKE_NUM": True}, {"LOWER": "eggs"}]
        price_pattern = [{"LIKE_NUM": True}, {"LOWER": "cents"}, {"LOWER": "an"}, {"LOWER": "egg"}]
        matcher.add("BUY_PATTERN", [buy_pattern])
        matcher.add("QUANTITY_PATTERN", [quantity_pattern])
        matcher.add("PRICE_PATTERN", [price_pattern])
        matches = matcher(doc)
        doc._.matches = matches
        return doc
    return custom_matcher

# Register the extension
if not Doc.has_extension("matches"):
    Doc.set_extension("matches", default=[])