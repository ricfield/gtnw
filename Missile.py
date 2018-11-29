import random
class Missile(object):
   def __init__(target):
      self.target = target
   
   def fire():
      print("Firing missile on "+ target.city_name)
      
      hit = random.choice([True, False])
      
      if hit == True:
         print("Missile hit " + target.city_name)
      else:
         print("Missile missed " + target.city_name)


   
         
