import ephem


planets_dict = {
                "Меркурий" : ephem.Mercury,
                "Венера" : ephem.Venus, 
                "Марс" : ephem.Mars, 
                "Mars" : ephem.Mars, 
                "Юпитер" : ephem.Jupiter, 
                "Сатурн" : ephem.Saturn, 
                "Уран" : ephem.Uranus, 
                "Нептун" :ephem.Neptune, 
                "Плутон" : ephem.Pluto, 
                "Луна" : ephem.Moon } 

planet = planets_dict["Луна"]

mars = planet("1575218963")
const = ephem.constellation(mars)
                 

print(const)