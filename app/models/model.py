import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='89a14342bdfd49828106d735dca29e24',
                                                    client_secret='8343129f85bb4707b7406a0d65e630d2')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


rap_song_results=sp.search(q='genre:' + "rap", type='track', limit=10) 
rap_song_list=[]
for item in rap_song_results['tracks']['items']:
    rap_song_list.append({'name':item['name'], 'artists':item['artists'][0]['name'], 'link':item['external_urls']['spotify'], 'images':item['images'][0]['url']})
    
    

pop_song_results=sp.search(q='genre:' + "pop", type='track', limit=10)
pop_song_list=[]
for item in pop_song_results['tracks']['items']:
    pop_song_list.append({'name':item['name'], 'artists':item['artists'][0]['name'], 'link':item['external_urls']['spotify'], 'images':item['images'][0]['url']})
        
randb_song_results=sp.search(q='genre:' + "randb", type='track', limit=10)
randb_song_list=[]
for item in randb_song_results['tracks']['items']:
    randb_song_list.append({'name':item['name'], 'artists':item['artists'][0]['name'], 'link':item['external_urls']['spotify'], 'images':item['images'][0]['url']})
    
    
trap_song_results=sp.search(q='genre:' + "trap", type='track', limit=10)
trap_song_list=[]
for item in trap_song_results['tracks']['items']:
    trap_song_list.append({'name':item['name'], 'artists':item['artists'][0]['name'], 'link':item['external_urls']['spotify'], 'images':item['images'][0]['url']})
    
    
indie_song_results = sp.search(q='genre:' + "indie", type='track', limit = 10)
indie_song_list = []
for item in indie_song_results['tracks']['items']:
    indie_song_list.append({'name': item['name'], "artists": item['artists'][0]['name'], "Link": item['external_urls']['spotify'], "images": item['images'][0]['url']})
    
    
folk_song_results = sp.search(q='genre:' + "folk", type='track', limit = 10)
folk_song_list = []
for item in indie_song_results['tracks']['items']:
    folk_song_list.append({'name': item['name'], "artists": item['artists'][0]['name'], "Link": item['external_urls']['spotify'], "images": item['images'][0]['url']})
    
country_song_results = sp.search(q='genre:' + "country", type='track', limit = 10)
country_song_list = []
for item in country_song_results['tracks']['items']:
    country_song_list.append({'name': item['name'], "artists": item['artists'][0]['name'], "Link": item['external_urls']['spotify'], "images": item['images'][0]['url']})
    
electrical_song_results = sp.search(q='genre:' + "electrical", type='track', limit = 10)
electrical_song_list = []
for item in electrical_song_results['tracks']['items']:
    electrical_song_list.append({'name': item['name'], "artists": item['artists'][0]['name'], "Link": item['external_urls']['spotify'], "images": item['images'][0]['url']})
    
    
alternative_song_results = sp.search(q='genre:' + 'alternative', type='track', limit = 10)
alternative_song_list = []
for item in alternative_song_results['tracks']['items']:
    alternative_song_list.append({'name':item['name'], 'artists':item['artists'][0]['name'],'link':item['external_urls']['spotify'],'images':item['images'][0]['url']})
    

rock_song_results = sp.search(q='genre:' + 'rock', type='track', limit = 10)
rock_song_list = []
for item in rock_song_results['tracks']['items']:
    rock_song_list.append({'name':item['name'], 'artists':item['artists'][0]['name'],'link':item['external_urls']['spotify'], 'images':item['images']['url'][0]})
        
    
classical_song_results = sp.search(q='genre:' + 'classical', type='track', limit = 10)
classical_song_list = []
for item in classical_song_results['tracks']['items']:
    classical_song_list.append({'name':item['name'], 'artists':item['artists'][0]['name'],'link':item['external_urls']['spotify'], 'images':item['images'][0]['url']})
    

soul_song_results = sp.search(q='genre:' + 'soul', type='track', limit = 10)
soul_song_list = []
for item in soul_song_results['tracks']['items']:
    soul_song_list.append({'name':item['name'], 'artists':item['artists'][0]['name'],'link':item['external_urls']['spotify'], 'images':item['images'][0]['url']})

all_songs = {'Rap': rap_song_list, 'Pop': pop_song_list, 'R&B': randb_song_list, 'Trap': trap_song_list, 'Rock': rock_song_list, 'Alternative': alternative_song_list, 'Classical': classical_song_list, 'Soul': soul_song_list, 'Indie':indie_song_list, 'Electrical':electrical_song_list, 'Country':country_song_list, 'Folk':folk_song_list}
hgvu0ij-ok


