plus=function(){
    console.log("第一个参数:",arguments[0])
    console.log("第二个参数:",arguments[1])
    return arguments[0]+arguments[1]
}

console.log(plus('1', '2'));

//输出
// 第一个参数: 1
// 第二个参数: 2
// 12
