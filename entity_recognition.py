import spacy
from spacy.pipeline import EntityRuler
from custom_entities import entity_patterns
import re
import memory


nlp = spacy.load("en_core_web_lg")

ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(entity_patterns)

def replace_entities(input : str, output : str):
    output_nlp = nlp(output)
    input_nlp = nlp(input)

    # Pre-Define entities
    entities = {
        "PERSON": memory.get_user_name(),
        "ORG": "Hogwarts",
        "MONEY": "galleons"
    }

    # update pre-defined entities by entities in input
    for input_ent in input_nlp.ents:
        entities[input_ent.label_] = input_ent.text

    # Entity Recognition for entities in input
    for output_ent in output_nlp.ents:
        try:
            ent = entities[output_ent.label_]
            output = re.sub(output_ent.text, ent, output)
        except KeyError:
            pass

    return output

def get_entities(input : str):
    input_nlp = nlp(input)

    person = None
    org = None
    
    # returns last entity that matched this label
    for ent in input_nlp.ents:
        if ent.label_ == "PERSON":
            person = ent.text
        elif ent.label_ == "ORG":
            org = ent.text
    return person, org

def replace_entity(output : str, ent, new_ent, label: str):
    if ent.label_ == label:
        output = re.sub(ent.text, new_ent, output)
    return output

def replace_entity_custom(output, list, entity):
    for element in list:
        if element in output:
            output = re.sub(element, entity, output)
    return output