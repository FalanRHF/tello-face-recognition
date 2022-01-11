import tello

# Create Billy
billy = tello.Tello()

# Flight path from Station 1 to all station sequentially
station = [[2, "cw", 90, "forward", 100], [3, "ccw", 90, "forward", 80], [4, "ccw", 90, "forward", 40],
           [5, "ccw", 90, "forward", 40], [6, "cw", 90, "forward", 60], [1, "ccw", 90, "forward", 40]]

# Set destination
destination = 2

# Put Tello into command mode
billy.send("command", 3)

# Send the takeoff command
billy.send("takeoff", 7)

# Start at Station 1 and print destination
print("Start at Station 1")
print("Destination: " + str(destination) + "\n")

# Billy's flight path
for i in range(len(station)):
    print("Current location: Station " + str(station[i][0]-1) + "\n")
    # If arrive at destination station, land for a while, then takeoff again
    if (station[i][0]-1) == destination:
        billy.send("land", 3)
        print("Land at Station " + str(station[i][0]) + "\n")
        billy.send("takeoff", 10)
        print("Takeoff again at " + str(station[i][0]) + "\n")
    # print(station[i][1] + " " + str(station[i][2]) + "\n")
    # Turn cw or ccw
    billy.send(station[i][1] + " " + str(station[i][2]), 4)
    # print(station[i][3] + " " + str(station[i][4]) + "\n")
    # Move forward
    billy.send(station[i][3] + " " + str(station[i][4]), 4)

# Reach back at Station 1
print("Arrived home")

# Turn to original direction before land
billy.send("cw 180", 4)

# Land
billy.send("land", 3)


# Close the socket
billy.sock.close()


