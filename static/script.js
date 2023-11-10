let href = window.location.href;
href = href.substring(0, href.lastIndexOf('/')) + "/";

function redirect_query() {
    let searchBar = document.getElementById('search-bar');
    let api_read = href + "?query=" + searchBar.value;
    window.location.href = api_read;
}

function check_in_out() {
    console.log("TODO");
}

let searchBtn = document.getElementById('search-button');
searchBtn.addEventListener('click', () => {
    redirect_query();
})