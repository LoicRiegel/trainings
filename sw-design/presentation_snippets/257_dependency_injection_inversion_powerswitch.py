# BEFORE

class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class ElectricPowerSwitch:
    """Switch that can turn on or off connected devices."""
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True

def main():
    l = LightBulb()
    switch = ElectricPowerSwitch(l)
    switch.press()
    switch.press()
