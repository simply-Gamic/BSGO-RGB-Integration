import sacn
import time

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

    # LED1
    Red1 = str(packet.dmxData[3:4]).strip('(),')
    Green1 = str(packet.dmxData[4:5]).strip('(),')
    Blue1 = str(packet.dmxData[5:6]).strip('(),')

    # LED2
    Red2 = str(packet.dmxData[6:7]).strip('(),')
    Green2 = str(packet.dmxData[7:8]).strip('(),')
    Blue2 = str(packet.dmxData[8:9]).strip('(),')

    # LED3
    Red3 = str(packet.dmxData[9:10]).strip('(),')
    Green3 = str(packet.dmxData[10:11]).strip('(),')
    Blue3 = str(packet.dmxData[11:12]).strip('(),')

    # LED4
    Red4 = str(packet.dmxData[12:13]).strip('(),')
    Green4 = str(packet.dmxData[13:14]).strip('(),')
    Blue4 = str(packet.dmxData[14:15]).strip('(),')

    # LED5
    Red5 = str(packet.dmxData[15:16]).strip('(),')
    Green5 = str(packet.dmxData[16:17]).strip('(),')
    Blue5 = str(packet.dmxData[17:18]).strip('(),')


    # print out values for each LED
    print('LED0: ' + 'R:' + Red0 + ' G:' + Green0 + ' B:' + Blue0 + '\n' + '-' * 100)
    print('LED1: ' + 'R:' + Red1 + ' G:' + Green1 + ' B:' + Blue1 + '\n' + '-' * 100)
    print('LED2: ' + 'R:' + Red2 + ' G:' + Green2 + ' B:' + Blue2 + '\n' + '-' * 100)
    print('LED3: ' + 'R:' + Red3 + ' G:' + Green3 + ' B:' + Blue3 + '\n' + '-' * 100)
    print('LED4: ' + 'R:' + Red4 + ' G:' + Green4 + ' B:' + Blue4 + '\n' + '-' * 100)
    print('LED5: ' + 'R:' + Red5 + ' G:' + Green5 + ' B:' + Blue5 + '\n' + '-' * 100 + '\n' + '-' * 100)
    print('RawData: ' + str(packet.dmxData) + '\n' + '-' * 100)

# optional: if multicast is desired, join with the universe number as parameter
receiver.join_multicast(1)

time.sleep(100)  # receive for 10 seconds

# optional: if multicast was previously joined
receiver.leave_multicast(1)

receiver.stop()