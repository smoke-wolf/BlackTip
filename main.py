import http.server
import json
import webbrowser
import socketserver
import folium
import requests
import time

from bs4 import BeautifulSoup

bannar = ('''
===================================================
  ____  _            _ _______ _             __     ____   _____ _____ _   _ _______   
 |  _ \| |          | |__   __(_)            \ \   / __ \ / ____|_   _| \ | |__   __|  
 | |_) | | __ _  ___| | _| |   _ _ __    _____\ \ | |  | | (___   | | |  \| |  | |     
 |  _ <| |/ _` |/ __| |/ / |  | | '_ \  |______\ \| |  | |\___ \  | | | . ` |  | |     
 | |_) | | (_| | (__|   <| |  | | |_) |         \ \ |__| |____) |_| |_| |\  |  | |     
 |____/|_|\__,_|\___|_|\_\_|  |_| .__/           \_\____/|_____/|_____|_| \_|  |_|     
                                | |                                                    
    -Interactive osint shell    |_|   Smoke-Wolf                                                 
===================================================

''')

options = '''
|| Emails & UserNames   || IP address & DNS  ||
||======================||===================||
|| [11] Instagram OSINT || [21] Basic WHOIS  ||   
|| [12] Email OSINT     || [22] Simple GeoIP ||
|| [13] Common UNs      || [23] Map View IP  || 
|| [13] Common UNs      || [24]
|| [13] Common UNs      || [25]
|| [13] Common UNs      || [26]
|| [13] Common UNs      || [27]
|| [13] Common UNs      || [28]
||======================||==================||
'''

target = '''
[*] Creating Attack Vector To Analyze: 

===================================================
||                 Target Vector                 ||
===================================================
|| TYPES: [0] Email [1] UserName [2] Phone Number||
||======  [3]
'''
def WHOIS():
    ipaddd = None
    time.sleep(0.7)
    print('[*] Launched WHOIS')
    print('if no input is given, process will use your own address for operation')
    ipaddd = input('target IP address: ')
    print(f'[*] IP target posed: {ipaddd}')
    time.sleep(0.3)
    if ipaddd is not None:
        ipadd = (f'/json/{ipaddd}')
        response = requests.get(f"http://ip-api.com{ipadd}")
        json_response = json.loads(response.text)
        print('[*] Analyzing Results')
        for key, value in json_response.items():
            if value:
                print(f"{key.title()}: {str(value).strip()}")
                time.sleep(0.2)
        input('[*] enter to continue')
    else:
        print('No input detected')

def view_html_file_locally(html_file_path, port=8000):
    # Start a simple HTTP server in the current directory
    with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{port}/")

        # Open the default web browser to view the HTML file
        webbrowser.open(f"http://localhost:{port}/{html_file_path}")

        # Start serving indefinitely until the user presses Ctrl+C
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

def generate_map():
    latitude = input('latitude: ')
    longitude = input('longitude: ')
    # Create a base map centered around the given latitude and longitude
    m = folium.Map(location=[latitude, longitude], zoom_start=10)

    # Add a marker at the specified location
    folium.Marker([latitude, longitude], tooltip='Location').add_to(m)

    # Save the map as an HTML file
    m.save('map.html')

    view_html_file_locally('map.html')


def Create_Target():
    pass

def GeoIP():
    print('connected to geoIP')
    time.sleep(0.3)
    ipadd = input('target IP address: ')
    response = requests.get(f"http://ipwhois.app/json/{ipadd}")
    json_response = json.loads(response.text)
    for key, value in json_response.items():
        if value:
            print(f"{key.title()}: {str(value).strip()}")
            time.sleep(0.12)
    input('enter to continue')

while True:
    print('\n'*50)
    print(bannar)
    print(options)
    option = input('Enter Desired Option: ')
    if '21' in option:
        print('[*] Launching WHOIS')
        WHOIS()
        print('[*] WHOIS Complete')
    elif '22' in option:
        print('[*] Launching GeoIP')
        GeoIP()
        print('[*] GeoIP Complete')
    elif '23' in option:
        print('[*] Launching MapView')
        generate_map()
        print('[*] MapView Complete')
