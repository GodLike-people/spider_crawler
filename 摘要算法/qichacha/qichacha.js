const cryptoJS = require("crypto-js")


// n='{"searchkey":"小米","pageindex":2,"pagesize":20}'


// n="iLAgiklLN8QiklLN8QrLi4giLAgiklLN8QiklLN8QrLi4g"
// e='/api/search/searchmulti{"searchkey":"小米","pageindex":2,"pagesize":20}'
// secrect=cryptoJS.HmacSHA512(e,n).toString()
// console.log(secrect)


// arguments= {
//     "0": "/api/search/searchmulti"
// }

hmac_func = function (e, n) {
    return cryptoJS.HmacSHA512(e, n)
}

bb2 = function (e, t) {
    return hmac_func(e, t).toString()
}

aa2 = function () {
    o = {
        "n": 20,
        "codes": {
            "0": "W",
            "1": "l",
            "2": "k",
            "3": "B",
            "4": "Q",
            "5": "g",
            "6": "f",
            "7": "i",
            "8": "i",
            "9": "r",
            "10": "v",
            "11": "6",
            "12": "A",
            "13": "K",
            "14": "N",
            "15": "k",
            "16": "4",
            "17": "L",
            "18": "1",
            "19": "8"
        }
    }
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var a = t[i].charCodeAt() % o.n;
        n += o.codes[a]
    }
    return n
}
a_default = function () {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , n = JSON.stringify(e).toLowerCase();
    return bb2(t + n, aa2(t)).toLowerCase().substr(8, 20)
}


r_default = function () {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
        , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , i = JSON.stringify(e).toLowerCase();
    return (bb2)(n + "pathString" + i + t, (aa2)(n))
}
window = global
window.tid = '57d94eb35137dbaec407200d6b9ed4ae'
s_default = function () {
    var list = ["w", "i", "n", "d", "o", "w", ".", "t", "i", "d"];
    return eval(list.join(""))
}

data = {
    "searchKey":"小米",
    "pageIndex":1,
    "pageSize":20
}

get_params = function (data) {
    console.log(data)
    t = "/api/search/searchmulti"
    var i = a_default("/api/search/searchmulti", data)
    console.log(i)
    var l = (r_default)(t, data, (s_default)());
    console.log(l)

    return [i,l]

}

console.log(get_params(data));







