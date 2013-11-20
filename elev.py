import simplejson
import urllib

ELEVATION_BASE_URL = 'http://maps.googleapis.com/maps/api/elevation/json'
    
def getElevation( path, samples, sensor="false", **elvtn_args ):
    elvtn_args.update({
            'path': path,
            'samples': samples,
            'sensor': sensor
            })

    url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
    response = simplejson.load(urllib.urlopen(url))

    # Create a dictionary for each results[] object
    elevationArray = []

    for resultset in response['results']:
        elevationArray.append(resultset['elevation'])

    print elevationArray

    # Create the chart passing the array of elevation data
    #getChart(chartData=elevationArray)

if __name__ == '__main__':
    '''
    starye koordinaty

    p11 = "51.732131639851644,94.39041137695312"
    p12 = "51.73617148842998,94.50679779052734"
    p21 = "51.67936786087718,94.39247131347656"
    p22 = "51.690649161687986,94.51057434082031"

    x11 = 51.732131639851644
    y11 = 94.39041137695312
    x21 = 51.67936786087718
    y21 = 94.39247131347656

    x12 = 51.73617148842998
    y12 = 94.50679779052734
    x22 = 51.690649161687986
    y22 = 94.51057434082031
    '''
    
    '''
    novye koordinaty
    sbor karty po dnyam:
    + 0: 1 - 50
    + 1: 50 - 100
    + 2: 100 - 150
    + 3: 150 - 200
    ''' 

    x11 = 51.71894646414401 
    y11 = 94.36105728149414 

    x12 = 51.74648209613251 
    y12 = 94.47795867919922

    x21 = 51.68915933967863
    y21 = 94.36655044555664

    x22 = 51.7107569598828 
    y22 = 94.49169158935547

    NumDay = 3

    samplesX = 200
    samplesY = 400
    
    delta1x = ( x11 - x21 ) / samplesX
    delta2x = ( x12 - x22 ) / samplesX
    x11t = x11 - delta1x * 50 * NumDay
    x12t = x12 - delta2x * 50 * NumDay

    delta1y = ( y21 - y11 ) / samplesX
    delta2y = ( y22 - y12 ) / samplesX
    y11t = y11 + delta1y * 50 * NumDay
    y12t = y12 + delta2y * 50 * NumDay

    for i in range( 50 ) : 
        pathStr = str( x11t ) + "," + str( y11t ) + "|" + str( x12t ) + "," + str( y12t )
        getElevation( pathStr, samplesY )
        
        x11t -= delta1x
        x12t -= delta2x

        y11t += delta1y
        y12t += delta2y
