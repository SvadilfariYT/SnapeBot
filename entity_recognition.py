import spacy
import re
import memory

nlp = spacy.load("en_core_web_lg")

characters = ["Snape", "Hagrid", "Dumbledore", "Draco"]

def replace_entities(input : str, output : str):
    output_nlp = nlp(output)

    person = memory.user_name

    org = "Hogwarts"

    # Input Entities
    person_, org_ = get_entities(input)
    
    # Update if not None
    person = person_ if person_ is not None else person
    org = org_ if org_ is not None else org

    # Output Entities
    for ent in output_nlp.ents:
        output = replace_entity(output, ent, person, "PERSON")
        output = replace_entity(output, ent, org, "ORG")

    output = replace_entity_custom(output, characters, person)

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