from vpython import *
#GlowScript 2.9 VPython

# constants
G = 6.674 / (10**11) # Nm^2/kg^2
r = 6.3781 * (10**6) # m (radius of the earth)
m_earth = 5.9722 * (10**24) # kg

diameter = 1.65 #m
A = pi * (diameter / 2) * (diameter / 2)
Cd = 0.125

# variables
m0 = 4000 + 8800 #kg
m = m0 # kg
fuelrate = 129.4 # kg/s
thrust # N
v = 0 # m/s
a # m/s^2
Fnet # N
Fg
v_exhaust = 2050 # m/s
rho #kg/m^3 - air density is a variable now
x = 0
t = 0 # s
dt = 0.11 # s

window1=graph(height=200, xtitle='Time (s)', ytitle = 'Altitude (m)')  #create the first plot window
pos_plot = gcurve(color=color.red) #specify plotting in the window above
window2 = graph(height=200, xtitle='Time(s)', ytitle= 'Velocity (m/s)')  #create second plot window
vel_plot = gcurve(color=color.blue)  #specify plotting in window above
window3 = graph(height=200, xtitle='Time(s)', ytitle= 'Acceleration (m/s)')  #create third plot window
acc_plot = gcurve(color=color.blue)  #specify plotting in window above
window4 = graph(height=200, xtitle='Time(s)', ytitle= 'Drag (N)')  #create fourth plot window
dra_plot = gcurve(color=color.blue)  #specify plotting in window above

max_height = 0

while x >= 0:
    
    if m > 4000:
        thrust = v_exhaust * (fuelrate * dt) / dt
    else:
        thrust = 0
    
    Fg = G * m_earth * m / ((r + x) * (r + x))
    
    #calculate air density (rho) using a piecewise exponential function 
    if x < 10000:
        rho = 1.2443 * exp(-0.0001 * x)
    else:
        rho = 1.4596 * exp(-0.0001 * x)
    
    if v > 0:
        D = -0.5 * rho * v * v * Cd * A
    else:
        D = 0.5 * rho * v * v * Cd * A
    
    Fnet = thrust - Fg + D
    a = Fnet / m
    v += a * dt
    x += v * dt
    
    if x > max_height:
        max_height = x
    
    pos_plot.plot(t, x)
    vel_plot.plot(t, v)
    acc_plot.plot(t, a)
    dra_plot.plot(t, D)
    
    if m > 4000:
        m -= fuelrate * dt
    t += dt

print (max_height)