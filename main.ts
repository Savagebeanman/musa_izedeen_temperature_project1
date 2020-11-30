while (true) {
    console.log("The temperature is: " + input.temperature(TemperatureUnit.Fahrenheit))
    if (input.temperature(TemperatureUnit.Fahrenheit) >= 44) {
        light.clear()
        light.setPixelColor(0, light.rgb(255, 0, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 43) {
        light.clear()
        light.setPixelColor(1, light.rgb(255, 0, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 42) {
        light.clear()
        light.setPixelColor(2, light.rgb(255, 0, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 41) {
        light.clear()
        light.setPixelColor(3, light.rgb(255, 0, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 40) {
        light.clear()
        light.setPixelColor(4, light.rgb(255, 0, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 39) {
        light.clear()
        light.setPixelColor(5, light.rgb(0, 255, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 38) {
        light.clear()
        light.setPixelColor(6, light.rgb(0, 255, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 37) {
        light.clear()
        light.setPixelColor(7, light.rgb(0, 255, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 36) {
        light.clear()
        light.setPixelColor(8, light.rgb(0, 255, 0))
    } else {
        light.clear()
        light.setPixelColor(9, light.rgb(0, 255, 0))
    }
    
}
