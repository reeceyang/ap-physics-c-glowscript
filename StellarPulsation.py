from vpython import *
#GlowScript 2.9 VPython
# Stellar Pulsation Simulation - Reece Yang, 2019/11/20
# ------------------------------------------------------------------------------
# This program simulates a very simple model of a Cepheid variable star.

#constants
G = 6.67259 * pow(10, -11) # N m^2 kg^-2 - gravitational constant
M = 1.00 * pow(10, 31) #kg - mass at center point of the star
m = 1.00 * pow(10, 26) #kg - mass of the outer shell

#variables
r = 1.70 * pow(10, 10) # m - radius of the outer shell
v = 0 # m/s - radial velocity
P = 5.60 * pow(10, 4) # N m^-2 - pressure of the gas inside
t = 0 # s
dt = 10000 # s - change in time

star = sphere(pos=vector(0,0,0), radius=r, color=color.red, opacity=0.50) # the star object

window1=graph(height=400, xtitle='Time (s)', ytitle = 'Radius (m)')  #create the first plot window
pos_plot = gcurve(color=color.red) #specify plotting in the window above
window2 = graph(height=400, xtitle='Time (s)', ytitle= 'Velocity (m/s)')  #create second plot window
vel_plot = gcurve(color=color.blue)  #specify plotting in window above
window3 = graph(height=400, xtitle='Time (s)', ytitle= 'Pressure (N m^-2)')  #create third plot window
acc_plot = gcurve(color=color.blue)  #specify plotting in window above

# run the loop for 1500000 seconds
while t <= 1500000:
    rate(10) # slow down the loop so the simulation is animated
    
    # calculate values using given equations
    vf = v + dt * ((4 * pi * r * r * P / m) - (G * M / (r * r)))
    rf = r + vf * dt
    Pf = P * (r / rf) * (r / rf) * (r / rf) * (r / rf) * (r / rf)
    
    pos_plot.plot(t, rf) # plot the radius
    vel_plot.plot(t, vf) # plot the velocity
    acc_plot.plot(t, Pf) # plot the pressure
    
    star.radius = rf # update radius of the star
    # update the opacity of the star to make it seem to get brighter
    # note: I'm not sure if the brightness of the star actually works like this,
    # this effect just makes it look cool
    star.opacity = 0.50 - (((1.54 * pow(10, 10)) - rf) / (0.32 * pow(10, 10))) 
    
    # update variables
    t += dt
    v = vf
    r = rf
    P = Pf