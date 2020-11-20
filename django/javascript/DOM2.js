var one = document.querySelector("#om");


one.addEventListener("mouseover",oh);
one.addEventListener("mouseout",oh1);
// header.style.color = "red"

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

// function myfun2()
// {
//     colorip = myfun()
//     header.style.color = colorip
// }
// header.addEventListener("click",myfun2)


function oh()
{ 
    one.innerHTML = " this will change"
    var ch = myfun()
    one.style.color = ch
}
function oh1()
{
    one.innerHTML = "again changed"
    var ch = myfun()
    one.style.color = ch
}

