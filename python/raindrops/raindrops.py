def convert(number):
    if number < 3:
        return str(number)
        
    if number % 3 == 0:
        if number % 5 == 0:
            if number % 7 == 0:
                return 'PlingPlangPlong'
            return 'PlingPlang'
        elif number % 7 == 0:
            return 'PlingPlong'
        return 'Pling'
    
    if number % 5 == 0:
        if number % 7 == 0:
            return 'PlangPlong'
        return 'Plang'
    
    if number % 7 == 0:
        return 'Plong'
    return str(number)
