import requests
import json


def fetch_joke(json_data):
  if('joke' not in json_data):
    joke = json_data['setup'] + " \n " + json_data['delivery']
    print(joke)
    return joke
  
  else:
    joke = json_data['joke']
    print(joke)
    return joke

#get joke from the API
def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Any")
  json_data = json.loads(response.content)
  #joke_question = json_data.setup
  #print(joke_answer)
  return fetch_joke(json_data)



  
def search_joke(query):
  response = requests.get("https://v2.jokeapi.dev/joke/Any?contains={0}".format(query))
  json_data = json.loads(response.content)
  return fetch_joke(json_data)

  #joke_question = json_data.setup
  #print(joke_answer)