from flask import Flask, render_template, request, jsonify
from flask_paginate import Pagination
import json

app = Flask(__name__)

@app.route('/')
def index():
    '''Main index: return first 100 items of movies_inventory.json to the user in table format
        Allows for searching in the top right, as well as a few buttons for detailed searches'''
    data = get_json_api()
    
    page = request.args.get('page', 1, type=int)
    items_per_page = 100

    decade = request.args.get('decade')
    genre = request.args.get('genre')
    query = request.args.get('query')
    filtered_data = filter_movies(data, decade, genre, query)

    # Paginate the filtered data
    pagination = Pagination(page=page, total=len(filtered_data), per_page=items_per_page, record_name='movies')
    start = (page - 1) * items_per_page
    end = start + items_per_page
    paginated_data = filtered_data[start:end]
    return render_template('index.html', movies=paginated_data, pagination=pagination)

@app.route('/search')
def search():
    '''Renders the detailed search template (separate from search in top right)'''
    return render_template('search.html')

@app.route('/api/inventory')
def inventory():
    '''Easier to read full table of what json_dump() returns'''
    return render_template('full_inventory.html', movies=json_dump())

@app.route('/api/inventory/json')
def json_dump():
    '''JSON data returned from movies_inventory.json with query parameters enabled'''
    data = get_json_api()
    decade = request.args.get('decade')
    genre = request.args.get('genre')
    query = request.args.get('query')
    return filter_movies(data, decade, genre, query)

@app.route('/api/inventory/checkout', methods=["POST"])
def checkout():
    '''POST: Checkout a movie, change its checked_out value between true and false'''
    data_list = get_json_api()
    data = request.get_json()
    target_id = data.get('id')

    for item in data_list:
        if item['id'] == target_id:
            if item['checked_out'] == True:
                item['checked_out'] = False
            elif item['checked_out'] == False:
                item['checked_out'] = True
            break

    try:
        with open('movies_inventory.json', 'w', encoding='utf-8') as f_write:
            json.dump(data_list, f_write, indent=2)
    except Exception as e:
        print(f"Error: {e}")
        return "Issue with data and server!", 500
    
    return jsonify({'message': 'Data updated successfully', 'data': data})


@app.route('/about')
def about():
    '''About page, showing lore'''
    return render_template('about.html')

def get_json_api():
    '''Opens the movies_inventory.json file as read only and returns its contents'''
    try:
        with open('movies_inventory.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return data
    except FileNotFoundError:
        return "JSON file not found!", 404
    except json.JSONDecodeError:
        return "Invalid JSON data!", 500

def filter_movies(data, decade, genre, query):
    '''Filters movies from the movies_inventory.json file by decade, genre and query text.'''
    if decade:
        if decade.isnumeric() and 1899 < int(decade) < 2050:
            new_data = [d for d in data if int(decade) <= int(d.get('year')) <= int(decade) + 9]
            data = new_data

    if genre:
        new_data = [d for d in data for d_genre in d.get('genres') if d_genre.lower() == genre.lower()]
        data = new_data

    if query:
        new_data = [d for d in data if query.lower() in d.get('title').lower()]
        data = new_data

    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)