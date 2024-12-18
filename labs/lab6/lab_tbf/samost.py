#!/usr/bin/env python

"""
Simple experiment.
Output: ping.dat
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import time

def emptyNet():

	"create an empty network and add nodes to it."

	net = Mininet( controller=Controller, waitConnected=True )

	info('*** adding controller\n' )
	net.addController( 'c0' )

	info('*** adding hosts\n' )
	h1 = net.addHost( 'h1', ip='10.0.0.1' )
	h2 = net.addHost( 'h2', ip='10.0.0.2' )
	info('*** adding switch\n' )
	s1 = net.addSwitch( 's1' )

	info('***creating links\n' )
	net.addLink( h1, s1)
	net.addLink( h2, s1)

	info('***starting network' )
	net.start()

	info('***set loss\n' )
	h1.cmdPrint( 'tc qdisc add dev h1-eth0 root tbf rate 10gbit burst 5000000 limit 15000000' )
	
	time.sleep(10)

	info('***proverka propysknoi sposobnosti')
	h2.cmdPrint('iperf3 -s &')
	time.sleep(10)
	h1.cmdPrint('iperf3 -c', h2.IP(), ' | grep "MBytes" | awk \'{print $7}\' > ping.dat')

	info('***stopping network' )
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	emptyNet()
