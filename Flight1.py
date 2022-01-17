import tello

# drone
drone = tello.Tello()

# Each leg of the box will be 100 cm. Tello uses cm units by default.
box_leg_distance = 100

# Yaw 90 degrees
yaw_angle = 90

# Yaw clockwise (right)
yaw_direction = "ccw"

# Put Tello into command mode
drone.send("command", 3)


# Send the takeoff command
drone.send("takeoff", 5)

# Fly box pattern
drone.send("forward " + str(box_leg_distance), 4)
drone.send("ccw " + str(yaw_angle), 3)
drone.send("forward " + str(box_leg_distance), 4)
drone.send("ccw " + str(yaw_angle), 3)
drone.send("forward " + str(box_leg_distance), 4)
drone.send("ccw " + str(yaw_angle), 3)
drone.send("forward " + str(box_leg_distance), 4)
drone.send("ccw " + str(yaw_angle), 3)
drone.send("forward " + str(box_leg_distance), 4)
drone.send("ccw " + str(yaw_angle), 3)

# Special : Flip backwards
drone.send("flip b ", 4)

# Send the land command
drone.send("land ", 4)



# Print message
print("Mission completed successfully!")

# Close the socket
drone.sock.close()