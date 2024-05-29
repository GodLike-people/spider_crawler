### hongren 注意点 

和mytoken的MD5加密类似，找到加密位置，测试发现，为标准SHA256加密，使用标准库即可

### 有个坑：
在python传递数据给js使用json.dumps;以及在js里使用参数的时候，JSON.Stringfy方法
在给param数据加密的时候，要注意序列化之后的差异

json.dumps和JSON.Stringfy之后的数据如下：
```
param="{\"no\":\"dy3009\",\"data\":{}}"
```
这时候需不需要序列化，需要查看官网原数据如何？

官网加密没有反斜杠，即无论是在js里还是在python里无需序列化，所以这里在扣下js代码时候，要去掉JSON.Stringfy

因为这时候使用的param是从python传递过来，就已经是解析好的参数

注意细节！！！！尤其是在方法都扣下来，但是依旧有问题的情况，要留意。

![img.png](img.png)

