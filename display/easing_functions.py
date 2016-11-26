# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# taken from http://www.grasshopper3d.com/profiles/blogs/easing-functions-in-python
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import math
 
 
def linear(t):
    return t
 
 
def easeInQuad(t):
    return t**2.0
 
 
def easeOutQuad(t):
    return -t * (t-2.0)
 
 
def easeInOutQuad(t):
    if t < 0.5:
        return 2.0 * t**2.0
    else:
        t = 2.0*t - 1.0
        return -0.5 * (t*(t-2.0) - 1.0)
 
 
def easeInCubic(t):
    return t**3
 
 
def easeOutCubic(t):
    t -= 1.0
    return t**3 + 1.0
 
 
def easeInOutCubic(t):
    t *= 2.0
    if t < 1.0:
        return 0.5 * t**3
    else:
        t -= 2.0
        return 0.5 * (t**3 + 2.0)
 
 
def easeInQuart(t):
    return t**4
 
 
def easeOutQuart(t):
    t -= 1.0
    return -(t**4 - 1.0)
 
 
def easeInOutQuart(t):
    t *= 2.0
    if t < 1.0:
        return 0.5 * t**4
    else:
        t -= 2.0
        return -0.5 * (t**4 - 2.0)
 
 
def easeInQuint(t):
    return t**5
 
 
def easeOutQuint(t):
    t -= 1.0
    return t**5 + 1.0
 
 
def easeInOutQuint(t):
    t *= 2.0
    if t < 1.0:
        return 0.5 * t**5
    else:
        t -= 2.0
        return 0.5 * (t**5 + 2.0)
 
 
def easeInSine(t):
    return -1.0 * math.cos(t * math.pi / 2.0) + 1.0
 
 
def easeOutSine(t):
    return math.sin(t * math.pi / 2.0)
 
 
def easeInOutSine(t):
    return -0.5 * (math.cos(math.pi * t) - 1.0)
 
 
def easeInExpo(t):
    if t == 0:
        return 0
    else:
        return 2.0**(10 * (t - 1.0))
 
 
def easeOutExpo(t):
    if t == 1.0:
        return 1.0
    else:
        return -(2.0 ** (-10 * t)) + 1.0
 
 
def easeInOutExpo(t):
    if t == 0:
        return 0
    elif t == 1.0:
        return 1.0
    else:
        t = t * 2.0
        if t < 1.0:
            return 0.5 * 2.0**(10 * (t - 1.0))
        else:
            t -= 1.0
            return 0.5 * (-1.0 * (2.0 ** (-10 * t)) + 2.0)
 
 
def easeInCirc(t):
    return -1.0 * (math.sqrt(1.0 - t * t) - 1.0)
 
 
def easeOutCirc(t):
    t -= 1.0
    return math.sqrt(1.0 - (t * t))
 
 
def easeInOutCirc(t):
    t *= 2.0
    if t < 1.0:
        return -0.5 * (math.sqrt(1.0 - t**2.0) - 1.0)
    else:
        t = t - 2.0
        return 0.5 * (math.sqrt(1.0 - t**2.0) + 1.0)
 
 
def easeInElastic(t, amplitude=None, period=None):
    if period is None:
        period = 0.3
 
    if amplitude is None:
        amplitude = 1.0
 
    if amplitude < 1.0:
        amplitude = 1.0
        s = period / 4
    else:
        s = period / (2.0 * math.pi) * math.asin(1.0 / amplitude)
 
    t -= 1.0
    return -1.0 * (amplitude * 2.0**(10*t) * math.sin( (t-s)*(2.0*math.pi) / period))
 
 
def easeOutElastic(t, amplitude=None, period=None):
    if period is None:
        period = 0.3
 
    if amplitude is None:
        amplitude = 1.0
 
    if amplitude < 1.0:
        amplitude = 1.0
        s = period / 4
    else:
        s = period / (2.0 * math.pi) * math.asin(1.0 / amplitude)
 
    return amplitude * 2.0**(-10*t) * math.sin((t-s)*(2.0*math.pi / period)) + 1.0
 
 
def easeInOutElastic(t, amplitude=None, period=None):
    if period is None:
        period = 0.5
 
    if amplitude is None:
        amplitude = 1.0
 
    if amplitude < 1.0:
        amplitude = 1.0
        s = period / 4
    else:
        s = period / (2.0 * math.pi) * math.asin(1.0 / amplitude)
 
    t *= 2.0
    if t < 1.0:
        t -= 1.0
        return -0.5 * (amplitude * 2.0**(10*t) * math.sin((t - s) * 2.0 * math.pi / period))
    else:
        t -= 1.0
        return amplitude * 2.0**(-10*t) * math.sin((t - s) * 2.0 * math.pi / period) * 0.5 + 1.0
 
 
def easeInBack(t, s=1.70158):
    return t**2.0 * ((s + 1.0) * t - s)
 
 
def easeOutBack(t, s=1.70158):
    t -= 1.0
    return t**2.0 * ((s + 1.0) * t + s) + 1.0
 
 
def easeInOutBack(t, s=1.70158):
    t *= 2.0
    if t < 1.0:
        s *= 1.525
        return 0.5 * (t * t * ((s + 1.0) * t - s))
    else:
        t -= 2.0
        s *= 1.525
        return 0.5 * (t * t * ((s + 1.0) * t + s) + 2.0)
 
 
def easeInBounce(t):
    return 1.0 - easeOutBounce(1.0 - t)
 
 
def easeOutBounce(t):
    if t < (1.0/2.75):
        return 7.5625 * t * t
    elif t < (2.0/2.75):
        t -= (1.5/2.75)
        return 7.5625 * t * t + 0.75
    elif t < (2.5/2.75):
        t -= (2.25/2.75)
        return 7.5625 * t * t + 0.9375
    else:
        t -= (2.65/2.75)
        return 7.5625 * t * t + 0.984375
 
 
def easeInOutBounce(t):
    if t < 0.5:
        return easeInBounce(2.0*t) * 0.5
    else:
        return easeOutBounce(2.0*t - 1.0) * 0.5 + 0.5