var header = document.querySelector("h1")

header.style.color = "red"

function myfun()
{
    var s = "0123456789ABCDEF"
    var color = '#'
    for (var x =0;x<6;x++)
    {
        color += s[Math.floor(Math.random()*16)]
    }
    return color
}

function myfun2()
{
    colorip = myfun()
    header.style.color = colorip
}

setInterval("myfun2()",500)