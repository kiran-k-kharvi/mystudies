var a = document.querySelector("#a")
var b = document.querySelector("#b")
var c = document.querySelector("#c")
var d = document.querySelector("#d")
var e = document.querySelector("#e")
var f = document.querySelector("#f")
var g = document.querySelector("#g")
var h = document.querySelector("#h")
var i = document.querySelector("#i")

var res = document.querySelector("#btn")

a.addEventListener("click",function(){
    var x = a.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    a.textContent = zr
})
b.addEventListener("click",function(){
    var x = b.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    b.textContent = zr
})
c.addEventListener("click",function(){
    var x = c.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    c.textContent = zr
})
d.addEventListener("click",function(){
    var x = d.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    d.textContent = zr
})
e.addEventListener("click",function(){
    var x = e.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    e.textContent = zr
})
f.addEventListener("click",function(){
    var x = f.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    f.textContent = zr
})
g.addEventListener("click",function(){
    var x = g.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    g.textContent = zr
})
h.addEventListener("click",function(){
    var x = h.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    h.textContent = zr
})
i.addEventListener("click",function(){
    var x = i.textContent
    if (x==="") {
        zr = "X"   
    }
    else if(x==="X"){
        zr = "O"
    }
    else{
        zr=""
    }
    i.textContent = zr
})

res.addEventListener("click",function(){
    
    a.textContent = ""
    b.textContent = ""
    c.textContent = ""
    d.textContent = ""
    e.textContent = ""
    f.textContent = ""
    g.textContent = ""
    h.textContent = ""
    i.textContent = ""
   
})