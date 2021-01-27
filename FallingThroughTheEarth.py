from vpython import *
#GlowScript 2.9 VPython
# Falling Through The Earth Simulation - Reece Yang, 2019/11/20
# ------------------------------------------------------------------------------
# This program simulates a person (or any object, really) falling through a tunnel 
# going through the earth. The distance from the tunnel to the center of the earth
# can be modified by changing the constant h (more explanation is below). 
#
# We model the earth and the person with two different spheres, and we also plot
# the information about the motion of the person with three graphs. In addition,
# the program outputs the period of the oscillation after the loop finishes.
# 
# The earth should appear as a sphere with the earth texture; however, it appears 
# as though the textures do not load on certain computers, so if the earth is not
# displaying it may be because the earth texture is not working.

#constants
R_earth = 6.3781 * pow(10, 6) # m
G = 6.67259 * pow(10, -11) # N m^2 kg^-2
M_earth = 5.9722 * pow(10, 24) # kg
density_earth = M_earth / ((4.0 / 3.0) * pi * R_earth * R_earth * R_earth)
# change h to get a tunnel that is h meters away from the center of the earth
h = R_earth * 0.9 # m - height of the tunnel (for h = 0 the tunnel goes through the center of the earth)

#variables
x = sqrt(R_earth * R_earth - h * h) # m - distance from person to center of tunnel
v = 0 # m/s - velocity of the person
a # m/s^2 - acceleration of the person
r = R_earth # m - distance from person to center of the earth
M_enclosed #kg - enclosed mass of the earth
t = 0 # s
dt = 1 # s - change in time
period # s - period of the oscillation
found_period = False # used to find the period

earth = sphere(pos=vector(0,0,0), radius=R_earth, texture=textures.earth, opacity=0.40) # the earth object
person = sphere(pos=vector(h,x,0), radius=R_earth*0.1, color=color.orange) # the "person"

window1=graph(height=400, xtitle='Time (min)', ytitle = 'Distance from center of tunnel (m)')  #create the first plot window
pos_plot = gcurve(color=color.red) #specify plotting in the window above
window2 = graph(height=400, xtitle='Time (min)', ytitle= 'Velocity (m/s)')  #create second plot window
vel_plot = gcurve(color=color.blue)  #specify plotting in window above
window3 = graph(height=400, xtitle='Time (min)', ytitle= 'Acceleration (m/s)')  #create third plot window
acc_plot = gcurve(color=color.blue)  #specify plotting in window above

# run the loop for 3 * 84 minutes
while t < 3 * 84 * 60:
    rate(10000) # slow down the loop so the simulation is animated
    
    M_enclosed = density_earth * ((4.0 / 3.0) * pi * r * r * r) # calculate the enclosed mass of the earth
    a = (G * M_enclosed / (r * r)) * x / r # calculate the acceleration (note: we've divided out the mass of the person)
    v += a * dt # calculate velocity
    x -= v * dt # calculate the position of the person
    
    # let's try to find the period!
    # check if we have a period already, then check if the velocity has changed directions this past time interval
    if not found_period and v - a * dt > 0 and v < 0:
        # if it has, then the person has reached the other side of the tunnel
        period = 2 * t # the period is then twice the time it has taken to do so
        found_period = True # we've now found the period, so set found_period to True
        
    # let's find the velocity of the person in the middle
    # since its unlikely that position is ever exactly 0, we'll just check if it is close enough
    if abs(x) < 100: # we settled on 100 m through experimentation
        speed_center = v # set speed_center to v
    
    pos_plot.plot(t / 60, x) # plot the position
    vel_plot.plot(t / 60, v) # plot the velocity
    acc_plot.plot(t / 60, a) # plot the acceleration
    person.pos = vector(h, x, 0) # update the position of the person graphic
    
    t += dt # update time
    r = sqrt(h * h + x * x) # update distance from person to center of the earth
    
print("Period:",period/60, "minutes") # print the period of the oscillation, in minutes
print("Speed at center of earth:", speed_center, "m/s") # print the speed at the center, in m/s