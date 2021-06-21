'''
TODO
Use Open Weather API and Python to find weather of a city, display it and write to text file 'Weather Report.txt'

Add foll. parameters
1. Temperature
2. Description
3. Humidity
4. Wind Speed
'''
import requests
#import bs4
from datetime import datetime

api_key="b641ea93cb9bb30bb8d8c863b140b031"
units=[[1,['Fahrenheit', 'miles/hr'],'imperial'],[2,['Celcius', 'meters/s'],'metric'],[3,['Kelvin', 'meters/s'],'standard','']]

city=input("Enter name of desired city: ")

print("\nUnits:")
for unit in units:
    print("{}. {} : ({}, {})".format(unit[0],str(unit[2]).capitalize(), unit[1][0], unit[1][1]))
chosen_unit=int(input("Enter desired unit system: "))-1

url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+'&units='+units[chosen_unit][-1]
print("\n"+url)

r=requests.get(url)
w_data=r.json()
temp=str(w_data["main"]["temp"])+" "+units[chosen_unit][1][0]
w_desc=str(w_data["weather"][0]["description"]).title()
humidity=str(w_data["main"]["humidity"])+"%"
wind_speed=str(w_data["wind"]["speed"])+" "+units[chosen_unit][1][1]

'''
TESTER
initial_html=r.text
souped_html=bs4.BeautifulSoup(initial_html, 'html.parser')
print(souped_html.prettify())
print("\n"+souped_html.get_text())
'''
final_report=("="*12 + " WEATHER REPORT " + "="*12)+("\n"+city.title()+"\n"+ datetime.now().strftime("%d/%m/%Y \n%H:%M:%S"))+("\nDescription: {}\nTemperature: {}\nHumidity: {}\nWind Speed: {}\n".format(w_desc,temp,humidity,wind_speed))
print(final_report)

file=open("Weather Report.txt","w")
file.write(final_report)
file.close()