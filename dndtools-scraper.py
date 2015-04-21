#! /bin/env python

#A nice grandma to scrape spell stat blocks from dndtools pages

#Uses html2text to pull formatted text from a spell's index page
#Expects the filename of the index page to be scraped

import html2text
import sys

if len(sys.argv) == 1:
    sys.exit("No file specified!")

spell_index = sys.argv[1]
index_file = open(spell_index)
index_html = index_file.read()
html_handler = html2text.HTML2Text()
html_handler.ignore_links = True
html_handler.ignore_images = True
html_handler.ignore_emphasis = True
index_text = (html_handler.handle(index_html)).splitlines()
spell_text = ""
begin_adding = False
#Trim out useless text first
for line in index_text:
    if begin_adding == True:
        if "* ## " in line:
            spell_text = spell_text + line[line.find("##")+3:] + "\n"
        elif "(" in line[:1] and ")" in line[:-1]:
           # print("Ommitting source material")
            spell_text = line[1:-3] + spell_text + "\n"
        elif "###" in line:
            break
        else:
            spell_text = spell_text + line + "\n"
    else:
        if "All social disabled (faster)" in line:
            begin_adding = True

print(spell_text)
