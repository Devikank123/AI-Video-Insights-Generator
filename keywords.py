import spacy
# keyword extraction
# grammar analysis
# entity detection
nlp=spacy.load("en_core_web_sm")
# pretrained model used for extracting the keywords
def extract_keywords(text):
    doc=nlp(text)

# A structured object containing:
# tokens (words)
# POS tags
# syntax
    keyword=[]
# to add the extracted keywords
    for token in doc:
        if token.pos_ in ["NOUN","PROPN"]:
            # token.pos_ method is used for finding the part of speech like noun,pronoun etc..
            # filters keywords based onnoun and pronoun
            keyword.append(token.text)

    return list(set(keyword))[:10]
# Input Text
#    ↓
# spaCy Processing
#    ↓
# Tokenization
#    ↓
# POS Tagging
#    ↓
# Filter Nouns & Proper Nouns
#    ↓
# Remove duplicates
#    ↓
# Return top 10 keywords