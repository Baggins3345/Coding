# This one was pretty easy compared to the last so i decided to add some extra stuff
# to make it harder and also make it more Canadian. So I added the option to do the 
# windchill in celcius and convert if wanted to. So I added a convert to celcius function
# also the wind chill calculation function, and added if else statments asking the user 
# if they want to convert and change the units and conversion accordingly, hope that makes sense. 

def cel_to_far(cel):
    return cel * (9/5) + 32
def far_to_cel(far):
    return (far - 32) * (5/9)
def cal_wind_chill_f(temp_f, wind_speed_mph):
    return 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed_mph ** 0.16) + 0.4275 * temp_f * (wind_speed_mph ** 0.16)
def cal_wind_chill_c(temp_c, wind_speed_kmh):
    return 13.12 + 0.6215 * temp_c - 11.37 * (wind_speed_kmh ** 0.16) + 0.3965 * temp_c * (wind_speed_kmh ** 0.16)

user_temp = float(input("What is the temperature? "))
cel_or_far = input("Fahrenheit or Celsius (F/C)? ").lower()

if cel_or_far == "c":
    convert_f = input("Would you like to convert to Fahrenheit (yes/no)? ").lower()
    if convert_f == "yes":
        user_temp = cel_to_far(user_temp)
        temp = "F"
        wind = "mph"
        for wind_speed in range(5,61,5):
            wind_chill = cal_wind_chill_f(user_temp, wind_speed)
            print(f"At temperature {user_temp:.1f}{temp}, and wind speed at {wind_speed} {wind}, the windchill is: {wind_chill:.2f}{temp}")
    else:
        temp = "C"
        wind = "km/h"
        for wind_speed in range(5,61,5):
            wind_chill = cal_wind_chill_c(user_temp, wind_speed)
            print(f"At temperature {user_temp:.1f}{temp}, and wind speed at {wind_speed} {wind}, the windchill is: {wind_chill:.2f}{temp}")


elif cel_or_far == "f":
    convert_f = input("Would you like to convert to Celsius (yes/no)? ")
    if convert_f == "yes":
        user_temp = far_to_cel(user_temp)
        temp = "C"
        wind = "kmh"
        for wind_speed in range(5,61,5):
            wind_chill = cal_wind_chill_c(user_temp, wind_speed)
            print(f"At temperature {user_temp:.1f}{temp}, and wind speed at {wind_speed} {wind}, the windchill is: {wind_chill:.2f}{temp}")
    else:
        temp = "F"
        wind = "mph"
        for wind_speed in range(5,61,5):
            wind_chill = cal_wind_chill_f(user_temp, wind_speed)
            print(f"At temperature {user_temp:.1f}{temp}, and wind speed at {wind_speed} {wind}, the windchill is: {wind_chill:.2f}{temp}")

