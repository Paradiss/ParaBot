import ephem
from datetime import datetime

user_text_list = ['/planet']
user_text_list.append(input('Введи название планеты: '))  

ephem_planet = getattr(ephem, user_text_list[1].lower().capitalize())
ephem_planet_time = ephem_planet(datetime.today().strftime('%Y/%m/%d')) 
print(ephem.constellation(ephem_planet_time))
print(user_text_list[1]". Это что за покемон?")
