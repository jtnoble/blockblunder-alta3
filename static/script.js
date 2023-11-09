let api_url = '/api/inventory/json'
// not sure what is going on here yet...
function update_table() {
    tableHTML = document.getElementById('movies-table');
    fetch(api_url)
    .then(res => {
        res.json()
    })
}









searchBtn = document.getElementById('search-button');
searchBtn.addEventListener('click', () => {
    update_table()
})