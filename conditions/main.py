# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

weather = "sunny"  
#rainy sunny windy neutral
time_of_day = "day"
#day night
cow_milking_status = True
#true if milking is needed
location_of_the_cows = "pasture"
#pasture cowshed
season = "spring"
#winter spring summer fall
slurry_tank = False
#true if full
grass_status = True
#true if grass is long

tick = 0

def farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,slurry_tank,grass_status):
   if cow_milking_status == True and location_of_the_cows != "cowshed":
      location_of_the_cows = "cowshed"
      return "\n take cows to cowshed"
   elif location_of_the_cows == "pasture" and time_of_day == "night" or location_of_the_cows == "pasture" and weather =="rainy":
      location_of_the_cows = "cowshed"
      return "\n take cows to cowshed"
   elif location_of_the_cows == "cowshed" and cow_milking_status == True:
      cow_milking_status = False
      return "\n milk cows"
   elif  slurry_tank == True and location_of_the_cows == "cowshed" and weather != "sunny" or slurry_tank == True and location_of_the_cows == "cowshed" and weather != "windy":
      slurry_tank = False
      return "\n fertilize pasture"
   elif grass_status == True and season == "spring" and weather == "sunny" and location_of_the_cows == "pasture":
      location_of_the_cows = "cowshed"
      return "\n take cows to cowshed"
   elif grass_status == True and season == "spring" and weather == "sunny" and location_of_the_cows != "pasture":
      grass_status = False
      return "\n mow grass"
   else:
      return "\n wait"


while farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,slurry_tank,grass_status) != "wait" and tick < 20:
   print(farm_action(weather,time_of_day,cow_milking_status,location_of_the_cows,season,slurry_tank,grass_status))
   tick = tick + 1