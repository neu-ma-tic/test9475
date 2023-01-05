import discord
import requests
import json
from discord.ext import commands

client = commands.Bot(command_prefix = "/", case_insensitive = True)

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        return
    await client.process_commands(message)


@client.event
async def on_ready(): 
  print(f'[+] Yeaah, poze-bot connected!')

## START

@client.command()
async def start(ctx):
  await ctx.send(f'\n\n🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔𝗦: 🔍\n> ✅ • 𝗖𝗣𝗙:  /cpf 00000000000\n> ✅ • 𝗧𝗘𝗟𝗘𝗙𝗢𝗡𝗘:  /telefone 19996101067\n> ✅ • 𝗡𝗢𝗠𝗘:  /nome JAIR MESSIAS BOLSONARO\n> ✅ • 𝗣𝗟𝗔𝗖𝗔:  /placa ABC123\n> ✅ • 𝗖𝗡𝗣𝗝:  /cnpj 00000000000000\n> ✅ • 𝗕𝗜𝗡:  /bin 000000\n> ✅ • 𝗖𝗘𝗣:  /cep 00000000\n> ✅ • 𝗡𝗢𝗠𝗘 𝗣 𝗖𝗘𝗣:  /cep2 00000000\n> ✅ • 𝗜𝗣:  /ip 000000000\n> ✅ • 𝗖𝗢𝗩𝗜𝗗 𝟭𝟵:  /covid SP\n\n')



## CPF

@client.command()
async def cpf(ctx, cpf):
  data = requests.get(f"http://ifind.chapada.com.br:7777/?token=20491c06-5675-4e06-b2ae-4e3fcda2abdd&cpf=").text

  await ctx.send(data)

 ## CNPJ

@client.command()
async def cnpj(ctx, cnpj):
  data = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}").json()
  text = "🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗖𝗡𝗣𝗝 𝗥𝗘𝗔𝗟𝗜𝗭𝗔𝗗𝗔! 🔍 \n\n"

  try:
    error = data["error"]
    await ctx.send('⚠️ 𝗖𝗡𝗣𝗝 𝗡𝗔𝗢 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔𝗗𝗢!')
    return
  except Exception:
    pass

  text += f"> • 𝗖𝗡𝗣𝗝: {data['CNPJ']}\n"
  text += f"> • 𝗡𝗢𝗠𝗘 𝗙𝗔𝗡𝗧𝗔𝗦𝗜𝗔: {data['NOME FANTASIA']}\n"
  text += f"> • 𝗥𝗔𝗭𝗔𝗢 𝗦𝗢𝗖𝗜𝗔𝗟: {data['RAZAO SOCIAL']}\n"
  text += f"> • 𝗦𝗧𝗔𝗧𝗨𝗦: {data['STATUS']}\n"
  text += f"> • 𝗖𝗡𝗔𝗘 𝗗𝗘𝗦𝗖𝗥𝗜𝗖𝗔𝗢: {data['CNAE PRINCIPAL DESCRICAO']}\n"
  text += f"> • 𝗖𝗡𝗔𝗘 𝗖𝗢𝗗𝗜𝗚𝗢: {data['CNAE PRINCIPAL CODIGO']}\n"
  text += f"> • 𝗖𝗘𝗣: {data['CEP']}\n"
  text += f"> • 𝗗𝗔𝗧𝗔 𝗔𝗕𝗘𝗥𝗧𝗨𝗥𝗔: {data['DATA ABERTURA']}\n"
  text += f"> • 𝗗𝗗𝗗: {data['DDD']}\n"
  text += f"> • 𝗧𝗘𝗟𝗘𝗙𝗢𝗡𝗘: {data['TELEFONE']}\n"
  text += f"> • 𝗘𝗠𝗔𝗜𝗟: {data['EMAIL']}\n"
  text += f"> • 𝗧𝗜𝗣𝗢 𝗟𝗢𝗚𝗥𝗔𝗗𝗢𝗨𝗥𝗢: {data['TIPO LOGRADOURO']}\n"
  text += f"> • 𝗟𝗢𝗚𝗥𝗔𝗗𝗢𝗨𝗥𝗢: {data['LOGRADOURO']}\n"
  text += f"> • 𝗡𝗨𝗠𝗘𝗥𝗢: {data['NUMERO']}\n"
  text += f"> • 𝗖𝗢𝗠𝗣𝗟𝗘𝗠𝗘𝗡𝗧𝗢: {data['COMPLEMENTO']}\n"
  text += f"> • 𝗕𝗔𝗜𝗥𝗥𝗢: {data['BAIRRO']}\n"
  text += f"> • 𝗠𝗨𝗡𝗜𝗖𝗜𝗣𝗜𝗢: {data['MUNICIPIO']}\n"
  text += f"> • 𝗨𝗙: {data['UF']}\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"

  await ctx.send(text)

## TELEFONE
@client.command()
async def telefone(ctx, tel):
  data = requests.get(f"https://www.dualitybuscas.org/privado/consultar_telefone_api.php?consulta={tel}").text

  await ctx.send(data)


## NOME

@client.command()
async def nome(ctx, nome1):
  nome1 = nome1.replace(" ","%20")
  data = requests.get(f"http://ifind.chapada.com.br:7777/?token=20491c06-5675-4e06-b2ae-4e3fcda2abdd&nome1=").text

  await ctx.send(data)

## NOMES POR CEP

@client.command()
async def cep2(ctx, cep2):
  data = requests.get(f"https://dualitybuscas.org/privado/cep.php?consulta={cep2}").text

  await ctx.send(data)

## PLACA

@client.command()
async def placa(ctx, placa):
  data = requests.get(f"https://dualitybuscas.xyz/privado/placa.php?consulta={placa}").text

  await ctx.send(data)
## CEP

@client.command()
async def cep(ctx, cep):
  data = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

  if data.status_code != 200:
    await ctx.send("⚠️ 𝗖𝗘𝗣 𝗡𝗔𝗢 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔𝗗𝗢!")
    return

  data = data.json()

  text = "🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗖𝗘𝗣 𝗥𝗘𝗔𝗟𝗜𝗭𝗔𝗗𝗔! 🔍 \n\n"

  text += f"> • 𝗖𝗘𝗣: {data['cep']}\n"
  text += f"> • 𝗟𝗢𝗚𝗥𝗔𝗗𝗢𝗨𝗥𝗢: {data['logradouro']}\n"
  text += f"> • 𝗖𝗢𝗠𝗣𝗟𝗘𝗠𝗘𝗡𝗧𝗢: {data['complemento']}\n"
  text += f"> • 𝗕𝗔𝗜𝗥𝗥𝗢: {data['bairro']}\n"
  text += f"> • 𝗖𝗜𝗗𝗔𝗗𝗘: {data['localidade']}\n"
  text += f"> • 𝗘𝗦𝗧𝗔𝗗𝗢: {data['uf']}\n"
  text += f"> • 𝗜𝗕𝗚𝗘: {data['ibge']}\n"
  text += f"> • 𝗦𝗜𝗔𝗙𝗜: {data['siafi']}\n"
  text += f"> • 𝗗𝗗𝗗: {data['ddd']}\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"

  await ctx.send(text)

## BIN

@client.command()
async def bin(ctx, bin):
  data = requests.get(f"https://lookup.binlist.net/{bin}")

  if data.status_code != 200:
    await ctx.send("⚠️ 𝗕𝗜𝗡 𝗡𝗔𝗢 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔𝗗𝗢!")
    return

  data = data.json()
  
  text = "🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗕𝗜𝗡 𝗥𝗘𝗔𝗟𝗜𝗭𝗔𝗗𝗔! 🔍\n\n"

  text += f"> • 𝗕𝗜𝗡: {bin}\n"
  text += f"> • 𝗕𝗔𝗡𝗗𝗘𝗜𝗥𝗔: {data['scheme']}\n"
  text += f"> • 𝗧𝗜𝗣𝗢: {data['type']}\n"
  text += f"> • 𝗡𝗜𝗩𝗘𝗟: {data['brand']}\n"
  text += f"> • 𝗣𝗔𝗜𝗦: {data['country']['name']}\n"
  text += f"> • 𝗦𝗜𝗚𝗟𝗔: {data['country']['alpha2']}\n"
  text += f"> • 𝗕𝗔𝗡𝗗𝗘𝗜𝗥𝗔 𝗣𝗔𝗜𝗦: {data['country']['emoji']}\n"
  text += f"> • 𝗠𝗢𝗘𝗗𝗔: {data['country']['currency']}\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"

  await ctx.send(text)

## IP

@client.command()
async def ip(ctx, ip):
  data = requests.get(f"http://ip-api.com/json/{ip}").json()
  text = "🔍 𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔 𝗗𝗘 𝗜𝗣 𝗥𝗘𝗔𝗟𝗜𝗭𝗔𝗗𝗔! 🔍\n\n"

  if data["status"] != "success":
    await ctx.send('⚠️ 𝗜𝗣 𝗡𝗔𝗢 𝗘𝗡𝗖𝗢𝗡𝗧𝗥𝗔𝗗𝗢!')
    return

  text += f"> • 𝗣𝗔𝗜𝗦: {data['country']}\n"
  text += f"> • 𝗦𝗜𝗚𝗟𝗔 𝗣𝗔𝗜𝗦: {data['countryCode']}\n"
  text += f"> • 𝗘𝗦𝗧𝗔𝗗𝗢: {data['regionName']}\n"
  text += f"> • 𝗦𝗜𝗚𝗟𝗔 𝗘𝗦𝗧𝗔𝗗𝗢: {data['region']}\n"
  text += f"> • 𝗖𝗜𝗗𝗔𝗗𝗘: {data['city']}\n"
  text += f"> • 𝗖𝗘𝗣: {data['zip']}\n"
  text += f"> • 𝗟𝗔𝗧𝗜𝗧𝗨𝗗𝗘: {data['lat']}\n"
  text += f"> • 𝗟𝗢𝗡𝗚𝗜𝗧𝗨𝗗𝗘: {data['lon']}\n"
  text += f"> • 𝗙𝗢𝗥𝗡𝗘𝗖𝗘𝗗𝗢𝗥 𝗗𝗘 𝗜𝗡𝗧𝗘𝗥𝗡𝗘𝗧: {data['isp']}\n"
  text += f"> • 𝗘𝗠𝗣𝗥𝗘𝗦𝗔: {data['org']}\n"
  text += f"> • 𝗙𝗨𝗦𝗢 𝗛𝗢𝗥𝗔𝗥𝗜𝗢: {data['timezone']}\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"
  await ctx.send(text)

## COVID

@client.command()
async def covid(ctx, covid):
  data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()
  text = "🔍 𝗖𝗢𝗩𝗜𝗗𝟭𝟵 𝗕𝗥𝗔𝗦𝗜𝗟! 🔍\n\n"

  try:
    error = data["error"]
    await ctx.send('⚠️ 𝗘𝗦𝗧𝗔𝗗𝗢 𝗜𝗡𝗩𝗔𝗟𝗜𝗗𝗢!')
    return
  except Exception:
    pass

  text += f"> • 𝗘𝗦𝗧𝗔𝗗𝗢: {data['state']} - {data['uf']}\n"
  text += f"> • 𝗖𝗔𝗦𝗢𝗦: {data['cases']}\n"
  text += f"> • 𝗠𝗢𝗥𝗧𝗘𝗦: {data['deaths']}\n"
  text += f"> • 𝗖𝗔𝗦𝗢𝗦 𝗦𝗨𝗦𝗣𝗘𝗜𝗧𝗢𝗦: {data['suspects']}\n"
  text += f"> • 𝗖𝗔𝗦𝗢𝗦 𝗗𝗘𝗦𝗖𝗔𝗥𝗧𝗔𝗗𝗢𝗦: {data['refuses']}\n"
  text += f"> 𝗨𝗦𝗨𝗔𝗥𝗜𝗢: {ctx.author}\n\n"

  await ctx.send(text)

## SIM OU NÂO

@client.command()
async def eu(ctx):
  data = requests.get(f"https://yesno.wtf/api/?ref=devresourc.es").json()

  text = f"{data['image']}\n"

  await ctx.send(text)

## WHATSAPP

@client.command()
async def wpp(ctx, tel):

  info = ('💯 𝗦𝗘𝗨 𝗟𝗜𝗡𝗞 𝗣𝗔𝗥𝗔 𝗢 𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣:\n\n')
  data = ('> https://api.whatsapp.com/send?phone=')
  text = info + data + (tel)

  await ctx.send(text)

## INSTA

@client.command()
async def insta(ctx, insta):

  info = ('🍎 𝗦𝗘𝗨 𝗟𝗜𝗡𝗞 𝗣𝗔𝗥𝗔 𝗢 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠:\n\n')
  data = ('> https://www.instagram.com/')
  text = info + data + (insta)

  await ctx.send(text)

## GERADORES

## GERADOR DE CPF

@client.command()
async def gerarcpf(ctx):

    cpf = CPF()
    cpf = cpf.generate(True)

    text = ("• CPF GERADO:\n\n") + (cpf)
    await ctx.send(text)

client.run('ODg1MTgyNDgzNTk4MDIwNjI4.YTjUbQ.Sq8srAAHJnc6YlCo3UzfgECYIxw')
