"""
||  OPERADOR    ||      COMPARACION     ||
||==============||======================||
||      and     ||   SE CUMPLE A Y B    ||
||      or      ||   SE CUMPLE A O B    ||
||      not     ||         NO A         ||
"""

r = 10 == 10 and 10 >= 10
print(r)
print('=======')

r = 5 < 10 or 5 > 10
print(r)
print('=======')

#UN NOT DELANTE NIEGA TODO DE SER TRUE A FALSE
r = not 10 == 10 and 10 >= 10
print(r)
print('=======')