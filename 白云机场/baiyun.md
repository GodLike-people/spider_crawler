### 一点碎碎念 
baiyun机场的逆向，整体逆向不算很难，不过也多少有点坑。

加密位置只需要搜索参数，就能很快找到。 
找到参数，进入到pe方法，里面就是完整加密逻辑，用的是RSA加密。初步扣代码不难。

但是扣着扣着，会发现有下面这段代码，baiyun机场的难点，就在下面代码的参数x和K，解决了就都解决了。
```angular2html
 const t = x.getKey(e)
      , r = new K.crypto.Signature({
        alg: "SHA256withRSA"
    });
```

这里我把所有加密的方法js文件都补上了（补充js.js）， 直接导入，就懒得一步步扣
```angular2html
const { K:x, a:K, h :q } = require('./补充js.js');
```
在nodejs里，直接导入有一个问题就是，要用commonjs的语法，不要用es6的import语法
``
import {K as x, a as K, h as q} from "./jsrsasign-cf827c25.js";
``

用import在nodejs里会报错

在<补充js.js> 文件中 同时需要使用module.exports或exports来导出变量：
```angular2html
export { Jt as K,  $t as a,  Xt as h};

改写成下面这样

module.exports = {
  K: Jt,
  a:$t,
  h: Xt
};
```


### baiyun机场 逆向知识点 

扣代码,RSA算法,nodejs导出文件

