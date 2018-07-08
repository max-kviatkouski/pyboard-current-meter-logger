# PyBoard based Tilt Current Meter
Code to turn PyBoard with accelerometer into tilt current meter.

Assembly instructions and DIY project page: 

https://hackaday.io/project/158083-cheap-underwater-tilt-current-sensor

# Operational sequence
This guide assumes that
* You are running Linux with Python 3 installed
* When connected PyBoard is available as `/dev/ttyACM0`

1. Connect battery
2. Right after PyBoard launch sequence press and hold `USR` button until green 
led blinks - that means board switched into Storage/Serial device mode. If you missed
and orange LED started blinking (meaning that PyBoard started logging) press `RST` followed
by holding `USR` button until green LED blinks a few times
3. Connect PyBoard to computer
4. Execute `./setrtc.py` - this will set UTC time on the board based on computer time
5. Push RST button to recycle PyBoard. Press nothing else. If orange LED starts blinking
that means PyBoard entered logging mode
6. Assemble the meter
7. Calibrate still vertical position by attaching meter tether to a bottom of a 
bucket/pool/container filled with water. Leave it like this to 10-20 logging cycles
8. Deploy the meter underwater
9. After desired period of time has been logged, unmount the meter and bring back to the 
surface
10. Dry it out and open the housing
11. Push `RST` button followed by pushing `USR` button to switch the board into 
Storage/Serial device mode
12. Execute `./checkpointrtc.py` - this will measure and record difference between your 
computer clock and PyBoard clock. (PyBoard Lite has cheap oscillator as real-time clock 
and it is not precise. `setrtc.py` and `checkpoint.py` together establish cumulative error.
That information will be used to calculate correction of record timestamps during log 
processing)
13. Download log *.csv files into some folder
14. Proposed scripts to use for log processing
    * `average-sample-series.py` - take all records within logging frame and average them 
    to one record
    * `axes_to_angle.py` - convert axes values to angle between accelerometer (x,y,z) vector 
    and vertical direction
    * `pyboard-to-posix-timestampe.py` - convert PyBoard timestamps to POSIX timestamps.