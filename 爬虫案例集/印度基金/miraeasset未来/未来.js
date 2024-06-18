window=global;
request={
    "modulename": "Factsheet",
    "pgno": 1,
    "pgsize": 10
}
const JSEncrypt=require("jsencrypt")
function EncryptFunction(e) {
    var t = new JSEncrypt;
    t.setPublicKey("MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAOvAjm2G3Izal1C+7/KmbtYPjmpoddfexaNNl4Yc1KZCF72oczL8J6yq534Thl7/ViLr0a14e3x8+w7YzI/8cfkCAwEAAQ==");
    var n, o = JSON.stringify(e);
    n = o.length / 22;
    for (var a = "", r = 0; r < n; r++)
        a += t.encrypt(o.slice(0, 22)),
        o = o.substring(22);
    return a
}

console.log(EncryptFunction(request));


