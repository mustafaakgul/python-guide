
thisdict = {
  "brand": "Ford",
  "year": 1964
}

thisdict2 = {
  "model": "Mustang",
  "year": 1964
}

print(thisdict.get("model", False) or thisdict2.get("model", False))