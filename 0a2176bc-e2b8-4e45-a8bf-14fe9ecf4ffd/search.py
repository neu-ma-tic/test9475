#import statements
import json


#initiate base class that defines website
class EcoDataSearch:
  


#initiate for search parameters for key words and the url
  def key_words(user_message):
      words = user_message.split(' ')[1:]
      keywordsLower = ' '.join([str(item) for item in words])
      keywords = keywordsLower.title()
      return keywords
      


  def search(keyword):
    with open('jsonPlantData.json') as f:
      data = json.load(f)
      searchword = keyword
      
      importData = data.get(searchword)

      returnData = (json.dumps(importData, indent=1))
      #items = returnData.items()
      #splitData = ''
      #splitData(returnData)

      #print(items.type)


      #print(data.get(searchword))
      print(returnData)
      return returnData
      
       
