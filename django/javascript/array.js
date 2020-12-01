var loop = true
var roaster = []
while(loop)
{
   var opt = prompt("What action you want to perform (add,display,remove,exit) ?")
   if(opt==="add"){
       ele = prompt("Enter the name to add ")
       roaster.push(ele)
   }
   if(opt==="remove"){
    ele = prompt("Enter the name to remove ")
    var temp = []
    for (name of roaster){
        if(name != ele){
            temp.push(name)
            roaster = temp
            temp = []
        }
    }
    alert("array after removing "+ele+" is "+roaster )

}
if(opt ==="display"){
   alert(roaster)
}
if(opt ==="exit")
{
    loop = false
}



}