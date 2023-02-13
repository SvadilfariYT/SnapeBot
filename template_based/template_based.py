from template_based.reflections import reflect
from template_based.text_patterns import patterns
from entity_recognition import get_entities
from special_patterns import introductions
import re
import random
import memory

def templatebased_answer(user_input : str):
# Test input string for all known text patterns in pychobabble
    for pattern, responses in patterns:
        match = re.search(pattern.lower(), str(user_input).lower().strip())
        if match:
            answer = random.choice(responses)
            return answer.format(*[reflect(g.strip(",.?!")) for g in match.groups()])
    return None

def special_patterns(input : str):
    # Check for name
    matched, answer = check_for_special_pattern(input, introductions)
    if (matched):
        person, org = get_entities(input)

        memory.user_name = person

        answer = answer.format(person)
    
    return answer

def check_for_special_pattern(input : str, special_patterns):
    answer = None
    for category, pattern, responses in special_patterns:
        match = re.search(pattern.lower(), str(input).lower().strip())
        if match:
            answer = random.choice(responses)
            return match, answer 

    return False, None