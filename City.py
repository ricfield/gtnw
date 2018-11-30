MAX_HIT_POINTS = 100


import random
class City:

   hit_points = MAX_HIT_POINTS

   def __init__(self, city_name):
      self.city_name = city_name
      random.seed()
   
   def rebuild():
      hit_points = random.randint(1, MAX_HIT_POINTS)
      print(self.city_name + " rebuilt with " + str(hit_points) + " hit points.")
      
   def destroy():
      hit_points = 0
      print(self.city_name + " destroyed.")
      
