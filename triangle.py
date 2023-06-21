#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=150000)  
time.sleep(3)

print '0. taking off till 10m'
drone.take_off(10.0)

print ' move in a triangular trajectory of side length 10m at a height of 10m'

print ' 1. moving from Point A to B of triangle ABC'
# h^2=p^2+b^2, here square root of sum of square of p=8m and b=6m
# gives us the desired side length of 10m. 
drone.position_set(5, 8.6, 10, relative=True)
drone.position_set(5, -8.6, 10, relative=True)
drone.position_set(-10,0, 10, relative=True)

print ' 4. Landing'
drone.land(async=False)


drone.disconnect()
