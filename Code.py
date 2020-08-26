# Program-to-remove-vowels-from-sentence
#define function to remove vowel
def remove_vowels(newstr, string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for j in string.lower():
        if j in vowels:
            newstr = newstr.replace(j, '')
    return newstr

print("Click * to close program. ")
string = input("Enter any string to remove vowel : ")
if string == '*':
    exit()

else:
    newstr = string
    print("Removing vowels from string...")
    print("Vowels removed from string")
    newstr = remove_vowels(newstr, string)
    print(f"This is your new string : {newstr}.")
