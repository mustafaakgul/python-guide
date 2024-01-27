planet = {
    'name': 'Earth',
    'moons': 1
}
print(f'{planet["name"]} has {planet["moons"]} moon(s)')

print(planet['name'])
print(planet.get('Earth'))
planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

planet.pop('orbital period')

planet['orbital period'] = 4333

planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')


planet = {
    'name': 'Mars',
    'moons': 2
}
print(f'{planet["name"]} has {planet["moons"]} moon(s)')
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')


rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')


planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
total_planets = len(planet_moons.keys())