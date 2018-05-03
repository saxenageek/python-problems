numerals = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

def tonumber(number):
	result = 0    
	pv = None    
	for letter in reversed(number):
		result = result + numerals[letter] if (pv is None) or (pv <= numerals[letter]) else result - numerals[letter]
		pv = numerals[letter]
	return result


print(tonumber("MD"))
