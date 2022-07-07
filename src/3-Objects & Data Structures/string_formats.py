template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name='Earth', planet='The Earth', gravity=9.8))
#print(template.format(name=name, planet=planet, gravity=gravity))

string_immutable = 'Hello'
#string_immutable[2] = '1' # Immutable
print(string_immutable)
print(string_immutable.find('l'))