import pyowm

owm = pyowm.OWM('09d46b1004c007a330052dcde0109616')  
observation = owm.weather_at_place("Mountain View,CA")  
w = observation.get_weather()  
wind = w.get_wind()  
temperature = w.get_temperature('celsius') 
#forecast = w.get_forecast() 
print(w)  
#print(wind) 
temp = str(temperature["temp"]) + "C"
#print forecast
