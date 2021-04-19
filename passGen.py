import string
import random



def generator(length = 16, letters_ = True,numbers_ = True, punctuation_ = True):
    
    letters = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation
    
    char  = ""
    char += letters if letters_ else ""
    char += numbers if numbers_ else ""
    char += punctuation if punctuation_ else ""
    
    return  "".join(random.choices(char, k=length))
