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
                element.addEventListener("click", function(){
                    element.style.background = "blue";
                })
            }

        }
        function ee(tt) {
            tt.style.background = "blue";
        }
        document.getElementById("btn").addEventListener("mousemove", ss);