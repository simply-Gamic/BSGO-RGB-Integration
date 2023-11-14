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

r = range(9)

# set receiver
receiver = sacn.sACNreceiver()

# start receiving
receiver.start()

# define a callback function
@receiver.listen_on('universe', universe=1)  # listens on universe 1

def callback(packet):

    # split up incoming data into chunks of RGB values, 3 values for one LED

    #LED0
    Red0 = str(packet.dmxData[0:1]).strip('(),')
    Green0 = str(packet.dmxData[1:2]).strip('(),')
    Blue0 = str(packet.dmxData[2:3]).strip('(),')

    L0 = [int(Red0), int(Green0), int(Blue0)]

    # LED1
    Red1 = str(packet.dmxData[3:4]).strip('(),')
    Green1 = str(packet.dmxData[4:5]).strip('(),')
    Blue1 = str(packet.dmxData[5:6]).strip('(),')

    L1 = [int(Red1), int(Green1), int(Blue1)]

    # LED2
    Red2 = str(packet.dmxData[6:7]).strip('(),')
    Green2 = str(packet.dmxData[7:8]).strip('(),')
    Blue2 = str(packet.dmxData[8:9]).strip('(),')

    L2 = [int(Red2), int(Green2), int(Blue2)]

    # LED3
    Red3 = str(packet.dmxData[9:10]).strip('(),')
    Green3 = str(packet.dmxData[10:11]).strip('(),')
    Blue3 = str(packet.dmxData[11:12]).strip('(),')

    L3 = [int(Red3), int(Green3), int(Blue3)]

    # LED4
    Red4 = str(packet.dmxData[12:13]).strip('(),')
    Green4 = str(packet.dmxData[13:14]).strip('(),')
    Blue4 = str(packet.dmxData[14:15]).strip('(),')

    L4 = [int(Red4), int(Green4), int(Blue4)]

    # LED5
    Red5 = str(packet.dmxData[15:16]).strip('(),')
    Green5 = str(packet.dmxData[16:17]).strip('(),')
    Blue5 = str(packet.dmxData[17:18]).strip('(),')

    L5 = [int(Red5), int(Green5), int(Blue5)]

    # LED6
    Red6 = str(packet.dmxData[18:19]).strip('(),')
    Green6 = str(packet.dmxData[19:20]).strip('(),')
    Blue6 = str(packet.dmxData[20:21]).strip('(),')

    L6 = [int(Red6), int(Green6), int(Blue6)]

    # LED7
    Red7 = str(packet.dmxData[21:22]).strip('(),')
    Green7 = str(packet.dmxData[22:23]).strip('(),')
    Blue7 = str(packet.dmxData[23:24]).strip('(),')

    L7 = [int(Red7), int(Green7), int(Blue7)]

    # LED8
    Red8 = str(packet.dmxData[21:22]).strip('(),')
    Green8 = str(packet.dmxData[22:23]).strip('(),')
    Blue8 = str(packet.dmxData[23:24]).strip('(),')

    L8 = [int(Red8), int(Green8), int(Blue8)]


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
    #print('LED0: ' + 'R:' + Red0 + ' G:' + Green0 + ' B:' + Blue0 + '\n' + '-' * 100)
    #print('LED1: ' + 'R:' + Red1 + ' G:' + Green1 + ' B:' + Blue1 + '\n' + '-' * 100)
    #print('LED2: ' + 'R:' + Red2 + ' G:' + Green2 + ' B:' + Blue2 + '\n' + '-' * 100)
    #print('LED3: ' + 'R:' + Red3 + ' G:' + Green3 + ' B:' + Blue3 + '\n' + '-' * 100)
    #print('LED4: ' + 'R:' + Red4 + ' G:' + Green4 + ' B:' + Blue4 + '\n' + '-' * 100)
    #print('LED5: ' + 'R:' + Red5 + ' G:' + Green5 + ' B:' + Blue5 + '\n' + '-' * 100 + '\n' + '-' * 100)
    #print('RawData: ' + str(packet.dmxData) + '\n' + '-' * 100)

# optional: if multicast is desired, join with the universe number as parameter
receiver.join_multicast(1)

#time.sleep(100)  # receive for 10 seconds

