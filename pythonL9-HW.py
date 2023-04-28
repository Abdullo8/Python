def f(city):
    if city.lower() == "dushanbe":
        print(city + " population are more than 10M")
    if city.lower() == "russia":
        print(city + " population are more than 30M")

myCity = input("Write your city: ")

f(myCity)