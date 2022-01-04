import manual
import detect_mask_video
import time
from djitellopy import tello
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

    # drone = Tello()
    # drone.connect()
    # print(drone.get_battery())
    # drone.streamon()
    drone = 'This drone'
    finish = False
    GUIThread = Thread(target=initGui)
    GUIThread.start()

    videoThread = Thread(target=initVideo)
    videoThread.start()
    
    GUIThread.join()
    videoThread.join()
    # manual.init(drone)\
  # detect_mask_video.init()



# task delegation:
# run drone on command list : done
# send withoutMask error from detect_mask_video to terminal : todo
# buat github repo: todo
# test drone: todo
