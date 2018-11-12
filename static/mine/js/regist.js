$(document).ready(function () {
    var account = document.getElementById('account')
    var accunterr = document.getElementById('accunterr')
    var checker = document.getElementById('checker')

    var pass = document.getElementById('pass')
    var passer = document.getElementById('passerr')
    var passwd = document.getElementById('passwd')
    var passwderr = document.getElementById('passwderr')


    //  **************验证账号***************
    account.addEventListener("focus", function () {
        accunterr.style.display = 'none';
        checker.style.display = 'none';
    }, false)

    account.addEventListener("blur", function () {
        instr = this.value
        if(instr.length < 6 || instr.length > 12){
            accunterr.style.display = 'block'
            return
        }
        
    //    发起请求,验证账号是否存在
        $.post('/checkuserid/',  {'userid': instr}, function (data) {
            if (data.status == 'error'){
                checker.style.display = 'block';
            }
        })
    }, false)

    // ***************密码****************

    pass.addEventListener("focus", function () {
        passer.style.display = 'none';
    }, false)

    pass.addEventListener("blur", function () {
        instr = this.value
        if(instr.length < 6 || instr.length > 12){
            passer.style.display = 'block'
            return
        }
    }, false)

    // **************验证密码***************

    passwd.addEventListener("focus", function () {
        passwderr.style.display = 'none';
    }, false)

    passwd.addEventListener("blur", function () {
        instr = this.value
        if(instr != pass.value){
            passwderr.style.display = 'block'
            return
        }
    }, false)



})