import requests
import json




def get_meme():
  response = requests.get("https://meme-api.herokuapp.com/gimme")
  json_data = json.loads(response.content)
  return json_data["url"]
  #print(json_data)
  #meme = json_data["data"][random.randint(1,20)]["image"]
  #return meme

def generate_meme():
  response = requests.get("https://api.memegen.link/images/buzz/memes/memes_everywhere.png")
  return response.text
  



