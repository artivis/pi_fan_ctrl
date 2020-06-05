# pi_fan_ctrl

Yet another variable fan controller for the RaspberryPi.

This script is based on the [instructable][instructable] tutorial of
[Aerandir14][Aerandir14] available [at this link][tutorial].

The main differences are:
-  set/get-able parameters
-  the fan speed value ([0-100] %) is written to a file (optional)
-  packaged as a snap for easier distribution

## Installation

```bash
$ sudo snap install pi-fan-ctrl
```
You should then connect the snap interface,
```bash
$ snap connect pi-fan-ctrl:hardware-observe
$ snap connect pi-fan-ctrl:gpio pi4-devel:bcm-gpio-21
```

# Parameters

The parameters are all set/get-able through the commands:
```bash
snap get/set pi-fan-ctrl <parameters>
```
The available parameters and their default values are as follows,
```yaml
# Fan control configuration

gpio:     21  # BCM used to drive transistor's base
fan_min:  20  # [%] Fan minimum speed.
sleep:     1  # [s] Time to wait between each refresh
pwm_freq: 25  # [Hz] Change this value if fan has strange behavior

hyst: 1 # Fan speed will change only of the difference of temperature is higher than hysteresis

fan_speed_out: True # Whether to write the fan speed to a file or not

# !!! Not yet configurable !!!
#
# Configurable temperature and fan speed steps
# temp_steps:  [50, 55,   60, 65,   70]   # [C]
# speed_steps: [30, 47.5, 65, 82.5, 100]  # [%]
```

Finally, if `fan_speed_out: True` the fan speed will be written to a file
in the snap. To retrieve the current fan speed simply issue,
```bash
$ cat /var/snap/pi-fan-ctrl/common/fan_speed
45
```

[//]: # (URLs)

[instructable]: https://www.instructables.com/
[Aerandir14]: https://www.instructables.com/member/Aerandir14/
[tutorial]: https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/
