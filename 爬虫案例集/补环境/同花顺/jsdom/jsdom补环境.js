//npm install jsdom --save

//jsdom 相当于 有一套自己的环境，可以把环境直接拿过来使用，使用方式即
//document=dom.window.document

const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
title = dom.window.document.querySelector("p").textContent
console.log(title)

document=dom.window.document
window=dom.window
document=dom.window.navigator
console.log(document.head)
