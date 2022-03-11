import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_wavvy.settings")
import django
django.setup()

from spot.models import ForcastData,Weather
import arrow
import requests
import schedule
import my_settings

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
                'Authorization': my_settings.STORM_GLASS_KEY
            }
        )
        # Do something with response data.
        json_data = response.json()
        # 데이터만 꺼네기
        data = json_data["hours"]
        data = data[::3] #3시간 단위로 변경

        # index 행
        a = []
        for i in data:
            weather = {
                'airTemperature': i['airTemperature']['noaa'],
                'gust': i['gust']['noaa'],
                'precipitation': i['precipitation']['noaa'],
                'cloudCover':i['cloudCover']['noaa'],

                'waterTemperature': i['waterTemperature']['noaa'],
                'waveDirection': i['waveDirection']['icon'],

                'waveHeight': i['waveHeight']['icon'],
                'wavePeriod': i['wavePeriod']['icon'],
                'windDirection': i['windDirection']['icon']
            }
            a.append(weather)
        return a


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