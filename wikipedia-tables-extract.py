import sys
import re

from bs4 import BeautifulSoup

text = sys.stdin.read()
soup = BeautifulSoup(text, 'html.parser')

bg = lambda style: style and 'background' in style

def filter_color_cells ( tag ) :

   if tag.name == 'td': return bg(tag.get('style'))

   return False

def filter_tables_and_titles ( tag ) :
   return tag.name in ['table', 'h2', 'h3']

def extract_color_from_style ( style ) :

   m = re.search('background(-color)?: *#([a-fA-F0-9]{6})', style)
   return m.group(2).lower()

tat = soup.find_all(filter_tables_and_titles)

current_title = None

for tag in tat:

   if tag.name in ['h2', 'h3']:
      try:
         current_title = tag.string
         for span in tag.find_all('span'):
            if current_title: break
            current_title = span.string
      except:
         current_title = None

   elif tag.name == 'table':
      colors = list(map(extract_color_from_style, map(lambda tag: tag.get('style'), tag.find_all(filter_color_cells))))
      if colors:
         if current_title is not None:
            slug = ''.join(filter(lambda x : 'a' <= x <= 'z' or '0' <= x <= '9' or x in '-', current_title.lower().replace(' ', '-')))
            with open('palette/{}.colors'.format(slug), 'w') as f: f.write('\n'.join(colors))
            with open('palette/{}.title'.format(slug), 'w') as f: f.write(current_title)
         else:
            print(current_title, colors)
