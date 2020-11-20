var num = prompt("Enter the series till it need to print")
var num2 = num
var cont = 0
while(num>0)
{
    cont = cont+1
    console.log(cont)
    num -= 1
}
var arr = []
cont = 0
while(num2>0)
{
    cont = cont+1
    arr.push(cont)
    num2 -= 1
}

console.log(arr.join(' '))