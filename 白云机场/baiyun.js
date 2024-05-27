// import {K as x, a as K, h as q} from "./补充js.js";
const { K:x, a:K, h :q } = require('./补充js.js');
de = e=>{
    let n = {};
    if (null == e || "" === e)
        return "";
    let t = JSON.parse(e)
      , r = Object.keys(t).sort();
    for (let o = 0; o < r.length; o++) {
        let e = t[r[o]];
        null != e && (n[r[o]] = t[r[o]])
    }
    return JSON.stringify(n)
}

fe = (e,n)=>{
    const t = x.getKey(e)
      , r = new K.crypto.Signature({
        alg: "SHA256withRSA"
    });
    return r.init(t),
    r.updateString(n),
    q(r.sign())
}






 let r = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (e=>{
        const n = 16 * Math.random() | 0;
        return ("x" == e ? n : 3 & n | 8).toString(16)
    }
    ))
n='{"type":"1","terminal":"","day":0,"depOrArr":"1","pageNum":3,"pageSize":15}';

get_data=function (n){
    o = (new Date).getTime()
    aab = de(n);
     t="/byairport-flight/flight/list"

     signature= fe("-----BEGIN PRIVATE KEY-----\n  MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdgJNfUFPDNJsL\n  HObB1JMu7E1+nuwkFHmXnBU2AOM2dweE+tpmViZo90w+YQIuIS8MoVz60AGHbLE8\n  BYcdxQEKmPsqq0Lq/1ltIdp1YcO9W60qSxwpZS+7o73ljRrrtOXcE1UUpH5l07Fh\n  ziCIRDI/4ODCA8AJ1kV6IyfPNM2Fes3BEqhMOgw4Z5i4pZHnb4Nm+4kEXmyM+UgQ\n  cShcXZA/dx5MXKA2Bbb0I0G6HS3D4nMhnm6IgYWEyT8ngenMOyy+ysBuHWt2j9Cp\n  AGLWRyqHigFcKTlP5BSIkU+8sqssab1jvDg2F8MXWuupwF43OVARgHofiwQBAHPo\n  PfTfPlMvAgMBAAECggEBAJKQpZNasrfCak0LFgllgZl2uB6OUPy6OPRGgM6CQO3c\n  EhlDPp1gqdmf10ltCJRYuOmt91JG4kVddgh+tF+VhgSQm5n3SQxZlqQhjqMQ2Q+L\n  Ejd7Mberu6GHHB1TE6wn6IbFTrUo5Z5oQnbbVBa6L3CWGVEyIDCHPpwLvu3pGx+L\n  083dNQUiF8WcSGybl1h4ZapAGdndPYJReKYccNBYu5IzTEjtG3VpMHl56hD8fPV8\n  SStYv4sEffyCbze5/KvG3WlG+8n1WzBRMAN1U8Qk3JlMM/g5Y2tL1elI2pQRmjH8\n  EVxNUzB9Ob/qk2N6pF4KwhDWjILkHdoXilHMgP5x0gECgYEAy9O9ShtRNwXdFzHe\n  v+buyjvWWvwTVRUBehe8BWO1QaZ4c/INw1Ks4pgoKvXyU1DRx5OloIx6BWDbs00O\n  1W1cDue2I/Ymvx5Q/XJmZK4eR2U3a2dmKLKVhCXhJ3y02R/OZ2xQHV3NZXqz88kf\n  rEmEKYTW9q2gVsZa82XpQhKnBYECgYEAxdFJ55AkU7VfzpV1x68NUetomB3OWxyq\n  Cugn3STLNx7Jw6FaK3dwRz0eKIbwCRxtlluZmxWX0jWSvj3cyLRBIKTD8atUfJW2\n  +ESKZb/i961HhhQjXqNfGQpmMdEazNqv0sDzQ5jHHIjc63oty/FjckcC+AaDGZIJ\n  VGCet5J5kK8CgYBm2R/Bfgk792R5KLvaHz/MoebmoB1tKB1HqyQ/n/E9AC/1aWUS\n  cuwzpk1WaCXvbm98Af9oBJopjpctYSuj+/ugtcDNYo5oj3aUfJ44HTfAFM2jD1iY\n  HoydUrPKxf1HNepje17tgoB6vTCCSbEGsU3T2WjSrgei4ZHREVJi+aB3gQKBgEy8\n  rm2sxdrPHjZWVlU6+/DOYEm6LkW77d7DRkuMLWTZha1lF0SLVbvc4qkYB1+RbpWI\n  PSMjEj0SWTWBa/dTrXwLTpOeQez+avcOJ53m/RXVW0yQ3VOmDor5NMGYe0wCfXhF\n  L1kGmB7inMigIcnefxRipa0vYYX217WqsYdGw++zAoGBALKswyV5j1GjVjN+fS1t\n  N9R0x+S7cKBqW6Bwj6aAdo4+spmRn9WK4h9Zk2k7BMUiqJKTce6RdW0Ep+aTErRs\n  LL0sBHArhQdaQvq0yS57BJUZm3ASrOpp3wkQdDejS3YEKiIQSG2kNFRanh8RbtbA\n  ac7pfLikyQm795/qF0H9YHgF\n  -----END PRIVATE KEY-----", "Timestamp&" + o + "&" + t + "&" + r + "&" + aab),
timestamp= o.toString();
nonce= r;

console.log(signature)
console.log(timestamp)
console.log(nonce)
    return [signature,timestamp,nonce]
}
console.log(get_data(n))

