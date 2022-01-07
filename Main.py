import manual
import detect_mask_video
import time
from djitellopy import Tello
from threading import Thread

# task delegation:
def initGui():
  print("initGUI()")
  global finish
  manual.startWindow(drone)

  finish = True

def initVideo():
  print("initVideo()")
  detect_mask_video.execute(drone)
#   while not finish:
#       print('hello bois')

if __name__ == "__main__":

    drone = Tello()
    drone.connect()
    print(drone.get_battery())
    drone.streamon()

    # Run video thread after turning on video stream
    # videoThread = Thread(target=initVideo)
    # videoThread.start()

    drone.takeoff()
    # drone = 'This drone'
    finish = False
    GUIThread = Thread(target=initGui)
    GUIThread.start()
    
    GUIThread.join()
    # videoThread.join()
    # manual.init(drone)
  # detect_mask_video.init()



# task delegation:
# run drone on command list : done
# send withoutMask error from detect_mask_video to terminal : todo
# drone lands when camera starts and receive frame error (error photo in screenshot)
# stream still on, just drone landed


"""
1. prevent landing (done? to be tested)
2. send frames of "no mask" to GUI thread (or just print kat terminal) (asyraf)
3. mapping of drone path (alya)
4. 3 types of Drone Mode:
- predefined path (nik)
- input command list (done)
- remote control (guna keyboard) (danish)
- track face (low priority)
5. design GUI (including the logic) to include Drone Modes and takeoff/landing (Falan, izzati)

https://www.geeksforgeeks.org/python-communicating-between-threads-set-1/


"""



