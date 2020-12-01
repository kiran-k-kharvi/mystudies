var temp = prompt("Enter the surrounding temperature")
var res = ""
if (temp>38 && temp<=60) {
res = "Its hot"
    
} else if (temp>60){
    res = "very hot"

}
else{
    res = "normal"
}

console.log(res)