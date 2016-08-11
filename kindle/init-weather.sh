#!/bin/sh

cd "$(dirname "$0")"

export PATH=/usr/local/bin:/bin:/usr/bin:/usr/sbin:/sbin:/usr/local/python/bin

stop framework
stop powerd

log () {
	#eips 5 5 "$1"
    logger "$1"
}

while true; do
    # enable wifi
    #lipc-set-prop com.lab126.cmd wirelessEnable 1

    log "Waiting for network..."

    ./wait-for-network.sh

    log "Got network."

    sleep 10

    log "Displaying image..."

    ./display-weather.sh

    # disable wifi
    #lipc-set-prop com.lab126.cmd wirelessEnable 0

    log "Waiting 20 seconds..."

    sleep 20

    log "Sleeping 20 seconds..."

    sleep 2

    # Sleep for 12 hours minus 30 seconds (we estimate image refresh takes 30 seconds)
    rtcwake -d /dev/rtc1 -s $((60*60*12-30))
done
