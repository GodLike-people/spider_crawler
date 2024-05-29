// npm install crypto-js --save

var cryptoJS=require("crypto-js")

var text="python"
console.log(cryptoJS.MD5(text).toString(),"MD5长度为："+cryptoJS.MD5(text).toString().length);


console.log("SHA1长度为："+cryptoJS.SHA1(text).toString().length);
console.log("SHA224长度为："+cryptoJS.SHA224(text).toString().length);
console.log("SHA256长度为："+cryptoJS.SHA256(text).toString().length);
console.log("SHA512长度为："+cryptoJS.SHA512(text).toString().length);

 var key = "secret"
console.log(cryptoJS.HmacMD5(text,key).toString(),"HmacMD5长度为："+cryptoJS.HmacMD5(text,key).toString().length);