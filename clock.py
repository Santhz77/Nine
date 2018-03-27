'''
Author : Santhosh Nayak

License : BSD License
'''

# imports
# import os
# os.system("espeak -v en-wi+f1  -s150  'Good Morning Kim'")


from util import getweather_info
import configparser
import getopt
import sys,os
import logging
import json
import pyttsx3

#FIXME : Make a logger config to include  a configuration and log file set up
log= logging.getLogger( __name__ )


def speak(msg):
    # os.system("espeak -v en-wi+f1  -s150 '" + msg +"'")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for dat in voices:
        print(dat)
    engine.setProperty('voice', 'english+f1')

    engine.say(msg)
    engine.runAndWait()



def core(API_KEY):
    #weather_json = getweather_info(API_KEY)
    # FixME : when using the API load to json!

    weather_json = {"coord":{"lon":7,"lat":49.23},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"base":"stations","main":{"temp":8.03,"pressure":1011,"humidity":61,"temp_min":7,"temp_max":9},"visibility":10000,"wind":{"speed":6.2,"deg":220},"clouds":{"all":75},"dt":1522161000,"sys":{"type":1,"id":4890,"message":0.0025,"country":"DE","sunrise":1522127942,"sunset":1522173375},"id":2842647,"name":"Saarbrucken","cod":200}
    print(weather_json)

    speak('Now the temparature is ' + str(weather_json['main']['temp']) + ' degree celcius.')



def usage(message):
    print("""
    Usage: pyhton3 clocl.py [OPTIONS] -c CONFIGFILE

    -c FILENAME, --configfile FILENAME    Use FILENAME for configuration
    -h, --help                            Show help
    """)

    if(message):
        print("\nERROR: " + message + "\n\n")
    sys.exit(2)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:d", ["help", "configfile="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -c not recognized"
        usage()

    configfile = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-c", "--configfile"):
            configfile = a
        else:
            assert False, "unhandled option"

    if(configfile is None):
        usage("Missing configfile")
    if(not os.path.exists(configfile)):
        usage("Cannot open file " + configfile)

    # read the config file.
    log.info("Using config file : " + configfile)
    config = configparser.ConfigParser()
    config.read(configfile)
    API_KEY = config.get("Weather", "API_KEY")
    log.debug('APIKEY IS ' + API_KEY)

    core(API_KEY)



if __name__ == "__main__":
    main();