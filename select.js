const select_json_url = "https://protonianosaurio.github.io/select/select.json"
let select_inf = {}

const rquest = new XMLHttpRequest();

rquest.open('GET',select_json_url)
rquest.responseType = 'json';
rquest.send()

rquest.onload = function () {
    const respuesta = rquest.response

    select_inf = respuesta
    console.log(select_inf)
}