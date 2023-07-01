#Printing ascci value corresponding to alphabet.
dic={} #Taking emty dictionary
for i in range(97,123): #ASCCI Value of "a"=97 and z="122"
    dic[chr(i)]=i 
print(dic)    