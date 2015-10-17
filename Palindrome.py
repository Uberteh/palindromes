def main():
	word= []
	word= input("Input word to test if it is a Palindrome: ")
	
	L1=[c for c in word if c.isalpha()]

	L2 = [x.lower() for x in L1]
	L3 = L2[::-1]
	

	if (L2 == L3):

		print("This is a palindrome.")
		return main()
	else:
		print("That is not a palindrome.")
		return main()




	return main ()

main()