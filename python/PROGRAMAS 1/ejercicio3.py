def isVowel2(char):
	if char in 'aeiouAEIOU':
		return True
	else:
		return False

print("Indica una letra");

letra =input();

print(isVowel(letra));
