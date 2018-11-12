$(document).ready(function () {
    var alltypebtn = document.getElementById('alltypebtn')
    var showsortbtn = document.getElementById('showsortbtn')

    var typediv = document.getElementById('typediv')
    var sortdiv = document.getElementById('sortdiv')

    typediv.style.display = 'none'
    sortdiv.style.display = 'none'


    alltypebtn.addEventListener('click', function () {
        typediv.style.display = 'block'
        sortdiv.style.display = 'none'
    },false)

    showsortbtn.addEventListener('click', function () {
        typediv.style.display = 'none'
        sortdiv.style.display = 'block'
    },false)

    typediv.addEventListener('click', function () {
        typediv.style.display = 'none'
        sortdiv.style.display = 'none'
    },false)

    sortdiv.addEventListener('click', function () {
        typediv.style.display = 'none'
        sortdiv.style.display = 'none'
    },false)


    // 修改购物车  增加

    var subShoppings = document.getElementsByClassName('subShopping')
    var addShoppings = document.getElementsByClassName('addShopping')
    console.log(addShoppings.length)

    for(var i=0; i < addShoppings.length; i++){
        addShopping = addShoppings[i]
        addShopping.addEventListener('click', function () {
            pid = this.getAttribute('ga')
            console.log(pid)
            $.post('/changecart/0/', {'productid': pid}, function (data) {
                if (data.status == 'success'){
                //    如果成功，将span中间变成当前数量
                    document.getElementById(pid).innerHTML = data.data;
                }
                else {
                    if (data.data == -1){
                        console.log('******');
                        // $.get('/login/');
                        window.location.href='http://127.0.0.1:8000/login/';
                    }
                }
            })
        })
    }

    // 修改购物车  减少

    for(var i=0; i < subShoppings.length; i++){
        subShopping = subShoppings[i]
        subShopping.addEventListener('click', function () {
            pid = this.getAttribute('ga')
            console.log(pid)
            $.post('/changecart/1/', {'productid': pid}, function (data) {
                if (data.status == 'success'){
                //    如果成功，将span中间变成当前数量
                    document.getElementById(pid).innerHTML = data.data;
                }
                else {
                    if (data.data == -1){
                        console.log('******');
                        // $.get('/login/');
                        window.location.href='http://127.0.0.1:8000/login/';
                    }
                }
            })
        })
    }



})




