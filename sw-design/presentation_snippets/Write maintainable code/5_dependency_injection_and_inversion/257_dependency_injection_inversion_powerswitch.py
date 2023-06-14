# FRANCOIS: to use in code quizz


# BEFORE


class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class ElectricPowerSwitch:
    """Switch that can turn on or off connected devices."""
    def __init__(self):
        self.light_bulb = LightBulb()
        self.on = False

    def press(self):
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True

def main():
    electrical_power_switch = ElectricPowerSwitch()
    electrical_power_switch.press()
    electrical_power_switch.press()


# AFTER DEPENDENCY INJECTION


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
    light_bulb = LightBulb()
    electrical_power_switch = ElectricPowerSwitch(light_bulb)
    electrical_power_switch.press()
    electrical_power_switch.press()


# AFTER DEP INJECTION

from abc import ABC, abstractmethod

class ConnectedDevice(ABC):
    @abstractmethod
    def turn_on(self):
        """Turn on the connected device."""

    @abstractmethod
    def turn_off(self):
        """Turn off the connected device."""

class LightBulb(ConnectedDevice):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class SmartPlug(ConnectedDevice):
    def turn_on(self):
        print("SmartPlug: turned on...")

    def turn_off(self):
        print("SmartPlug: turned off...")


class ElectricPowerSwitch:
    """Switch that can turn on or off connected devices."""

    def __init__(self, connected_device: ConnectedDevice):
        self.connected_device = connected_device
        self.on = False

    def press(self):
        if self.on:
            self.connected_device.turn_off()
            self.on = False
        else:
            self.connected_device.turn_on()
            self.on = True

def main():
    light_bulb = LightBulb()
    electrical_power_switch = ElectricPowerSwitch(light_bulb)
    electrical_power_switch.press()
    electrical_power_switch.press()
