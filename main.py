#!/usr/bin/env python
import PySimpleGUI as sg
from PIL import Image
import os
from Code import requests as req


#G_SIZE = (800,600)          # Size of the Graph in pixels. Using a 1 to 1 mapping of pixels to pixels

sg.theme('black')

# FIRST PAGE
# create txt file for private Riot Developer API key
if(not os.path.exists('apiKey.txt')):
    api = sg.popup_get_text('Input API Key')
    with open('apiKey.txt', 'w') as f:
        f.write(api)

#Enter summonerName 
summonerName = sg.popup_get_text('Enter Summoner Name')
champOut=req.call(summonerName)
# MAIN PAGE 
layout = [  
            [sg.Text('Click on the right side of the window to navigate forward, the left side to go backwards')],
            [sg.Text(champOut)]
            [sg.Text(f'Displaying image: '), sg.Text(k='-FILENAME-')]
            
            
            ]
window = sg.Window('League of Legends', layout, margins=(0,0),  use_default_focus=False, finalize=True)



while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
   


window.close()