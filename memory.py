import random

user_names = ["wizard"]
input_count = {"questions": 0, "imperatives": 0, "pleasantries": 0}

def get_user_name():
    return random.choice(user_names)

def add_user_name(new_name : str):
    user_names.append(new_name)

def get_input_counts():
    return input_count