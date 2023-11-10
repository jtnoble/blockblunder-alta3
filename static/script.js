let href = window.location.href;
href = href.substring(0, href.lastIndexOf('/')) + "/";

// Redirect when searching via searchbar
function redirect_query() {
    let searchBar = document.getElementById('search-bar');
    let api_read = href + "?query=" + searchBar.value;
    window.location.href = api_read;
}

// Redirect when searching via detailed search
function detailed_search() {
    let searchBar = document.getElementById('search-bar');
    let decade = document.getElementById('selected-decade');
    let genre = document.getElementById('selected-genre');
    if (decade.value == "Decade") {
        decade.value = "";
    }
    if (genre.value == "Genre") {
        genre.value = "";
    }
    let api_read = href + "?query=" + searchBar.value + "&decade=" + decade.value + "&genre=" + genre.value;
    window.location.href = api_read;
}

// POST REQUEST: Handler for clicking the 'checkin/out' button on the movies table
function check_in_out(e) {
    let row = e.closest('tr');
    var pTag = row.querySelector('.movie-id');
    var movieId = pTag.textContent;
    movieId = parseInt(movieId);

    let data = {"id": movieId}
    fetch(href+"api/inventory/checkout", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then(res => window.location.reload());
}