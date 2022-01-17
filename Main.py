import Window as GUI
import detect_mask_video as DMV
import queue
from djitellopy import Tello
from threading import Thread

def startGUI():
  print("startGUI()")
  global finish
  window = GUI.Window(drone, q)
  window.mainloop()

  finish = True

def startVideo():
  print("startVideo()")
  DMV.execute(drone, q)

def startDrone():
    drone = Tello()
    drone.connect()
    print(drone.get_battery())
    drone.streamon()
    return drone
  
if __name__ == "__main__":
    # drone = startDrone()
    drone='this drone'
    q = queue.Queue()
    videoThread = Thread(target=startVideo)
    videoThread.start()
    finish = False
    GUIThread = Thread(target=startGUI)
    GUIThread.start()
    GUIThread.join()
    videoThread.join()
