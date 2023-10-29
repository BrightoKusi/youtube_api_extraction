import requests # This is a  Python library that is commonly used for making HTTP requests to interact with APIs. It allows you to send HTTP GET and POST requests to web servers and receive the HTML content of web pages, JSON data, or other resources.
import pandas as pd

from configparser import ConfigParser
config = ConfigParser()
config.read('.env')

['API']
base_url = config['API']['base_url']
api_key = config['API']['api_key']
search_endpoint = config['API']['search_endpoint']
part = config['API']['part']
username = config['API']['username']
channel_Id = config['API']['channel_Id']

uri = f'{base_url}/{search_endpoint}?key={api_key}&part={part}&channelId={channel_Id}&type={type}'

response = requests.get(uri)  # send an HTTP GET request to a specified URL and retrieve the content from the server
print(response.status_code)    # 200 means success

result = response.json()  #get content in json format
print(result)

items = result['items']   #get the values of the key 'items' in the dictionary result


all_videos = []

for item in items:   #extract information as a lisut
    obj = {}
    obj['channelTitle'] = item['snippet']['channelTitle']
    obj['videoID'] = item['id']['videoId']
    obj['videoTitle'] = item['snippet']['title']
    obj['description'] = item['snippet']['description']
    obj['publishedDate'] = item['snippet']['publishedAt']
    all_videos.append(obj)

print(all_videos)



df = pd.DataFrame(all_videos)  # convert to dataframe
print(df)

df.to_csv('videos_by_10Alytics.csv') #convert to csv file format











