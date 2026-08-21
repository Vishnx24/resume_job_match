import spacy

nlp=spacy.load("en_core_web_sm")

def extract_entities(text):
    doc=nlp(text)
    entities=[]
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label":ent.label_
        })

    return entities

def get_person_name(text):

    doc = nlp(text)

    for ent in doc.ents:

        if ent.label_ == "PERSON":
            return ent.text

    return "Not detected"