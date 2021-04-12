def fly_by(lamps, drone):
    print(lamps[len(drone)::])
    return (lamps[0:len(drone)]).replace('x', 'o') + lamps[len(drone)::]