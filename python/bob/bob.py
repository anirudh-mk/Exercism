def response(hey_bob):

    cleaned_data = hey_bob.strip()
    
    if cleaned_data == "":
        return "Fine. Be that way!"
    
    if cleaned_data.isupper():
        if cleaned_data.endswith('?'):
            return "Calm down, I know what I'm doing!" 
        return "Whoa, chill out!"
        
    if cleaned_data.endswith("?"):
        print('hi')
        return "Sure."
    
    return "Whatever."
        