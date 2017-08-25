import pyowm
import datetime
import time
from microdotphat import HEIGHT, write_string, scroll_vertical, show, clear

owm = pyowm.OWM('09d46b1004c007a330052dcde0109616')  
observation = owm.weather_at_place("Mountain View,CA") 
while True:	
	w = observation.get_weather()  
	#wind = w.get_wind()
	status = w.get_status()  
	temperature = w.get_temperature('fahrenheit')  

	temp = str(temperature["temp"]) + "F"

	t = datetime.datetime.now()    
	alltime = t.strftime('%I'+":"+'%M')

	lines = [status, temp, alltime]



	for line, text in enumerate(lines):
	    write_string(text, offset_y = line*7, kerning=False)

	show()

	while True:
	    time.sleep(1)
	    for x in range(7):
	        scroll_vertical()
	        show()
	        time.sleep(0.02)	