import requests as r
import json


# Dictionary functionality
apiurl = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'

def meaning(term):
  try: 
    term = apiurl+term
    result = r.get(term)
    temp = json.loads(result.text)
    meaning = temp[0]['meanings'][0]['definitions'][0]['definition']
    return meaning
  except:
    return "Sorry pal, we couldn't find definitions for the word you were looking for"
