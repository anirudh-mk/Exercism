def is_pangram(sentence):
    
    letters = set()
    
    for letter in sentence:
    
        if letter.isupper():
            letter = letter.lower()
        
        if 'a' <= letter <= 'z':
            letters.add(letter)
    
    return True and len(letters) == 26
