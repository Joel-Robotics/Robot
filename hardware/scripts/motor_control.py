#!/usr/bin/env python
import serial
import rospy
import time
import numpy as np

def wheelspeeds(rspeed,rangle,rangular):
    wheels_dist = np.array([0.110, 0.110,0.110])
    wheels_angle = np.radians(np.array([0, 120, 240]))
    rangle = np.radians(np.array([rangle, rangle, rangle]))
    rspeed = np.array([rspeed, rspeed, rspeed])
    rangular = np.array([rangular, rangular, rangular])
    vel = rspeed*np.cos(rangle - wheels_angle) + wheels_dist*rangular
    return vel

def right(power):
    vel = [power,power,power]
    return vel

def stop():
    vel = [0,0,0]
    return vel