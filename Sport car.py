class SportsCar:
    def _init_(self, brand, model, horsepower, top_speed):
        self._brand = brand  # Encapsulation: Using a protected attribute
        self._model = model
        self._horsepower = horsepower
        self._top_speed = top_speed
    
    def display_info(self):
        return f"{self._brand} {self._model}: {self._horsepower} HP, Top Speed: {self._top_speed} mph"
    
    def accelerate(self):
        return f"The {self._model} accelerates rapidly!"

# LuxuryCar inherits from SportsCar
class LuxuryCar(SportsCar):
    def _init_(self, brand, model, horsepower, top_speed, comfort_level, autonomous_drive):
        super()._init_(brand, model, horsepower, top_speed)
        self._comfort_level = comfort_level  # Encapsulation: Using a protected attribute
        self._autonomous_drive = autonomous_drive  # Boolean indicating self-driving capability
    
    def display_info(self):  # Method overriding
        base_info = super().display_info()
        return f"{base_info}, Comfort: {self._comfort_level}, Autonomous Drive: {self._autonomous_drive}"
    
    def activate_massage_seats(self):
        return f"The {self._model}'s massage seats are activated for ultimate relaxation."
    
    def use_autonomous_mode(self):
        if self._autonomous_drive:
            return f"The {self._model} is now driving autonomously."
        else:
            return f"The {self._model} does not support autonomous driving."
    
# Example usage
luxury_car = LuxuryCar("Mercedes", "S-Class", 500, 155, "Ultra-luxury", True)
print(luxury_car.display_info())
print(luxury_car.accelerate())
print(luxury_car.activate_massage_seats())
print(luxury_car.use_autonomous_mode())