import launchpad_py as launchpad
import sacn
import time

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
lp.Reset()

# set receiver
receiver = sacn.sACNreceiver()

# start receiving
receiver.start()

# join multicast
receiver.join_multicast(1)

# define a callback function
@receiver.listen_on('universe', universe=1)  # listens on universe 1

def callback(packet):

    # split up incoming data into RGB-Lists; one list for each LED
    L0 = [int(str(packet.dmxData[0:1]).strip('(),')), int(str(packet.dmxData[1:2]).strip('(),')), int(str(packet.dmxData[2:3]).strip('(),'))]

    L1 = [int(str(packet.dmxData[3:4]).strip('(),')), int(str(packet.dmxData[4:5]).strip('(),')), int(str(packet.dmxData[5:6]).strip('(),'))]

    L2 = [int(str(packet.dmxData[6:7]).strip('(),')), int(str(packet.dmxData[7:8]).strip('(),')), int(str(packet.dmxData[8:9]).strip('(),'))]

    L3 = [int(str(packet.dmxData[9:10]).strip('(),')), int(str(packet.dmxData[10:11]).strip('(),')), int(str(packet.dmxData[11:12]).strip('(),'))]

    L4 = [int(str(packet.dmxData[12:13]).strip('(),')), int(str(packet.dmxData[13:14]).strip('(),')), int(str(packet.dmxData[14:15]).strip('(),'))]

    L5 = [int(str(packet.dmxData[15:16]).strip('(),')), int(str(packet.dmxData[16:17]).strip('(),')), int(str(packet.dmxData[17:18]).strip('(),'))]

    L6 = [int(str(packet.dmxData[18:19]).strip('(),')), int(str(packet.dmxData[19:20]).strip('(),')), int(str(packet.dmxData[20:21]).strip('(),'))]

    L7 = [int(str(packet.dmxData[21:22]).strip('(),')), int(str(packet.dmxData[22:23]).strip('(),')), int(str(packet.dmxData[23:24]).strip('(),'))]

    L8 = [int(str(packet.dmxData[21:22]).strip('(),')), int(str(packet.dmxData[22:23]).strip('(),')), int(str(packet.dmxData[23:24]).strip('(),'))]

    # set colors
    lp.LedCtrlXYByRGB(0, 1, L0)
    lp.LedCtrlXYByRGB(1, 2, L1)
    lp.LedCtrlXYByRGB(2, 3, L2)
    lp.LedCtrlXYByRGB(3, 4, L3)
    lp.LedCtrlXYByRGB(4, 5, L4)
    lp.LedCtrlXYByRGB(5, 6, L5)
    lp.LedCtrlXYByRGB(6, 7, L6)
    lp.LedCtrlXYByRGB(7, 8, L7)
    lp.LedCtrlXYByRGB(8, 9, L8)
    lp.LedCtrlXYByRGB(0, 8, L0)
    lp.LedCtrlXYByRGB(1, 7, L1)
    lp.LedCtrlXYByRGB(2, 6, L2)
    lp.LedCtrlXYByRGB(3, 5, L3)
    lp.LedCtrlXYByRGB(4, 4, L4)
    lp.LedCtrlXYByRGB(5, 3, L5)
    lp.LedCtrlXYByRGB(6, 2, L6)
    lp.LedCtrlXYByRGB(7, 1, L7)
    lp.LedCtrlXYByRGB(8, 1, L8)
    lp.LedCtrlXYByRGB(8, 0, L8)

    # print out values for each LED
    #print('RawData: ' + str(packet.dmxData) + '\n' + '-' * 100)
    #print('LED0: ' + str(L0))
    #print('LED1: ' + str(L1))
    #print('LED2: ' + str(L2))
    #print('LED3: ' + str(L3))
    #print('LED4: ' + str(L4))
    #print('LED5: ' + str(L5))
    #print('LED6: ' + str(L6))
    #print('LED7: ' + str(L7))
    #print('LED8: ' + str(L8) + '\n' + '-' * 100 + '\n' + '-' * 100)

# receive for only x seconds
#time.sleep(x)
