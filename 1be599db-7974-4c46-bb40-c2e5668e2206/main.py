from hcapbypass import bypass
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from random import randint
import os, shutil
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


driver.get('https://discord.com/login')
channel_url = 'https://discord.com/channels/880378349166428180/882846115127517224'

email = driver.find_element_by_name("email")
passwd = driver.find_element_by_name("password")

email.send_keys("nitish191206@gmail.com")
print('Given email......')
passwd.send_keys("jmd@8287339159")
print('Given Password')

button = driver.find_element_by_class_name('button-3k0cO7')
button.click()
print(">>Login Complete......")

time.sleep(2)


time.sleep(2)

# <div id="checkbox" aria-haspopup="true" aria-checked="false" role="checkbox" tabindex="0" aria-live="assertive" aria-labelledby="a11y-label" style="position: absolute; width: 28px; height: 28px; border-width: 1px; border-style: solid; border-color: rgb(145, 145, 145); border-radius: 4px; background-color: rgb(250, 250, 250); top: 0px; left: 0px;"></div>


time.sleep(40)
print('Waiting to open the server link.....')

driver.get(channel_url)
print(">Opening The Server Link.....")
time.sleep(5)


msg = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')
print('Accessing the message box.....')

# while True:
#     msg.click()
#     msg_rob = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')
#     msg_rob.send_keys('pls with 500')
#     msg_rob.send_keys(Keys.ENTER)
#     time.sleep(2)
#     msg_rob.send_keys('pls rob @TECHNOBLADE')
#     msg_rob.send_keys(Keys.ENTER)

    
#     time.sleep(30)


# msg.send_keys('BOT_automation_test')
# msg.send_keys(Keys.ENTER)
while True:
    msg.click()
    msg_fish = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')
    msg_fish.send_keys('pls fish')
    msg_fish.send_keys(Keys.ENTER)
    print('asking for fishing......')
    time.sleep(5)
    
    msg_hunt = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')
    msg_hunt.send_keys('pls hunt')
    msg_hunt.send_keys(Keys.ENTER)
    print('asking for hunting......')
    time.sleep(5)
    
    msg_dig = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')
    msg_dig.send_keys('pls dig')
    msg_dig.send_keys(Keys.ENTER)
    print('asking for digging......')
    time.sleep(5)
    
    msg_sell = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')
    msg_sell.send_keys('pls sell sand max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling sand......')
    time.sleep(2)

    msg_sell.send_keys('pls sell garbage max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling garbage......')
    time.sleep(2)

    msg_sell.send_keys('pls beg')
    msg_sell.send_keys(Keys.ENTER)
    print('begging:( ......')
    time.sleep(2)

    msg_sell.send_keys('pls sell skunk max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling skunk......')
    time.sleep(2)

    msg_sell.send_keys('pls sell junk max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling junk......')
    time.sleep(2)

    msg_sell.send_keys('pls sell ant max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling ant......')
    time.sleep(2)

    msg_sell.send_keys('pls sell bread max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling bread......')
    time.sleep(2)

    msg_sell.send_keys('pls sell deer max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling deer......')
    time.sleep(2)

    msg_sell.send_keys('pls sell duck max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling duck......')
    time.sleep(2)

    msg_sell.send_keys('pls sell common fish max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling fish......')
    time.sleep(2)

    msg_sell.send_keys('pls sell rarefish max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling rare fish......')
    time.sleep(2)

    msg_sell.send_keys('pls sell exoticfish max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling exoticfish......')
    time.sleep(2)

    msg_sell.send_keys('pls sell rabbit max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling rabbit......')
    time.sleep(2)

    msg_sell.send_keys('pls sell Seaweed max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling seaweed......')
    time.sleep(2)
    
    msg_sell.send_keys('pls sell Jellyfish max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling jellyfish......')    
    time.sleep(2)
    
    msg_sell.send_keys('pls sell worm max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling worm......')
    time.sleep(2)
    
    msg_sell.send_keys('pls sell ladybug max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling ladybug......')
    time.sleep(2)
    
    msg_sell.send_keys('pls sell stickbug max')
    msg_sell.send_keys(Keys.ENTER)
    print('selling stickbug......')
    time.sleep(2)
    
    msg_sell.send_keys('pls dep max')
    msg_sell.send_keys(Keys.ENTER)
    print('depositing all coins......')
    time.sleep(2)
    
    msg_sell.send_keys('pls bal')
    msg_sell.send_keys(Keys.ENTER)
    print('selling garbage......')
    
    
    # msg_sell.send_keys('pls use banknote max')
    # msg_sell.send_keys(Keys.ENTER)
    # msg_sell.send_keys('all')
    # msg_sell.send_keys(Keys.ENTER)
    # print('using banknote if any.......')    

    # time.sleep(4)
    # msg_dig.send_keys('pls search')
    # msg_dig.send_keys(Keys.ENTER)    
    # time.sleep(2)
    # msg_dig.send_keys('pls hl')
    # msg_dig.send_keys(Keys.ENTER)
    # time.sleep(2)
    # msg_dig.send_keys('pls pm')
    # msg_dig.send_keys(Keys.ENTER)  
    # time.sleep(40)







    






# <button type="button" class="component-1IAYeC button-38aScr lookFilled-1Gx00P colorGrey-2DXtkV sizeSmall-2cSMqn grow-q77ONN" disabled=""><div class="contents-18-Yxp"><div class="content-2wNArO" aria-hidden="false"><div class="label-3aEGGA">dresser</div></div></div></button>


#30s gap in searching

# msg_search = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')
# msg_search.send_keys('pls search')
# msg_search.send_keys(Keys.ENTER)
# msg_search = driver.find_element_by_class_name('component-1IAYeC')
# msg_search.click()

# <button role="button" type="button" class="component-1IAYeC button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN"><div class="contents-18-Yxp"><div class="content-2wNArO" aria-hidden="false"><div class="label-3aEGGA">dresser</div></div></div></button>
# <button role="button" type="button" class="component-1IAYeC button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN"><div class="contents-18-Yxp"><div class="content-2wNArO" aria-hidden="false"><div class="label-3aEGGA">dresser</div></div></div></button>
# msg = driver.find_element_by_class_name('textArea-12jD-V')
# msg.click()
# msg.send_keys('hello')

# <div class="textArea-12jD-V textAreaSlate-1ZzRVj slateContainer-3Qkn2x"><div class="placeholder-37qJjk fontSize16Padding-3Wk7zP" aria-hidden="true">Message #bot-spam</div><div aria-label="Message #bot-spam" aria-multiline="true" data-can-focus="true" data-slate-editor="true" data-key="0" contenteditable="true" class="markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP" autocorrect="off" spellcheck="true" role="textbox" data-gramm="false" style="outline: none; white-space: pre-wrap; overflow-wrap: break-word; -webkit-user-modify: read-write-plaintext-only;"><div data-slate-object="block" data-key="1" style="position: relative;"><span data-slate-object="text" data-key="2"><span data-slate-leaf="true" data-offset-key="2:0"><span data-slate-zero-width="z" data-slate-length="0">﻿<br></span></span></span></div></div></div>
# <div class="backdrop-1wrmKB withLayer-RoELSG" style="opacity: 0.85; background: hsl(0, calc(var(--saturation-factor, 1) * 0%), 0%);"></div>
# class="layerContainer-yqaFcK"
# //*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]