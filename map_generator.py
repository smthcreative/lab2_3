'''
Program create html map of twitter friends
'''
import json
import folium
from geopy.geocoders import Nominatim


def read_json(path:str):
    '''
    Function read file json to the path in which
    we have friends location
    '''
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def find_location(data):
    '''
    Function
    >>> type(find_location(read_json('files/info.json')))
    <class 'set'>
    '''
    locations_of_user = set()
    for user in data['users']:
        name = user['screen_name']
        location = user['location']
        if location == '':
            continue
        locations_of_user.add((name, location, find_coordinate(location)))
    return locations_of_user


def find_coordinate(location):
    '''
    Function find coordinate of location
    >>> find_coordinate('Coventry,West Midlands,England,UK')
    (52.4081812, -1.510477)
    '''
    geolocator = Nominatim(user_agent="notme")
    try:
        location = geolocator.geocode(location)
        if location is not None:
            return (location.latitude, location.longitude)
    except AttributeError:
        return None


def create_map(data):
    '''
    Function create and save html
    file with name Map.html
    '''
    map = folium.Map(tiles="Stamen Terrain",
        location=[49.817545, 24.023932],
        zoom_start=17)
    folgroup = folium.FeatureGroup(name='Friend')
    for friend in data:
        folgroup.add_child(folium.Marker(location=[friend[2][0], friend[2][1]],
            popup=f'Name: {friend[0]}\nLocation: {friend[1]}', icon= folium.Icon()))
    map.add_child(folgroup)
    map.save('templates/Map.html')


def main():
    '''
    Function run process of creating a map of friend,
    logical function
    data: dictionaty
    '''
    path = 'files/info.json'
    data = read_json(path)
    data = find_location(data)
    create_map(data)

