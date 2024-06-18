var target = {
    name: 'JACK',
    age: 18,
};

var p = new Proxy(target, {

    get: function (target, propertyKey, receiver) {
        // 1 原对象
        // 2 访问属性
        // 3 代理器处理对象
        console.log(target, propertyKey, receiver)
    },
    set: function(target,propertyKey,value,receiver){
        // 1. 原对象
        // 2. 设置的属性
        // 3. 设置的值
        // 4. 代理器代理的对象
        console.log(target, propertyKey, value, receiver)
    }
})
p.age
p.user = 'aa'