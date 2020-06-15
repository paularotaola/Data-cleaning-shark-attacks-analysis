import re

def white_shark(x):
    x = str(x)
    match = re.search(r"[Ww](hite|HITE)", x)
    
    if match:
        return "White Shark"
    else:
        return "Other"

def injury(x): 
    x = str(x)

    if (x == "N") or (x == "n") or (x == " N"):
        return "N"
    elif (x == "Y") or (x == "y") :
        return "Y"
    else:
        return "N"
