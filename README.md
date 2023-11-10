# blockblunder-alta3
BlockBlunder Flask Project for Alta3 TLG Cohort

### Installation
- Requires Python 3.8+
- Install pip packages
  - `pip install -r requirements.txt`

### Running
- Run locally with `python alta3research-flask01.py`
- Open your browser to localhost:2224
  - http://127.0.0.1:2224
- If you would like to run the requests check, you must run the flask01 file first
  - `python alta3research-requests02.py`

#### EndPoints
- `/`: Main page, shows a table of all items in the movies_inventory.json, or just shows searched items via query parameters.
- `/search`: Detailed search, allowing for search of query parameters, genre, and decade.
- `/about`: About section explaining what this site is.
- `/api/inventory`: A quick look at the full table of items from the movies_inventory.json file with no extra fluff.
- `/api/inventory/json`: JSON returned from the movies_inventory.json file with the oppourtunity to query using the parameters "query", "genre", and "decade".

#### Known Issues
- Spamming Checkin/out: This will cause an internal server error. With a reload, you should be back in just fine.
- Paginate with query params: If you choose query params that still result in over 100 rows of data, if you try to go to the next page, you will be returned to the table with ALL movies, not just queried ones
