import math

# parameters

m = 0.25      # mass or the rubber duck in kg
v = 4.3       # velocity of the rubber duck when leaving the catapult
alpha = 45    # release angle of the duck from the catapult, against horizontal
h = 1.5       # release height of the rubber duck from the catapult
g = 9.81     # vertical acceleration due to gravity in m/s^2

# calculations

alpha_rad = alpha * math.pi / 180       # convert the angle to radiant for calculation
v_h = v * math.cos( alpha_rad )         # horizontal velocity
v_v = v * math.sin( alpha_rad )         # vertical velocity of rubber duck on release

t_up = v_v / g                          # time to reach the highest point (v_v = 0)
h_max = h + v_v * t_up - 0.5 * g * t_up**2    # maximal hight of projectile 

t_down = math.sqrt( 2 * h_max / g)      # time from highest point to touchdown

distance = v_h * ( t_up + t_down)

print(distance)
