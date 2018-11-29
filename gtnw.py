import City, random


usa_cities = [ City("Cheyenne"), City("Akron"), City("Cordova") ]
russia_cities = [ City("Moscow"), City("Vladivostok"), City("Leningrad") ]
                                                    

def main():
   print("\n\nWelcome to Global Thermnonuclear War!.\n\n
   print("1. USA")
   print("2. Russia")
   side = input("Choose a side: ")

   # USA side
   if side == 1:
       print("Attack targets:")
       for city in russia_cities:
          i = 1
          print(str(i) + ". " + city.city_name)
          i += 1
       
       keyin = input("Select a target: ")
  
       if keyin == 1:
          fire_missile(russia_cities[keyin])
          russia_cities[keyin].hit_points = russia_cities[1].hit_points - fire_missile(russia_cities[keyin])
          if russia_cities[keyin].hit_points > 0:
              print(russia_cities[keyin].city_name + " was not destroyed!")
          else:
              print(russia_cities[keyin].city_name + " was destroyed.")
       else if keyin == 2:
          fire_missile(russia_cities[keyin])
          russia_cities[keyin].hit_points = russia_cities[1].hit_points - fire_missile(russia_cities[keyin])
          if russia_cities[keyin].hit_points > 0:
              print(russia_cities[keyin].city_name +  " was not destroyed!")
          else:
              print(russia_cities[keyin].city_name + " was destroyed.")
       else if keyin == 3:
          fire_missile(russia_cities[keyin])
          russia_cities[keyin].hit_points = russia_cities[1].hit_points - fire_missile(russia_cities[keyin])
          if russia_cities[keyin].hit_points > 0:
              print(russia_cities[keyin].city_name + " was not destroyed!") 
          else:
              print(russia_cities[keyin].city_name + " was destroyed.")
         
         
   # Russia side      
   else if side == 2:
      # do stuff

         
def fire_missile(city):
   hit_points_lost = 0
   print("Firing missile on "+ city.city_name)
      
   hit = random.choice([True, False])
      
   if hit == True:
      print("Missile hit " + city.city_name)
      hit_points_lost = hit_points_lost - random.randint(1, MAX_HIT_POINTS)
      else:
         print("Missile missed " + target.city_name)
         
    return hit_points_lost
         
         
if __name__ == '__main__':
   main()
   
   
