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

def core(API_KEY):
    print('ops')



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
    print("Using config file : " + configfile)
    config = configparser.ConfigParser()
    config.read(configfile)

    API_KEY = config.get("Weather", "API_KEY")

    core(API_KEY)



if __name__ == "__main__":
    main();