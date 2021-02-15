def replace(s,a,b):
    if len(s) == 0:
        return s
    
    smallIO = replace(s[1:],a,b)

    if s[0]==a:
        return b + smallIO
    else:
        return s[0] + smallIO



ls = 'qwedssdyu'
print(replace(ls,'s','i'))


