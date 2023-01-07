from template_based.reflections import reflect
from template_based.text_patterns import patterns
import re
import random

def templatebased_answer(user_input : str):
# Test input string for all known text patterns in pychobabble
    for pattern, responses in patterns:
        match = re.search(pattern.lower(), str(user_input).lower().strip())
        if match:
            answer = random.choice(responses)
            return answer.format(*[reflect(g.strip(",.?!")) for g in match.groups()])
    return None