class Planet:
    def __init__(self, name, planet, star):
        if not all(isinstance(i, str) for i in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        if name == "" or planet_type ==  "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
self.name = name
self.planet_type = planet_type
self.star = star
def orbit(self):
    return f"{self.name} is orbiting around {self.star}..."
def __str__(self):
    return "Planet: {name} | Type: {planet_type} | Star: {star}" 
planet_1 = Planet("Earth", "Terminal","Sun")
planet_2 = Planet("Jupiter", "Gas Gaint", "Sun")
planet_3 = Planet("Mars", "Tornstrial", "Sun")
print(planet_1)
print(planet_2)
print(planet_3)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())                 
               