window=global
navigator={
        'appCodeName': "Mozilla",
'appName': "Netscape",
'appVersion': "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
}
const JSEncrypt=require("jsencrypt")
// const JSEncrypt = require('./jqueryAjax');

function getUuid() {
    var s = [];
    var a = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = a.substr(Math.floor(Math.random() * 0x10), 1)
    }
    s[14] = "4";
    s[19] = a.substr((s[19] & 0x3) | 0x8, 1);
    s[8] = s[13] = s[18] = s[23];
    var b = s.join("");
    return b
}
function sort_ASCII(a) {
    var b = new Array();
    var c = 0;
    for (var i in a) {
        b[c] = i;
        c++
    }
    var d = b.sort();
    var e = {};
    for (var i in d) {
        e[d[i]] = a[d[i]]
    }
    return e
}
function url2json(a) {
    var b = /^[^\?]+\?([\w\W]+)$/
      , reg_para = /([^&=]+)=([\w\W]*?)(&|$|#)/g
      , arr_url = b.exec(a)
      , ret = {};
    if (arr_url && arr_url[1]) {
        var c = arr_url[1], result;
        while ((result = reg_para.exec(c)) != null) {
            ret[result[1]] = result[2]
        }
    }
    return ret
}
function dataTojson(a) {
    var b = [];
    var c = {};
    b = a.split('&');
    for (var i = 0; i < b.length; i++) {
        if (b[i].indexOf('=') != -1) {
            var d = b[i].split('=');
            if (d.length == 2) {
                c[d[0]] = d[1]
            } else {
                c[d[0]] = ""
            }
        } else {
            c[b[i]] = ''
        }
    }
    return c
}
const serialize = function(a) {
    var b = [];
    for (var p in a)
        if (a.hasOwnProperty(p) && a[p]) {
            b.push(encodeURIComponent(p) + '=' + encodeURIComponent(a[p]))
        }
    return b.join('&')
};
var paramPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvxXa98E1uWXnBzXkS2yHUfnBM6n3PCwLdfIox03T91joBvjtoDqiQ5x3tTOfpHs3LtiqMMEafls6b0YWtgB1dse1W5m+FpeusVkCOkQxB4SZDH6tuerIknnmB/Hsq5wgEkIvO5Pff9biig6AyoAkdWpSek/1/B7zYIepYY0lxKQIDAQAB";
var encrypt = new JSEncrypt();
encrypt.setPublicKey(paramPublicKey);

    beforeSend=function(b) {
        var c = Date.parse(new Date());
        var d = getUuid();
        var e = JSON.stringify(sort_ASCII(dataTojson(b.data || '{}')));
        b.data = encrypt.encryptUnicodeLong(e);
        var f = MD5(e + d + c);

        a.setRequestHeader("timestamp", c);
        a.setRequestHeader('requestId', d);
        a.setRequestHeader('sign', f)
    }


console.log(beforeSend('page=1&limit=20&pointname=%E5%A3%B6%E7%93%B6%E5%B1%B1%E5%9B%BD%E5%AE%B6%E7%BA%A7%E8%87%AA%E7%84%B6%E4%BF%9D%E6%8A%A4%E5%8C%BA%E7%AE%A1%E7%90%86%E5%B1%80'));