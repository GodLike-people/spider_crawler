const CryptoJS = require("crypto-js")

get_params = function () {
    n = Date.now().toString()
    code = CryptoJS.MD5(n + "9527" + n.substr(0, 6)).toString()
    console.log(code)
    return [n, code]
}


console.log(CryptoJS.MD5("1").toString());