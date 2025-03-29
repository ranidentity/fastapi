
buy_pattern = [
    {"LOWER": {"IN":["buy","grab","get"]}},
    {"LIKE_NUM": True},
    {"LEMMA": "egg"}
]

quantity_pattern = [
    {"LIKE_NUM": True},
    {"LOWER": {"IN": ["dozen", "dozens"]}},
]

price_pattern = [
    {"LIKE_NUM": True},
    {"LOWER": {"IN": ["cents", "bucks", "dough", "per", "$"]}, "OP": "?"},  # Optional price unit or connector    # {"LEMMA": "egg", "OP": "?"},
    {"LOWER": {"IN": ["egg", "unit"]}, "OP": "?"},  # Optional item or slang like "pop"
    {"IS_PUNCT": True, "OP": "?"},  # Optional punctuation (e.g., "0.20")
    {"LIKE_NUM": True, "OP": "?"},  # Optional decimal part (e.g., "0.20")
]