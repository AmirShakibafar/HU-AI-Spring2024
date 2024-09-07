from classes.car import Car
from classes.parking import Parking
from classes.rush_hour import Rush_hour


# first map cars
main_car = Car(0, "h", main=True)
main_car.set_start(x=2, y=1)
main_car.set_end(x=2, y=2)

c1 = Car(1, orientation= "v")
c1.set_start(x=1, y=3)
c1.set_end(x=3, y=3)

c2 = Car(2, orientation= "v")
c2.set_start(x=2, y=4)
c2.set_end(x=3, y=4)

c3 = Car(3, orientation= "h")
c3.set_start(x=4, y=1)
c3.set_end(x=4, y=3)


# easy map
map_one = [main_car, c1, c2, c3]


####################################

#second map cars

main_car = Car(0, "h", main=True)
main_car.set_start(x=2, y=0)
main_car.set_end(x=2, y=1)

c1 = Car(1, orientation= "h")
c1.set_start(x=0, y=3)
c1.set_end(x=0, y=5)

c2 = Car(2, orientation= "h")
c2.set_start(x=3, y=0)
c2.set_end(x=3, y=1)

c3 = Car(3, orientation= "h")
c3.set_start(x=3, y=3)
c3.set_end(x=3, y=4)

c4 = Car(4, orientation= "h")
c4.set_start(x=4, y=2)
c4.set_end(x=4, y=3)

c5 = Car(5, orientation= "h")
c5.set_start(x=5, y=2)
c5.set_end(x=5, y=3)

c6 = Car(6, orientation= "v")
c6.set_start(x=4, y=0)
c6.set_end(x=5, y=0)

c7 = Car(7, orientation= "v")
c7.set_start(x=4, y=1)
c7.set_end(x=5, y=1)

c8 = Car(8, orientation= "v")
c8.set_start(x=2, y=2)
c8.set_end(x=3, y=2)

c9 = Car(9, orientation= "v")
c9.set_start(x=1, y=3)
c9.set_end(x=2, y=3)

c10 = Car(10, orientation= "v")
c10.set_start(x=2, y=5)
c10.set_end(x=4, y=5)

c11 = Car(11, orientation= "v")
c11.set_start(x=0, y=2)
c11.set_end(x=1, y=2)

#harder map
map_two = [main_car, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11]

# pass the map you want as the cars argument  

parking = Parking(w = 6, h = 6, g = 0, parent = None, cars = map_two)
game = Rush_hour(initial_state=parking)
game.run()

