def sort_hyphen_string(text):
    words = text.split('-')          
    words.sort()                     
    sorted_text = '-'.join(words)    
    return sorted_text


result = sort_hyphen_string("python-variable-funcion-computadora-monitor")
print(result)