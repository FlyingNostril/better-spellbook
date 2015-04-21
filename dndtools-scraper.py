#! /bin/env python

#A nice grandma to scrape spell stat blocks from dndtools pages

#Uses html2text to pull formatted text from a spell's index page
#Expects the filename of the index page to be scraped

import html2text
import sys

if len(sys.argv) == 1:
    sys.exit("No file specified!")

spell_index = sys.argv[1]
index_file = file.open(spell_index)
for line in index_file:
    print (line).strip()
