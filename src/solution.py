import os

input_file = open("inputs/a_example.in","r")
first_line = input_file.readline()
first_line_split = first_line.split(" ")

city = []
for item in first_line_split:
    city.append(int(item))

rows = city[0]
columns = city[1]
fleet = city[2]
rides = city[3]
bonus = city[4]
sim_steps = city[5]

rides = {}
ride_details = []
for ride in range(0, rides):
    ride_dets = input_file.readline().split(" ")
    for det in ride_dets:
        ride_details.append(int(det))
    rides[ride].append(ride_details)

print city
print rows
print columns
print rides
