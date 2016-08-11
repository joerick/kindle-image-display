#!/bin/sh

TIMER=60     # number of seconds to attempt a connection
CONNECTED=0                  # whether we are currently connected
while [ 0 -eq $CONNECTED ]; do
    # test whether we can ping outside
    /bin/ping -c 1 -w 2 8.8.8.8 > /dev/null && CONNECTED=1

    # if we can't, checkout timeout or sleep for 1s
    if [ 0 -eq $CONNECTED ]; then
        TIMER=$(($TIMER-1))
        if [ 0 -eq $TIMER ]; then
            logger "No internet connection after ${NETWORK_TIMEOUT} seconds, aborting."
            break
        else
            sleep 1
        fi
    fi
done
