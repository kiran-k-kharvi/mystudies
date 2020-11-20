var fname = prompt("Enter your first name")
var lname = prompt("Enter your last name")
var age = prompt("Enter your age")
var hgt = prompt("Enter your height in cm ")
var pname = prompt("Enter your pet name")

if(fname[0]===lname[0] && 20 > age < 30 && hgt >= 170 && pname.endsWith("y") )
{
 console.log("welcome commando!!!!!")
}
else{
 console.log("I dont know you")

}