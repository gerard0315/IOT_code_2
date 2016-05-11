lines = set()
with open('datapush.csv','r') as infile, open('waka.csv','w') as outfile:
    outfile.write('updatetime, vehiclecount, totalspaces, garagecode, streamtime, switch \n')
    next(infile)
    for line in infile:
        if line not in lines:
            # Remove whitespace
            DATA = line.strip().split(',')
            
            DATA = [d.strip() for d in DATA]
            
            # Get time to compare against
            TIME = (DATA[0])
            
            # Other data
            VEHICLECOUNT = float(DATA[1])
            TOTALSPACES = float(DATA[2])
            GARAGECODE = DATA[3]
            STREAMTIME = (DATA[4])
            
            spacesopen = TOTALSPACES- (VEHICLECOUNT)
            if spacesopen > 0:
                ratio = TOTALSPACES / spacesopen
            else:
                ratio = 1
                
            if ratio > 1.25:
                threshold = 1
            else:
                threshold = 0
            
            
            outfile.write('{}, {}, {}, {}, {},{}\n'.format(TIME,VEHICLECOUNT,TOTALSPACES,GARAGECODE,STREAMTIME,threshold))
            
            
            