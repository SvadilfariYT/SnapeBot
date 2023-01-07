#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import pandas as pd
import re
import requests as req
import unicodedata

movie_urls = ["Harry_Potter_and_the_Philosopher%27s_Stone",
              "Harry_Potter_and_the_Chamber_of_Secrets",
              "Harry_Potter_and_the_Prisoner_of_Azkaban",
              "Harry_Potter_and_the_Deathly_Hallows_–_Part_2"]

question_and_answers = {}

def extract_speaking_parts(web_data):
    content = web_data.find(id="content")
    speaking_parts = []
    for speaker in content.find_all("b"):
        # clean text
        text_cleaned = re.sub("([\(\[]).*?([\)\]])", "", speaker.parent.text)  # remove stage directions
        # Unicode -> Ascii
        #text_cleaned = unicodedata.normalize('NFKD', text_cleaned).encode('ascii','ignore')

        text_cleaned = text_cleaned.replace("\u2013", "-").replace("\u2014", "-").replace("\u2019", "'").replace("\u2018", "'").replace("\u00a0", " ").replace("\u00be", "3/4").replace("\n", "").replace("\u2013", "-")

        speaking_parts.append(text_cleaned)
    assemble_dict(speaking_parts)

def extract_speaking_parts_billoSeite(web_data):
    characterName = "snape".upper()
    regex = "<b> {29}SNAPE\n<\/b>(.|\n)*?<b>"

    matched = re.findall("<b> {29}SNAPE\n<\/b>(.|\n)*?<b>", web_data)
    # matched = re.findall("(.|\n)*?", web_data)
    # matched.split("\n")
    return matched

def assemble_dict(parts):
    character_name ="Harry:"

    for line_index, line in enumerate(parts):
        index = line.find(character_name)
        if index == 0:
            previous_line = parts[line_index - 1]
            previous_line_text = previous_line[previous_line.find(":") + 1:]
            question_and_answers[previous_line_text] = line[len(character_name):]

# MAIN METHOD
if __name__ == '__main__':
    # requesting website
    for movie in movie_urls:
        transcript = req.get('https://warnerbros.fandom.com/wiki/' + movie + '/Transcript')
        soup = BeautifulSoup(transcript.text, "html.parser")
        extract_speaking_parts(soup)

    data = pd.DataFrame(question_and_answers.items(), columns=["questions", "answers"])
    print(data)
    data.to_json("./data.json")

    # text = open('text.txt', 'r').read()
    # print(extract_speaking_parts_billoSeite(text))

