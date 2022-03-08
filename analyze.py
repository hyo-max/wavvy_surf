import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_wavvy.settings")
import django
django.setup()

from spot.models import ForcastData,Weather
import arrow
import requests
import schedule
import numpy as np

Weather.objects.all().delete()

forcastdata = ForcastData.objects.all()

for weather_list in forcastdata:
    def weather():
        start = arrow.now('UTC+9').floor('day')
        end = arrow.now('UTC+9').floor('day').shift(days=6)
        response = requests.get(
            'https://api.stormglass.io/v2/weather/point',
            params={
                'lat': weather_list.lat,
                'lng': weather_list.lng,
                'params': ','.join([
                    'airTemperature',  # 섭씨 온도
                    'waterTemperature',  # 물 섭씨 온도
                    'precipitation',  # kg / m²의 평균 강수량
                    'cloudCover',   #구름

                    'waveDirection',  # 파도 방향
                    'waveHeight',  # 파도 높이
                    'wavePeriod',  # 파도 주기

                    'windDirection',  # 바람 방향
                    'gust',  # 초당 미터 바람속도
                ]),
                'start': start.to('UTC+9').timestamp,  # Convert to UTC timestamp
                'end': end.to('UTC+9').timestamp  # Convert to UTC timestamp
            },
            headers={
                'Authorization': '46d92198-ad5f-11ea-954a-0242ac130002-46d92256-ad5f-11ea-954a-0242ac130002'
            }
        )
        # Do something with response data.
        json_data = response.json()
        # 데이터만 꺼네기
        data = json_data["hours"]
        data = data[::3] #3시간 단위로 변경

        # index 행
        b = []
        for i in data:
            weather = {
                'airTemperature': i['airTemperature']['noaa'],
                'gust': i['gust']['noaa'],
                'precipitation': i['precipitation']['noaa'],
                'cloudCover':i['cloudCover']['noaa'],

                'waterTemperature': i['waterTemperature']['noaa'],
                'waveDirection': i['waveDirection']['icon'],

                'waveHeight': round(i['waveHeight']['icon'],1),
                'wavePeriod': i['wavePeriod']['icon'],
                'windDirection': i['windDirection']['icon'],

            }
            b.append(weather)
        return b
    
        


    if __name__ == '__main__':
        weather_data = weather()
        ingu = weather_list
        
        for item in weather_data:
            Weather(
                spot = ingu,
                airTemperature=item['airTemperature'],
                gust=item['gust'],
                precipitation=item['precipitation'],
                cloudCover= item['cloudCover'],
                
                waterTemperature=item['waterTemperature'],
                waveDirection=item['waveDirection'],

                waveHeight=item['waveHeight'],
                wavePeriod=item['wavePeriod'],
                windDirection=item['windDirection']
                ).save()