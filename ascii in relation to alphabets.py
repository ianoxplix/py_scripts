# file to relate alphabets to there ascii values 
print("\nUpper case letters with the associated ASCII values:")
ch = 'A'                       
for i in range(26):
    print(ch, ord(ch))
    ch = chr(ord(ch) + 1)

    
print("\nLowercase letters:")
ch = 'a'                        
for i in range(26):
    print(ch, ord(ch))          
    ch = chr(ord(ch) + 1) 
