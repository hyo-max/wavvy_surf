from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    )
from .models import ForcastData,Weather
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime,timedelta
from django.utils.dateformat import DateFormat
import numpy as np

def spot_list(request):
    spot_list = ForcastData.objects.all()
    south = ForcastData.objects.filter(category='1').order_by('title') #남해안
    east = ForcastData.objects.filter(category='2').order_by('title')  #동해안
    west = ForcastData.objects.filter(category='3').order_by('title')  #서해안
    jeju = ForcastData.objects.filter(category='4').order_by('title')  #제주
    
    return render(request, 'spot/spot_list.html',{
        'spot_list':spot_list,
        'south':south,
        'east':east,
        'west':west,
        'jeju':jeju,
        })


class SpotListView(ListView):
    model = ForcastData
    template_name = 'spot/spot_list.html'  # <app>/<model>_<viewtype>.html   
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 30

class SchoolDetailView(DetailView):
    model = ForcastData
    template_name = 'spot/spot_detail.html' 
    
    def get_context_data(self, **kwargs):   
        context = super(SchoolDetailView, self).get_context_data(**kwargs)
        r = ForcastData.objects.filter(pk=self.kwargs['pk']) #DetailView에서 PK 값 얻기
        # 날씨 가즈아
        #for title in r:
        #    weather = Weather.objects.get(spot = title.title.id) 
        
        #for weathers in weather:
        #   context['airTemperature'] = weathers.airTemperature.all()

        for title in r:
            context['weathers'] = Weather.objects.filter(spot = title.pk) 
        

        #food 맛집
        for f in r:
            context['food_tag'] = f.food_tag.all()
        #Surfschool 섳핑스쿨
        for s in r:
            context['surfshool_tag'] = s.surfshool_tag.all()
        #Accommodation  숙박싯설
        for a in r:
            context['accommodation_tag'] = a.accommodation_tag.all()
        #Coveniences  편의시설
        for c in r:
            context['coveniences_tag'] = c.coveniences_tag.all()

        t = ['월','화','수','목','금','토','일',]
        time2 = datetime.now()
        time3 = time2 + timedelta(days=1)
        time4 = time2 + timedelta(days=2)
        time5 = time2 + timedelta(days=3)
        time6 = time2 + timedelta(days=4)
        time7 = time2 + timedelta(days=5)
        context['day_time5'] = time5.strftime('%m.%d')
        context['day_time6'] = time6.strftime('%m.%d')
        context['day_time7'] = DateFormat(time7).format('m.d')
        context['mon'] = t[datetime.today().weekday()]
        context['tue'] = t[time3.weekday()]
        context['wed'] = t[time4.weekday()]
        context['thu'] = t[time5.weekday()]
        context['fri'] = t[time6.weekday()]
        context['sat'] = t[time7.weekday()]


        # 날씨 가즈아
        for title in r:
            weathers = Weather.objects.filter(spot = title.pk) 

        ##################파도 점수 계산####################
        waveHeight = []
        for w in weathers:
            waveHeight.append(round(w.waveHeight))
        
        waveHeight_score=[]
        for a in waveHeight:
            if 1.2 == a:
                waveHeight_score.append(100)
            elif 1.3 == a or 1.1 == a:
                waveHeight_score.append(90)
            elif 1.4 == a:
                waveHeight_score.append(85)
            elif 1.5 == a or 1.0 == a:
                waveHeight_score.append(80)
            elif 1.6 == a:
                waveHeight_score.append(75)
            elif 1.7 == a or 0.9 == a:
                waveHeight_score.append(70)
            elif 1.8 == a:
                waveHeight_score.append(65)
            elif 1.9 == a or 0.8 == a:
                waveHeight_score.append(60)
            elif 2.0 == a or 0.7 == a:
                waveHeight_score.append(50)
            elif 2.1 == a:
                waveHeight_score.append(45)
            elif 2.2 == a or 0.6 == a:
                waveHeight_score.append(40)
            elif 2.3 == a:
                waveHeight_score.append(35)
            elif 2.4 == a or 0.5 == a:
                waveHeight_score.append(30)
            elif 2.5 == a:
                waveHeight_score.append(25)
            elif 2.6 == a or 0.4 == a:
                waveHeight_score.append(20)
            elif 2.7 == a:
                waveHeight_score.append(15)
            elif 2.8 == a or 0.3 == a:
                waveHeight_score.append(10)
            elif 2.9 == a:
                waveHeight_score.append(5)
            else:
                waveHeight_score.append(0)    
            
        waveHeight_day1=waveHeight_score[2:7]
        waveHeight_day2=waveHeight_score[10:15]
        waveHeight_day3=waveHeight_score[18:23]
        waveHeight_day4=waveHeight_score[26:31]
        waveHeight_day5=waveHeight_score[34:39]
        waveHeight_day6=waveHeight_score[42:47]

        context['waveHeight_day1_score'] = np.mean(waveHeight_day1)
        context['waveHeight_day2_score'] = np.mean(waveHeight_day2)
        context['waveHeight_day3_score'] = np.mean(waveHeight_day3)
        context['waveHeight_day4_score'] = np.mean(waveHeight_day4)
        context['waveHeight_day5_score'] = np.mean(waveHeight_day5)
        context['waveHeight_day6_score'] = np.mean(waveHeight_day6)

        ########################################################
        #바람############################################################
        gust = []
        for g in weathers:
            gust.append(round(g.gust))
        
        gust_score=[]
        for a in gust:
            if 0 == a:
                gust_score.append(100)
            elif 1 == a:
                gust_score.append(95)
            elif 2 == a:
                gust_score.append(90)
            elif 3 == a:
                gust_score.append(85)
            elif 4 == a:
                gust_score.append(80)
            elif 5 == a:
                gust_score.append(75)
            elif 6 == a:
                gust_score.append(70)
            elif 7 == a:
                gust_score.append(65)
            elif 8 == a:
                gust_score.append(60)
            elif 9 == a:
                gust_score.append(55)
            elif 10 == a:
                gust_score.append(50)
            elif 11 == a:
                gust_score.append(45)
            elif 12 == a:
                gust_score.append(40)
            elif 13 == a:
                gust_score.append(35)
            elif 14 == a:
                gust_score.append(30)
            elif 15 == a:
                gust_score.append(25)
            elif 16 == a:
                gust_score.append(20)
            elif 17 == a:
                gust_score.append(15)
            elif 18 == a:
                gust_score.append(10)
            elif 19 == a:
                gust_score.append(5)
            else:
                gust_score.append(0) 
                
        gust_day1=gust_score[2:7]
        gust_day2=gust_score[10:15]
        gust_day3=gust_score[18:23]
        gust_day4=gust_score[26:31]
        gust_day5=gust_score[34:39]
        gust_day6=gust_score[42:47]
        gust_day7=gust_score[50:55]

        context['gust_day1_score'] = np.mean(gust_day1)
        context['gust_day2_score'] = np.mean(gust_day2)
        context['gust_day3_score'] = np.mean(gust_day3)
        context['gust_day4_score'] = np.mean(gust_day4)
        context['gust_day5_score'] = np.mean(gust_day5)
        context['gust_day6_score'] = np.mean(gust_day6)
        ############################################################
        #수온###########################################################
        waterTemperature = []
        for g in weathers:
            waterTemperature.append(round(g.waterTemperature))
        
        waterTemperature_score=[]
        for a in waterTemperature:
            if 0 == a:
                waterTemperature_score.append(100)
            elif 1 == a:
                waterTemperature_score.append(95)
            elif 2 == a:
                waterTemperature_score.append(90)
            elif 3 == a:
                waterTemperature_score.append(85)
            elif 4 == a:
                waterTemperature_score.append(80)
            elif 5 == a:
                waterTemperature_score.append(75)
            elif 6 == a:
                waterTemperature_score.append(70)
            elif 7 == a:
                waterTemperature_score.append(65)
            elif 8 == a:
                waterTemperature_score.append(60)
            elif 9 == a:
                waterTemperature_score.append(55)
            elif 10 == a:
                waterTemperature_score.append(50)
            elif 11 == a:
                waterTemperature_score.append(45)
            elif 12 == a:
                waterTemperature_score.append(40)
            elif 13 == a:
                waterTemperature_score.append(35)
            elif 14 == a:
                waterTemperature_score.append(30)
            elif 15 == a:
                waterTemperature_score.append(25)
            elif 16 == a:
                waterTemperature_score.append(20)
            elif 17 == a:
                waterTemperature_score.append(15)
            elif 18 == a:
                waterTemperature_score.append(10)
            elif 19 == a:
                waterTemperature_score.append(5)
            else:
                waterTemperature_score.append(0) 
                
        waterTemperature_score_day1=waterTemperature_score[2:7]
        waterTemperature_score_day2=waterTemperature_score[10:15]
        waterTemperature_score_day3=waterTemperature_score[18:23]
        waterTemperature_score_day4=waterTemperature_score[26:31]
        waterTemperature_score_day5=waterTemperature_score[34:39]
        waterTemperature_score_day6=waterTemperature_score[42:47]
        waterTemperature_score_day7=waterTemperature_score[50:55]

        context['waterTemperature_score_day1_score'] = np.mean(waterTemperature_score_day1)
        context['waterTemperature_score_day2_score'] = np.mean(waterTemperature_score_day2)
        context['waterTemperature_score_day3_score'] = np.mean(waterTemperature_score_day3)
        context['waterTemperature_score_day4_score'] = np.mean(waterTemperature_score_day4)
        context['waterTemperature_score_day5_score'] = np.mean(waterTemperature_score_day5)
        context['waterTemperature_score_day6_score'] = np.mean(waterTemperature_score_day6)
        ############################################################
        #기온###########################################################
        airTemperature = []
        for a in weathers:
            airTemperature.append(round(a.airTemperature))
        
        airTemperature_score=[]
        for a in airTemperature:
            if 24 <= a <= 30:
                airTemperature_score.append(100)
            elif 23 == a:
                airTemperature_score.append(95)
            elif 22 == a or 31 == a:
                airTemperature_score.append(90)
            elif 21 == a or 32 == a:
                airTemperature_score.append(85)
            elif 20 == a or 33 == a:
                airTemperature_score.append(80)
            elif 19 == a or 34 == a:
                airTemperature_score.append(75)
            elif 18 == a or 35 == a:
                airTemperature_score.append(70)
            elif 17 == a or 36 == a:
                airTemperature_score.append(65)
            elif 16 == a or 37 == a:
                airTemperature_score.append(60)
            elif 15 == a or 38 == a:
                airTemperature_score.append(55)
            elif 14== a or 39 == a:
                airTemperature_score.append(50)
            elif 13 == a:
                airTemperature_score.append(45)
            elif 12 == a:
                airTemperature_score.append(40)
            elif 11 == a:
                airTemperature_score.append(35)
            elif 10 == a:
                airTemperature_score.append(30)
            elif 9 == a:
                airTemperature_score.append(25)
            elif 8 == a:
                airTemperature_score.append(20)
            elif 7 == a:
                airTemperature_score.append(15)
            elif 4 <= a <= 6 or 40 <= a <=45:
                airTemperature_score.append(10)
            elif 0 <= a <= 3:
                airTemperature_score.append(5)
            else:
                airTemperature_score.append(0) 
                
        airTemperature_day1=airTemperature_score[2:7]
        airTemperature_day2=airTemperature_score[10:15]
        airTemperature_day3=airTemperature_score[18:23]
        airTemperature_day4=airTemperature_score[26:31]
        airTemperature_day5=airTemperature_score[34:39]
        airTemperature_day6=airTemperature_score[42:47]
        airTemperature_day7=airTemperature_score[50:55]

        context['airTemperature_day1_score'] = np.mean(airTemperature_day1)
        context['airTemperature_day2_score'] = np.mean(airTemperature_day2)
        context['airTemperature_day3_score'] = np.mean(airTemperature_day3)
        context['airTemperature_day4_score'] = np.mean(airTemperature_day4)
        context['airTemperature_day5_score'] = np.mean(airTemperature_day5)
        context['airTemperature_day6_score'] = np.mean(airTemperature_day6)
        ############################################################
        #tot score###########################################################
        context['day1_tot_score']= round(np.mean(waveHeight_day1 + gust_day1 + waterTemperature_score_day1 + airTemperature_day1))
        context['day2_tot_score']= round(np.mean(waveHeight_day2 + gust_day2 + waterTemperature_score_day2 + airTemperature_day2))
        context['day3_tot_score']= round(np.mean(waveHeight_day3 + gust_day3 + waterTemperature_score_day3 + airTemperature_day3))
        context['day4_tot_score']= round(np.mean(waveHeight_day4 + gust_day4 + waterTemperature_score_day4 + airTemperature_day4))
        context['day5_tot_score']= round(np.mean(waveHeight_day5 + gust_day5 + waterTemperature_score_day5 + airTemperature_day5))
        context['day6_tot_score']= round(np.mean(waveHeight_day6 + gust_day6 + waterTemperature_score_day6 + airTemperature_day6))


        return context
