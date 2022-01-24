def ontimepercentage(airports,year):

    print('Percentage of ontime flights in ' + str(year))
    for i in airports:
        if( i['Time']['Year'] == year):
            ontime = i['Statistics']['Flights']['On Time']
            Total = i['Statistics']['Flights']['Total']
            per = '{:.2f}'.format((ontime/Total)*100)
            print(i['Airport']['Name'] + '     :' + str(per) +'%')