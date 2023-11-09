from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    # request.url('/api/inventory/json')
    return render_template('index.html', movies=json_dump())

@app.route('/api/inventory')
def inventory():
    return render_template('full_inventory.html', movies=json_dump())

@app.route('/api/inventory/json')
def json_dump():
    try:
        with open('movies_inventory.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())

        decade = request.args.get('decade')
        genre = request.args.get('genre')
        query = request.args.get('query')
        if decade:
            if decade.isnumeric() and 1899 < int(decade) < 2050:
                new_data = []
                for d in data:
                    if int(decade) <= int(d.get('year')) <= int(decade) + 9:
                        new_data.append(d)
                data = new_data
        if genre:
            new_data = []
            for d in data:
                for d_genre in d.get('genres'):
                    if d_genre.lower() == genre.lower():
                        new_data.append(d)
                        break
            data = new_data
        if query:
            new_data = []
            for d in data:
                if query.lower() in d.get('title').lower():
                    new_data.append(d)
            data = new_data
        return data
    except FileNotFoundError:
        return "JSON file not found!", 404
    except json.JSONDecodeError:
        return "Invalid JSON data!", 500

@app.route('/api/inventory/checkout', methods=["POST"])
def checkout():
    return "Checked Out!"

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()