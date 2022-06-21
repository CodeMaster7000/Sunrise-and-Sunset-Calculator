from tkinter import *
from geopy.geocoders import Nominatim
import datetime
from suntime import Sun

def sun():
	
	try:
		
		geolocator = Nominatim(user_agent="geoapiExercises")
		
		ladd1 = str(e.get())
		location1 = geolocator.geocode(ladd1)
		
		latitude = location1.latitude
		longitude = location1.longitude
		
		sun = Sun(latitude, longitude)

		time_zone = datetime.datetime.now()
		
		sun_rise = sun.get_local_sunrise_time(time_zone)
		sun_dusk = sun.get_local_sunset_time(time_zone)
		
		res_rise = sun_rise.strftime('%H:%M')
		res_dusk = sun_dusk.strftime('%H:%M')
		
		result1.set(res_rise)
		result2.set(res_dusk)
	
	except:
		result1.set("Sorry. Something went wrong.")

master = Tk()
master.configure(bg='light grey')
master.title("Sunrise and Sunset Calculator")

result1 = StringVar();
result2 = StringVar();

Label(master, text="Enter town/city: " ,
	bg = "light grey").grid(row=1, sticky=W)
Label(master, text="Sunrise:",
	bg = "light grey").grid(row=3, sticky=W)
Label(master, text="Sunset:",
	bg = "light grey").grid(row=4, sticky=W)

Label(master, text="", textvariable=result1,
	bg = "light grey").grid(row=3,column=1, sticky=W)
Label(master, text="", textvariable=result2,
	bg = "light grey").grid(row=4,column=1, sticky=W)


e = Entry(master,width = 50)
e.grid(row=1, column=1)


b = Button(master, text="Check",
		command=sun, bg = "white")
b.grid(row=1, column=2,columnspan=2,
	rowspan=2,padx=5, pady=5,)

mainloop()
