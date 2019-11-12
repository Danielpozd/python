def xor(a, b): 
   
    
    result = [] 
   
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 

def mod2div(divident, divisor): 
   
    
    pick = len(divisor) 
   

    tmp = divident[0 : pick] 
   
    while pick < len(divident): 
   
        if tmp[0] == '1': 
   
            tmp = xor(divisor, tmp) + divident[pick] 
   
        else:   
            tmp = xor('0'*pick, tmp) + divident[pick] 
   
        pick += 1
   
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
   
    checkword = tmp 
    return checkword 

def encodeData(data, key): 
   
    l_key = len(key) 
 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
    
    codeword = data + remainder 
    return codeword     

def decodeData(data, key): 
   
    l_key = len(key) 
   
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
   
    return remainder 
  
input_string = input("vvedi stroku->") 
data =(''.join(format(ord(x), 'b') for x in input_string)) 
print(data) 
key = "1001"
  
ans = encodeData(data,key) 
print(ans) 

ans1 = decodeData(ans, key) 
print("Octatok->"+ans1) 