while True:  
    print("The temperature is: " + input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) >= 44:
        light.clear()
        light.set_pixel_color(0, light.rgb(255, 0, 0))
        
    elif input.temperature(TemperatureUnit.FAHRENHEIT)>=43:
        light.clear()
        light.set_pixel_color(1, light.rgb(255, 0, 0))

    elif input.temperature(TemperatureUnit.FAHRENHEIT)>=42:
        light.clear()    
        light.set_pixel_color(2, light.rgb(255, 0, 0))
    
    elif input.temperature(TemperatureUnit.FAHRENHEIT)>=41:
         light.clear()
         light.set_pixel_color(3, light.rgb(255, 0, 0))
    
    elif input.temperature(TemperatureUnit.FAHRENHEIT)>=40:
        light.clear()
        light.set_pixel_color(4, light.rgb(255, 0, 0))
    
    elif input.temperature(TemperatureUnit.FAHRENHEIT)>=39:
         light.clear()
         light.set_pixel_color(5, light.rgb(0, 255, 0))
    
    elif input.temperature(TemperatureUnit.FAHRENHEIT)>=38:
         light.clear()
         light.set_pixel_color(6, light.rgb(0, 255, 0))
    
    elif input.temperature(TemperatureUnit.FAHRENHEIT)>=37:
         light.clear()
         light.set_pixel_color(7, light.rgb(0, 255, 0))
    
    elif input.temperature(TemperatureUnit.FAHRENHEIT)>=36:
         light.clear()
         light.set_pixel_color(8, light.rgb(0, 255, 0))
    
    else :
         light.clear()
         light.set_pixel_color(9, light.rgb(0, 255, 0))
    
    