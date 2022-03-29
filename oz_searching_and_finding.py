import re

# import L. Frank Baum's The Wonderful Wizard of Oz
oz_text = open("wizard_of_oz.txt",encoding='utf-8').read().lower()

found_wizard = re.search("wizard", oz_text)
# search oz_text for an occurrence of 'wizard'
print(found_wizard)

all_lions = re.findall("lion", oz_text)
# find all the occurrences of 'lion' in oz_text
number_lions = len(all_lions)
print(number_lions)
