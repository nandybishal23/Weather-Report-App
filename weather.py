import tkinter as tk
import requests
import time
 

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2db6f8a81f749ecb7176108a80459b21"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    visibility = json_data['visibility']
    sunrise = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 19080))
    sunset = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunset'] - 19080))
    

    final_info = condition + "\n" +str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset + "\n" +"Visibility: " + str(visibility)
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("800x600")
canvas.title("Weather Report App")

f = ("poppins", 20, "bold")
t = ("poppins", 50, "bold")
p = ("Helvetica",35,"bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t, bg='coral',borderwidth=10, relief="groove")
textField.pack(pady = 10)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=p,fg='coral')
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()