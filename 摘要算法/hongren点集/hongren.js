n = {
    "no": "dy3009",
    "data": {}
}
const cryptoJS = require("crypto-js")

get_params = function (text) {
    var e = (new Date).getTime()
    C = "kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$"
    // text = "param=" + JSON.stringify(text) + "&timestamp=" + e + "&tenant=1&salt=" + C
    //param="{\"no\":\"dy3009\",\"data\":{}}"&timestamp=1716996279382&tenant=1&salt=kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$  XXXXX错误XXXXX
    text = "param=" + text + "&timestamp=" + e + "&tenant=1&salt=" + C
    console.log(text);
    sign = cryptoJS.SHA256(text).toString()
    return [e, sign]
    // console.log(cryptoJS.SHA256("text").toString());
}

console.log(get_params("{\"no\":\"dy3009\",\"data\":{}}"));


// console.log(cryptoJS.SHA256("1").toString());