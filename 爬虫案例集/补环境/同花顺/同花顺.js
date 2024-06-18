(function () {
    //不能修改他原有逻辑
cookie_data=document.cookie

//1 对象 2属性 3执行的操作
Object.defineProperty(document,"cookie",{
    get:function (){
        return cookie_data
    },
    set:function(val){
        if (val.indexof("v")!=-1){
               console.log("新获取的cookie",val)
        debugger;
        }
        cookie_data=val

    }
})
})

(function(){
   'use strict'
    var _cookie = "";
    Object.defineProperty(document, 'cookie', {
        set: function(val) {
            console.log(val);
            debugger
            _cookie = val;
            return val;
        },
        get: function() {
            return _cookie;
        },
});
})()

