#!/usr/bin/python

import time
import json
import argparse
from DIndexService import DIndexService
import sys

def get_args():
    """
    Get command line args from the user.
    """
    parser = argparse.ArgumentParser(
        description='Standard Arguments for talking to Distributed Index Server')
    parser.add_argument('-c', '--config',
                        required=True,
                        action='store',
                        help='Config file of the network')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    """
    Main method starting deamon threads and peer operations.
    """
    try:
        args = get_args()
        with open(args.config) as f:
            config = json.loads(f.read())

        print "Starting Peer..."
        print "Initializing Index Service..."
        time.sleep(10)
        service = DIndexService(config)
        service.establish_connection()
        while True:
            print "*" * 20
            print "1. Put Key and Value"
            print "2. Get Key"
            print "3. Delete Key"
            print "4. Exit"
            print "*" * 20
            print "Enter choise : "
            ops = raw_input()

            if int(ops) == 1:
                print "Enter Key: "
                key = raw_input()
                print "Enter Value: "
                value = raw_input()
                rcv_data = service.put(key,value)
                if rcv_data:
                    print "Peer Put Key: \'%s\' on server successful." % (key)
                else:
                    print "Peer Put Key: \'%s\' on server unsuccessful." % (key)

            elif int(ops) == 2:
                print "Enter Key: "
                key = raw_input()
                rcv_data = service.get(key)
                if not rcv_data:
                    print "Peer Get value of Key: \'%s\' on server unsuccessful." % (key)
                else:
                    print "Peer Get value of Key: \'%s\' on server successful." % (key)
                    for value in rcv_data:
                        print "Value: %s" % (value)

            elif int(ops) == 3:
                print "Enter Key: "
                key = raw_input()
                rcv_data = service.delete(key)
                if rcv_data:
                    print "Peer Delete Key: \'%s\' on server successful." % (key)
                else:
                    print "Peer Delete Key: \'%s\' on server unsuccessful." % (key)

            elif int(ops) == 4:
                service.disable_connection()
                break

            else:
                print "Invaild choice...\n"
                continue

    except Exception as e:
        print "main function error: %s" % e
        sys.exit(1)
    except (KeyboardInterrupt, SystemExit):
        print "Peer Shutting down..."
        service.disable_connection()
        time.sleep(1)
        sys.exit(1)

__author__ = 'arihant'
