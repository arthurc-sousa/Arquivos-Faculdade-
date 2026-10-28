#Claudia Jacy Barenco Abbas
#26.08.2026
from datetime import datetime
impar = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
minuto = datetime.now().minute
if minuto in impar:
    print("O minuto atual é impar")     
else:
    print("O minuto atual é par")