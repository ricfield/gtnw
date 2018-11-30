from City import City
import random

MAX_HIT_POINTS = 100

usa_cities = [ City("a"), City("b"), City("c") ]
russia_cities = [ City("1"), City("2"), City("3") ]                                                 

def main():
   
   i = 1
   print("\n\nWelcome to Global Thermnonuclear War!.\n\n")
   print("1. USA")
   print("2. Russia")
   side = int(input("Choose a side: "))

   # USA side
   if side == 1:
       print("Attack targets:")
       for city in russia_cities:
          print(str(i) + ". " + city.city_name)
          i = i + 1
       
       keyin = int(input("Select a target: "))
       keyin -= 1  

       if keyin == 0:
          russia_cities[keyin].hit_points -= fire_missile(russia_cities[keyin])
          
          if russia_cities[keyin].hit_points > 0:
              print(russia_cities[keyin].city_name + " was not destroyed!")
              print(russia_cities[keyin].city_name + " has " + str(ussia_cities[keyin].hit_points) + " HP.")
          else:
              print(russia_cities[keyin].city_name + " was destroyed.")
       
       if keyin == 1:
          russia_cities[keyin].hit_points -= fire_missile(russia_cities[keyin])
          
          if russia_cities[int(keyin)].hit_points > 0:
              print(russia_cities[keyin].city_name +  " was not destroyed!")
              print(russia_cities[keyin].city_name + " has " + str(russia_cities[keyin].hit_points) + " HP.")
          else:
              print(russia_cities[keyin].city_name + " was destroyed.")
       
       if keyin == 2:
          russia_cities[keyin].hit_points -= fire_missile(russia_cities[keyin])
          
          if russia_cities[keyin].hit_points > 0:
              print(russia_cities[keyin].city_name + " was not destroyed!") 
              print(russia_cities[keyin].city_name + " has " + str(russia_cities[keyin].hit_points) + " HP.")
          
          else:
              print(russia_cities[keyin].city_name + " was destroyed.")
         
         
   # Russia side      
   #elif side == 2:
      # do stuff

         
def fire_missile(city):
   hit_points_lost = 0
   print("Firing missile on "+ city.city_name)
      
   hit = random.choice([True, False])
      
   if hit == True:
      print("Missile hit " + city.city_name)
      hit_points_lost = random.randint(1, MAX_HIT_POINTS)
   else:
       print("Missile missed " + city.city_name)
   
   print(str(hit_points_lost))     
   return hit_points_lost
         
         
if __name__ == '__main__':
   main()
   
   
