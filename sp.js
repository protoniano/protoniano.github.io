function acomodador(lista, indicador) {
    var retornadora = Array();
    var true_retorner = Array()
    if(indicador === 0){
        var pre_mayor = 0;
    }else{
        var pre_mayor = 1000000;
    }
    for (var i = 0; i < lista.length; i++) {
        var the_list = Array()
        var index = 0;
        var permitidor = retornadora.length
        var el_comparador = pre_mayor;
        if (permitidor != 0) {
            var len = retornadora.length
        } else {
            var len = lista.length
        }
        for (var j = 0; j < len; j++) {
            if (permitidor != 0) {
                var numero_c = retornadora[j];

            } else {
                var numero_c = lista[j];
            }
            if (indicador === 0 && numero_c > el_comparador) {
                el_comparador = numero_c;
                index = j;
            }else if(indicador === 1 && numero_c < el_comparador){
                el_comparador = numero_c;
                index = j;
            }
        }
        if (permitidor != 0) {
            true_retorner.push(retornadora[index]);
        } else {
            true_retorner.push(lista[index])
        }
        for (var o = 0; o < len; o++) {
            if (o != index) {
                if (permitidor != 0) {
                    the_list.push(retornadora[o]);
                } else {
                    the_list.push(lista[o])
                }
            }
        }
        retornadora = the_list;
    }
    return true_retorner;
}

function masonte(listax, height) {
    
    var t = "M"
    for(var i = 0; i < listax.length;i++){
        t+=i*30+40+","+(height-listax[i])+" "
    }
    return t
}

const rqt = new Request("images/jac.json");
let pap = {}

fetch(rqt)
.then((response)=>{
    if(!response.ok){
        throw new Error(`HTTP error! Status: ${ response.status }`);
    }

    return response.json()
})
.then((response)=>{
    console.log(response)
    pap = response;
})
console.log(pap);
