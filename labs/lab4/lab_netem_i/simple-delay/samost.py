with open('ping.dat', 'r') as file:
	s = []
	for line in file.readlines():
		if '\n' in line:
			line.replace('\n', "")
		s.append([int(j) for j in (line.split(" "))])
	s = [j[1] for j in s]

	std = (sum([(i-(sum(s)/len(s)))**2 for i in s])/(len(s)-1))**0.5
	print(f"min: {min(s)} \nmax: {max(s)} \navg: {sum(s)/len(s)} \nstd: {std}")
