import tello

# Billy
billy = tello.Tello()

# Each leg of the box will be 100 cm. Tello uses cm units by default.
box_leg_distance = 100

# Yaw 90 degrees
yaw_angle = 90

# Yaw clockwise (right)
yaw_direction = "ccw"

# Put Tello into command mode
billy.send("command", 3)


# Send the takeoff command
billy.send("takeoff", 5)

# Fly box pattern
billy.send("forward " + str(box_leg_distance), 4)
billy.send("ccw " + str(yaw_angle), 3)
billy.send("forward " + str(box_leg_distance), 4)
billy.send("ccw " + str(yaw_angle), 3)
billy.send("forward " + str(box_leg_distance), 4)
billy.send("ccw " + str(yaw_angle), 3)
billy.send("forward " + str(box_leg_distance), 4)
billy.send("ccw " + str(yaw_angle), 3)
billy.send("forward " + str(box_leg_distance), 4)
billy.send("ccw " + str(yaw_angle), 3)

# Special : Flip backwards
billy.send("flip b ", 4)

# Send the land command
billy.send("land ", 4)



# Print message
print("Mission completed successfully!")

# Close the socket
billy.sock.close()