var list = document.getElementById("a_ssa");
var firt_time = false;
var ar = [];
var index = 0;
function ss() {
    var item_list = document.createElement("li");
    item_list.className = "il_style";
    list.appendChild(item_list);


    if (firt_time === false) {
        list.style.height = "max-content";
        firt_time = true;
    }

    var ils = document.getElementsByClassName("il_style");


    for (let i = 0; i < ils.length; i++) {
        const element = ils[i];
        element.addEventListener("click", function () {
            element.style.background = "blue";
        })
    }

}
function ee(tt) {
    tt.style.background = "blue";
}
document.getElementById("btn").addEventListener("mousemove", ss);

function acomodador(lista) {
    var retornadora = Array();
    var true_retorner = Array()

    for (var i = 0; i < lista.length; i++) {
        var the_list = Array()
        var el_mayor = 0;
        var index = 0;
        var permitidor = retornadora.length
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
            if (numero_c > el_mayor) {
                el_mayor = numero_c;
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
        console.log(the_list)

        retornadora = the_list;
    }
    return true_retorner;
}