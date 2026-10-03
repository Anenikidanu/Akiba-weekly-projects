destination=input("Enter your travel destination: ")
distance=float(input("Enter the distance to your destination in kilometers: "))
speed=float(input("Enter your average speed in kilometers per hour: "))
time=distance/speed
minute=time*60
print("Destination: " + destination)
print(f"Distance : {distance} km")
print(f"Average speed : {speed} km/h")
print(f"\n Estimated Travel Time (in hour) : {time} hr")
print(f"Estimated Travel Time (in minutes) : {minute} min")
