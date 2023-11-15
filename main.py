import launchpad_py as launchpad
import keyboard
import time
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType
from openrgb.utils import RGBColor

# set launchpad_py
lp = launchpad.Launchpad()

# set openRGB client
cli = OpenRGBClient()

# define devices connected
Key = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
Pad = cli.get_devices_by_type(DeviceType.MOUSEMAT)[0]
Mobo = cli.get_devices_by_type(DeviceType.MOTHERBOARD)[0]
Mouse = cli.get_devices_by_type(DeviceType.MOUSE)[0]

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

# resize device zones if needed
# Key.zones[0].resize(0)
# Pad.zones[0].resize(0)
# Mobo.zones[0].resize(0)
# Mouse.zones[0].resize(0)

# define colors used
red = RGBColor(255, 0, 0)
green = RGBColor(0, 255, 0)
blue = RGBColor(0, 0, 255)
black = RGBColor(0, 0, 0)

# variable for later iteration through launchpad rows
r = range(9)

#  specify log file path
filepath = r'F:\BSGO\client\live\bsgo_Data\Vitalpoints.txt'

# set up loop
while True:
    try:
        # open log file and read lines
        with open(filepath) as f:
            lines = f.read().splitlines()
            line1 = lines[0]
            line2 = lines[1]

            # sort lines into current and max health
            MaxHealth = int(line1)
            CurrentHealth = int(line2)

            # calculate health percentage and translate to red & green values
            HealthDifference = MaxHealth - CurrentHealth
            PercentageMax = HealthDifference / MaxHealth
            PercentageCurrent = CurrentHealth / MaxHealth

            RChannel = PercentageMax * 255
            GChannel = PercentageCurrent * 255

            # make variable for color
            Color = RGBColor(int(RChannel), int(GChannel), 0)
            RGSwap = RGBColor(int(GChannel), int(RChannel), 0)  # use if devices uses different pin layout
            clist = [int(RChannel), int(GChannel), 0]
            lis = [Color] * 18 + [black] * 114

            # set delay for each update cycle
            time.sleep(0.001)

            # set color according to health
            Key.set_colors(lis)
            Pad.set_color(Color)
            Mobo.set_color(Color)
            Mouse.set_color(Color)

            # set up loop to iterate through launchpad rows and set colors
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

            #  print values to console
            a = 'Percentage: ' + str(PercentageMax)
            b = 'Green Channel: ' + str(GChannel)
            c = 'Red Channel: ' + str(RChannel)
            print(a + '\n' + b + '\n' + c + '\n' + '-'*100)

    finally:
        # pause program on keypress
        if keyboard.is_pressed('pageup'):
            lp.Reset()
            time.sleep(5)
        # end program on keypress
        if keyboard.is_pressed('pagedown'):
            lp.Reset()
            break
