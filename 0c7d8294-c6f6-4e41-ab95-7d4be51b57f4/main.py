# -*- coding: utf-8 -*-
import discord
import os
import json
import time
from dotenv import load_dotenv
from pathlib import Path


def openJsonFile(fileName) :
    file = "/data/" + fileName + ".json"
    print(f"trying to open : {file}")
    try:
        with open(file, 'r') as f :
            data = json.load(f)
            #print(data)
            f.close()
            return data
    except :
        print(f"error while opening '{file}'")
    

def writeToJson(fileName, data):
    with open(f"/data/{fileName}.json", 'w') as file:
        json.dump(data, file, indent=4)
        file.close()
        print(f"{fileName}.json was successfully writed !")


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._jsonFile = "findedItems"
        self._jsonFE = "liensNvidiaFE"
        self._model = ""
        self._findedObjects = {}
        print("Hello world !")
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.bg_drop())
        #self.bg_task2 = self.loop.create_task(self.bg_drop2())

    def getDataFromJson(self,filename):
        json = openJsonFile(filename)
        if json:
            for products in json.values():
                print(f"products: {products}")
                for model, product in products.items():
                    print(f"model: {model}")
                    for website in product.values():
                          print(model)
                          for id, values in website.items():
                              print(f"id : {id}")
                              self._findedObjects[id] = [model, values[0], values[1], values[2]]
                              print(f"_findedObjects[{id}] : {self._findedObjects[id]}")
            writeToJson(filename, {})

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def bg_drop(self):
        # print("WESH")
        await self.wait_until_ready()
        #channel_3090_fe = self.get_channel(817504026894663721)
        #channel_3080_fe = self.get_channel(817440964511662163)
        #channel_3070_fe = self.get_channel(817503955970031657)
        channel_test_dev = self.get_channel(842323144878719006)
        channel_nvidia_fe = self.get_channel(817503991649927198)
        channel_3090 = self.get_channel(817788761265668107)
        channel_3080 = self.get_channel(817788733877125180)
        channel_3070 = self.get_channel(817788812042305577)
        channel_3060ti = self.get_channel(817788850155028500)
        channel_3060 = self.get_channel(817788876251988029)
        channel_ps5= self.get_channel(818073118383407115)
        channel_xbox = self.get_channel(818073227254300693)
        channel_6800 = self.get_channel(818072967333412929)
        channel_6900xt = self.get_channel(818073000314142720)
        channel_6800xt = self.get_channel(818073023629754379)
        channel_6700xt = self.get_channel(830788170605002763)
        
        while not self.is_closed():     
            self.getDataFromJson(self._jsonFile)
            if self._findedObjects:
                for values in self._findedObjects.values():
                    model = values[0]
                    url = values[1]
                    price = values[2]+"€"
                    description = values[3]

                    if model == "RTX 3090" :
                        await channel_3090.send('<@&820051152023322635> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "RTX 3080" : 
                        await channel_3080.send('<@&820051152758243328> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "RTX 3070" : 
                        await channel_3070.send('<@&820051153722015784> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "RTX 3060TI" : 
                        await channel_3060ti.send('<@&820051153826873354> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "RTX 3060" : 
                        await channel_3060.send('<@&820051154485903390> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "NVIDIA_FE" : 
                        await channel_nvidia_fe.send('<@&820050460055961631> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "6900XT" : 
                        await channel_6900xt.send('<@&820051154713051187> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "6800XT" : 
                        await channel_6800xt.send('<@&820054444292833330> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "6800" : 
                        await channel_6800.send('<@&820054444397559838> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "6700XT" : 
                        await channel_6700xt.send('<@&820054448936058940> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "PS5" : 
                        await channel_ps5.send('<@&820054456339005485> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "XBOX" : 
                        await channel_xbox.send('<@&820054457266077757> {}€ NEW DROP \n {} \n {}'.format(price,url,description))
                    elif model == "TEST" : 
                        await channel_test_dev.send('<@&820050456369823745> {}€ DEV TEST DROP \n {} \n {}'.format(price,url,description))
                self._findedObjects = {}
            else:
                time.sleep(1)

dotenv_path = Path('/app/.env')
load_dotenv(dotenv_path=dotenv_path)
token = os.getenv("TOKEN")
client = MyClient()
if token is None:
    print("Please specify a token in your env")
else:
    client.run(token)