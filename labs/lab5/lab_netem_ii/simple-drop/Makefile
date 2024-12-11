all: ping.dat

ping.dat:
	sudo python lab_netem_ii.py
	sudo chown mininet:mininet ping.dat

clean:
	-rm -f *.dat
