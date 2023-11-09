import json

with open('movies.json', 'r', encoding='utf-8') as jsf_r:
    jsf = json.loads(jsf_r.read())

new_jsf = []
for js in jsf:
    js.update({'checked_out': False})
    new_jsf.append(js)


with open('movies_inventory.json', 'w', encoding='utf-8') as jsf_w:
    jsf_w.write(json.dumps(new_jsf))