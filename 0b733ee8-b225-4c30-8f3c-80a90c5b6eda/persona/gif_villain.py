import discord
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
import random


def get_html_soup(url: str):
    html = urlopen(url)
    soup = bs(html, "html.parser")
    return soup


async def gif_villain(message: discord.message.Message, top_n=5):
    content = message.content # 메세지 내용
    channel = message.channel # 메세지 보낸 채널

    query = quote_plus(content)
    url = f'https://tenor.com/search/{query}-gifs'
        
    soup = get_html_soup(url)
    
    gif_els = soup.findAll('div', 'Gif')
    gifs_top_n = gif_els[:top_n] if len(gif_els) >= top_n else gif_el
    gif_el = random.choice(gifs_top_n)
    gif_src = gif_el.img['src']
    
    await channel.send(gif_src) # 채널에 메세지 보내기
    return True
