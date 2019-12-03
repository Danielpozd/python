from random import randrange
import sys

def xor(a, b): 
   
    # initialize result 
    result = [] 
   
    # Traverse all bits, if bits are 
    # same, then XOR is 0, else 1 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 

def syndromGenerator(initial_string, gx):
	syndromformation = []
	new_string = list(initial_string)
	for i in range(0, 15):
		a = new_string[i]
		##print(a)
		if new_string[i] == "1":
			new_string[i] = "0"
		else:
			new_string[i] = "1"

		syndromremainder = mod2div(new_string, gx)
		syndromformation.append(syndromremainder)

		new_string[i] = a
		##print(new_string)
	##print(syndromformation)
	return syndromformation

def syndrom(remainder, syndromtable):
	
	##print(syndromtable)
	##print(remainder)
	
	##syndromtable = ['0001', '0010', '0100', '1000', '0011', '0110', '1100', '1011', '0101', '1010', '0111', '1110', '1111', '1101', '1001']
	for i in range(0, 15):
		if remainder == syndromtable[i]:
			##print(i)
			return i



def error(string):
	string1 = list(string)
	##print(string1)
	error = randrange(0, 15, 1)
	##print(f"{error} =>  {string1[error]}")
	if string1[error] == "1":
		string1[error] = "0"
	else:
		string1[error] = "1"
	#print(string1)
	string1 = ''.join(string1)
	return string1


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

string = "01010101111"
##print(len(string))


gx = "10011"

recreated_string = string + (len(gx)-1)*'0'

##print(f"1 string ->{recreated_string}")


result = mod2div(recreated_string, gx)
##print(f"remainder after division -> {result}")

recreated_string2 = string + result
print(f"string that will be sended -> {recreated_string2}")

#-------------
#syndromGenerator
##print(recreated_string)
syndrom1 = syndromGenerator(recreated_string2, gx)
print(f"syndrom -> {syndrom1}")
#-------------

ErrorString = error(string + result)

##print(ErrorString)
ErrorString = ''.join(ErrorString)
print(f"recieved string with an error -> {ErrorString}")

errorResult = mod2div(ErrorString, gx)
print(f"remainder after division the error string -> {errorResult}")

k = syndrom(errorResult, syndrom1)
print(f"possition of an error bit -> {k}") 

finito = list(ErrorString)
##print(finito)

if finito[k] == '1':
	finito[k] = '0'
else:
	finito[k] = '1'
finito = ''.join(finito)
print(f"ta daaaaa! -> {finito}")

exit()