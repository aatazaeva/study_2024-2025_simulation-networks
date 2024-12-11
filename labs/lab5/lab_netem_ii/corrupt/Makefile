all: ping.dat plot

ping.dat:
	sudo python lab_netem_ii.py

plot: ping.dat
	plot_iperf.sh res.json
clean:
	-rm -f *.json *.csv
	-rm -rf results
