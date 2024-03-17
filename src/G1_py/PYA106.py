mins=float(input())
secs=float(input())
km=float(input())

mile=km/1.6
hour_avg=(secs/60+mins)/60
speed=mile/hour_avg

print("Speed = {:.1f}".format(speed))