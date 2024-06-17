// 整套流程是把列表当作实参传递给了自执行参数的e，然后n调用的就是列表的索引值，也就执行到e[t].call,对列表里某个函数进行调用

//外部导出
var bc;

//webpack打包格式
!function(e){
    //加载器
    function n(t){
        //这里的call起到了调用函数的作用，即得到函数的返回值
        return e[t].call()
    }

    //调用
    // n(0);
    bc=n

}(
    //插件 模块
{
     aa:function (){
            console.log("登录")
        },
        bb:function (){
            console.log("加密")
        },
        cc:function (){
            console.log("解密")
        },
}
)

console.log(bc(4));

function someFunction() {
  console.log("lallalalal");
}

someFunction.call();
