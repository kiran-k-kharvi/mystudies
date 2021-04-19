def pickingNumbers(a):
    # Write your code here
    d = {}
    numlist=[]
    num1=num2=maxNum=-1
    for x in a:
        if x in d:
            d[x]= d[x]+1
        else:
            d[x]=1
    flag = False
    for k,v in d.items():
        if k+1 in d:
            if d[k]+d[k+1]>maxNum:
                maxNum = d[k]+d[k+1]
                num1 = k
                num2 = k+1
                flag = True
                
    
    if flag:
        negNum1 = -1 * num1

        for k,v in d.items():
            if k not in [num1,num2] and k <= negNum1:
                maxNum += d[k]
    
        # elif k-1 in d:
        #     if d[k]+d[k-1]>maxNum:
        #         maxNum = d[k]+d[k-1]
        #         num1 = k
        #         num2 = k-1
                 
        return maxNum
    else:
        return sorted(d.items(),key=lambda kv:kv[1],reverse=True)[0][1]

a = [66]*100

print(pickingNumbers(a))