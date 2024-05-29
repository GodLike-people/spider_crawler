#### 怎么判断加密算法是md5？

MD5特质：

16进制，长度32就可能是md5

那怎么判断是否是16进制？

```
判断数据里有abcdef，可能为16进制（逢16进1）
如 ：87213627a0d09c6fd4e2eb747e61d435
```

进一步检验网站是否是md5加密：把网站算法加密1，以c4ca开头，即为加密

```
console.log(CryptoJS.MD5("1").toString());
//输出 c4ca4238a0b923820dcc509a6f75849b
```

sha1:23c02b203bd2e2ca19da911f1d270a06d86719fb`

`sha224:1ffeffcbe2707dc5d1c10df619203c1a3b620c70394b3c4c106d92e6`

`sha256:c3a845a318cd654749ea4db6f4d5f9cb5c6e5b0cade46d9dc04af46d32049c7c`

`sha512:af47f324b77a4885748bfc3f0d9b5a846c0153c589852bb3f185ab6e7a600547b818ab994776e8d24584457f9aac84246b0de971584cebbdd96aa1aee6630f9f`


