from numbers import Number
import math
def taylor_tool_life(**kwargs):
    if 'get' not in kwargs or kwargs['get'] not in ['time','speed']:
        raise Exception("You must specify get=\'time\' or get=\'speed\'")
    if 'n' not in kwargs or isinstance(kwargs['n'],Number) is not True:
        raise Exception("You must specify keyword n and it must be a Number")
    else:
        n = kwargs['n']
    if 'c' not in kwargs or isinstance(kwargs['c'],Number) is not True:
        raise Exception("You must specify keyword c and it must be a Number")
    else:
        c = kwargs['c']
    if kwargs['get'] == "time":
        if 'v_c' not in kwargs or isinstance(kwargs['v_c'],Number) is not True:
            raise Exception("You must specify keyword v_c and it must be a Number")
        else:
            v_c = kwargs['v_c']
        t = _nth_root(c/v_c,n)
        return t
    if kwargs['get'] == "speed":
        if 't' not in kwargs or isinstance(kwargs['t'],Number) is not True:
            raise Exception("You must specify keyword t and it must be a Number")
        else:
            t = kwargs['t']
        v_c = c/(t**n)
        return v_c

def spindle_speed(**kwargs):
    if 'get' not in kwargs or kwargs['get'] not in ['spindle_speed','cutting_speed']:
        raise Exception("You must specify get=\'spindle_speed\' or get=\'cutting_speed\'")
    if 'd' not in kwargs or isinstance(kwargs['d'],Number) is not True:
        raise Exception("You must specify keyword d and it must be a Number")
    else:
        d = kwargs['d']
    if 'metric' in kwargs and type(kwargs['metric']).__name__ != 'bool':
        print(type(kwargs['metric']).__name__)
        raise Exception("the metric keyword must be a boolean")
    elif 'metric' in kwargs:
        metric = kwargs['metric']
    else:
        metric = True
    if kwargs['get'] == "spindle_speed":
        if 'v_c' not in kwargs or isinstance(kwargs['v_c'],Number) is not True:
            raise Exception("You must specify keyword v_c and it must be a Number")
        else:
            v_c = kwargs['v_c']
        if metric:
            n = (v_c*1000)/(math.pi*d)
        else:
            n = (v_c*12)/(math.pi*d)
        return n
    if kwargs['get'] == "cutting_speed":
        if 'd' not in kwargs or isinstance(kwargs['d'],Number) is not True:
            raise Exception("You must specify keyword d and it must be a Number")
        else:
            d = kwargs['d']
        if 'n' not in kwargs or isinstance(kwargs['n'],Number) is not True:
            raise Exception("You must specify keyword n and it must be a Number")
        else:
            n = kwargs['n']
        if 'metric' in kwargs and type(kwargs['metric']).__name__ != 'bool':
            print(type(kwargs['metric']).__name__)
            raise Exception("the metric keyword must be a boolean")
        elif 'metric' in kwargs:
            metric = kwargs['metric']
        else:
            metric = True
        if metric:
            v_c = (n*(math.pi*d))/1000
        else:
            v_c = (n*(math.pi*d))/12
        return v_c

def table_feed(**kwargs):
    if 'f_z' not in kwargs or isinstance(kwargs['f_z'],Number) is not True:
        raise Exception("You must specify keyword f_z and it must be a Number")
    else:
        f_z = kwargs['f_z']
    if 'z' not in kwargs or isinstance(kwargs['z'],Number) is not True:
        raise Exception("You must specify keyword z and it must be a Number")
    else:
        z = kwargs['z']
    if 'n' not in kwargs or isinstance(kwargs['n'],Number) is not True:
        raise Exception("You must specify keyword n and it must be a Number")
    else:
        n = kwargs['n']

    table_feed = f_z * z * n
    return table_feed

def inches_to_mm(x):
    if isinstance(x,Number) is not True:
        raise Exception("Your input must be a number")
    return x * 25.4

def mm_to_inches(x):
    if isinstance(x,Number) is not True:
        raise Exception("Your input must be a number")
    return x / 25.4

def _nth_root(x,n):
# function to return the n-th root of x
    return x**(1.0/n)

# taylor_tool_life(get='time',n=0.0867550644,c=112.8632364851,v_c=81)
# spindle_speed(get='spindle_speed',v_c=81,d=0.125,metric=False)
# spindle_speed(get='cutting_speed',n=spindle_speed(get='spindle_speed',v_c=81,d=0.125,metric=False),d=0.125,metric=False)
# table_feed(f_z=0.001,z=4,n=spindle_speed(get='spindle_speed',v_c=81,d=0.125,metric=False))
# inches_to_mm(table_feed(f_z=0.001,z=4,n=spindle_speed(get='spindle_speed',v_c=81,d=0.125,metric=False)))

speed = inches_to_mm(table_feed(f_z=0.001,z=4,n=spindle_speed(get='spindle_speed',v_c=20,d=0.125,metric=False)))
print('speed:',speed)
life = taylor_tool_life(get='time',n=0.268907833513,c=226.026783561,v_c=20)
print('life:',life)
# speed = inches_to_mm(table_feed(f_z=0.001,z=4,n=spindle_speed(get='spindle_speed',v_c=70,d=0.125,metric=False)))
# print('speed:',speed)
# life = taylor_tool_life(get='time',n=0.0867550644,c=112.8632364851,v_c=70)
# print('life:',life)

# speed = inches_to_mm(table_feed(f_z=0.002,z=6,n=spindle_speed(get='spindle_speed',v_c=70,d=1.5,metric=False)))
# print('speed:',speed)
# life = taylor_tool_life(get='time',n=0.0867550644,c=144.6964570322,v_c=70)
# print('life:',life)

# # life = taylor_tool_life(get='time',n=0.5,c=1264,v_c=50,metric=True)
# # print('life:',life)
# vs = []
# for v in range(30,130):
#     vs.append(taylor_tool_life(get='time',n=0.4460643949,c=568.1625169728,v_c=v))
# for v in vs:
#     print(str(v)+',')