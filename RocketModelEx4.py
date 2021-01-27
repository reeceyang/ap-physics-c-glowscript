from vpython import *
#GlowScript 2.9 VPython

# constants
G = 6.674 / (10**11) # Nm^2/kg^2
r = 6.3781 * (10**6) # m (radius of the earth)
m_earth = 5.9722 * (10**24) # kg

diameter = 1.65 #m - diameter of the rocket
A = pi * (diameter / 2) * (diameter / 2) #m^2 - cross-sectional area of the rocket
Cd = 0.125 # drag coefficient
rho = 1.22 #kg/m^3 - density of air

# variables
m0 = 4000 + 8800 #kg
m = m0 # kg
fuelrate = 129.4 # kg/s
thrust # N
v = 0 # m/s
a # m/s^2
Fnet # N
Fg # N
D # N - drag force
v_exhaust = 2050 # m/s
x = 0 # m
t = 0 # s
dt = 0.11 # s

window1=graph(height=200, xtitle='Time (s)', ytitle = 'Altitude (m)')  #create the first plot window
pos_plot = gcurve(color=color.red) #specify plotting in the window above
window2 = graph(height=200, xtitle='Time(s)', ytitle= 'Velocity (m/s)')  #create second plot window
vel_plot = gcurve(color=color.blue)  #specify plotting in window above
window3 = graph(height=200, xtitle='Time(s)', ytitle= 'Acceleration (m/s)')  #create third plot window
acc_plot = gcurve(color=color.blue)  #specify plotting in window above

max_height = 0 #m - maximum height of the rocket

while x >= 0:
    if m > 4000:
        thrust = v_exhaust * (fuelrate * dt) / dt
    else:
        thrust = 0
        
    Fg = G * m_earth * m / ((r + x) * (r + x))
    
    # calculate drag force: if velocity is positive, drag force is in the negative
    # direction; if velocity is negative, drag force is in the positive direction
    if v > 0:
        D = -0.5 * rho * v * v * Cd * A
    else:
        D = 0.5 * rho * v * v * Cd * A
    
    Fnet = thrust - Fg + D
    a = Fnet / m
    v += a * dt
    x += v * dt
    
    pos_plot.plot(t, x)
    vel_plot.plot(t, v)
    acc_plot.plot(t, a)
    
    # set the max_height of the rocket
    if x > max_height:
        max_height = x
    
    if m > 4000:
        m -= fuelrate * dt
    t += dt

print(max_height)