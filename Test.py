import sacn
import time
import launchpad_py as launchpad
import keyboard
import time
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
from openrgb.utils import RGBColor

# set launchpad_py
lp = launchpad.Launchpad()
# check if launchpad is detected
if lp.Check(0, "mk2"):
    lp = launchpad.LaunchpadMk2()
    if lp.Open(0, "mk2"):
        print(" - Launchpad Mk2: OK")
    else:
        print(" - Launchpad Mk2: ERROR")
else:
    print(" - No Launchpad available")

# clear launchpad buffer
lp.ButtonFlush()

# provide an IP-Address to bind to if you want to send multicast packets from a specific interface
receiver = sacn.sACNreceiver()
receiver.start()  # start the receiving thread

# optional: if multicast is desired, join with the universe number as parameter
receiver.join_multicast(1)

r = range(9)

# define a callback function
@receiver.listen_on('universe', universe=1)  # listens on universe 1
def callback(packet):  # packet type: sacn.DataPacket
    print(str(packet.dmxData)[1:4].strip(','))  # print the received DMX data
    print(str(packet.dmxData)[4:7].strip(','))
    print(str(packet.dmxData)[7:10].strip(','))
    red = int(str(packet.dmxData)[1:4].strip(','))
    green = int(str(packet.dmxData)[4:7].strip(','))
    blue = int(str(packet.dmxData)[7:10].strip(','))
    clist = [red, green, blue]

    for n in r:
        lp.LedCtrlXYByRGB(0, n, clist)
        lp.LedCtrlXYByRGB(1, n, clist)
        lp.LedCtrlXYByRGB(2, n, clist)
        lp.LedCtrlXYByRGB(3, n, clist)
        lp.LedCtrlXYByRGB(4, n, clist)
        lp.LedCtrlXYByRGB(5, n, clist)
        lp.LedCtrlXYByRGB(6, n, clist)
        lp.LedCtrlXYByRGB(7, n, clist)
        lp.LedCtrlXYByRGB(8, n, clist)


time.sleep(100)  # receive for 10 seconds

# optional: if multicast was previously joined
receiver.leave_multicast(1)

receiver.stop()