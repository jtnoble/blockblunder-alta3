'''
This was made to grab all the genres and give me an html string to pop into the search.html file
'''

import json

with open('movies.json', 'r', encoding='utf-8') as jsf_r:
    jsf = json.loads(jsf_r.read())


genres = []
for data in jsf:
    for genre in data.get('genres'):
        if not genre in genres:
            genres.append(genre)
genres.sort()

for genre in genres:
    print(f'<option value="{genre}">{genre}</option>')
