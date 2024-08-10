#Q3 Write a Python program that reads a JSON file containing NASA APOD data and prints the keys: "explanation","Title" Use this link to copy your json data (do not use request module, just save the Json to a variable then do json operation) 
#JSON Data url: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY 

import json
nasa_apod_data = '''
{
  "copyright": "NASA",
  "date": "2024-08-10",
  "explanation": "Why would the shadow of a space station look like a flying saucer? Because it is round. Specifically, this shadow is from China's Tiangong Space Station orbiting the Earth last week during a partial solar eclipse. The featured image was taken at the appropriately dramatic moment when the circular shadow crossed the cusp of the Sun. The foreground of the telescopic image features the Alborz Mountains in northern Iran. Although much smaller than the shadow of the Earth on the Moon during a lunar eclipse, for example, the space station's shadow was still large enough to be captured by several astrophotographers from different locations. In another coincidence, the main body of the space station spans about the same angle in the sky as its shadow on the Sun -- both about one third of an arcminute.",
  "hdurl": "https://apod.nasa.gov/apod/image/2408/TiangongShadow_Hosseini_960.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "A Flying Saucer on the Sun"
}
'''
data = json.loads(nasa_apod_data)
print("Title:", data.get("title"))
print("Explanation:", data.get("explanation"))
