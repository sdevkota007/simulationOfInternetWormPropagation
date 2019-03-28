# simulationOfInternetWormPropagation
Internet Worm Propagation Simulation

## Design and Implementation:
For the purpose of simulation of internet worm propagation in a medium scale network, discrete time simulation technique is used in this program. It is assumed that we have an isolated network with omega(Ω) = 100,000 IP address space. For the sake of simplicity, the IP addresses is treated as having values from 1 to 100,000. There are N=1000 computers vulnerable to worm under consideration in this network and these vulnerable computers have the following specific IP addresses:

1, 2, 3,…, 10,

1001, 1002, …., 1010,  

2001, 2002, …, 2010,
…..

In other words, each cluster of 10 computers with the consecutive IPs are vulnerable to the worm, and in every 1000 consecutive IP addresses there will be one cluster of 10 vulnerable computers (so there are 100 clusters of vulnerable computers overall). 
It is also assumed that the worm starts its infection within this network from 1 initially infected machine that has the IP address of 1001. Every infected machine has a scan rate(η) of 3. That is, at each discrete time tick, a worm-infected computer can send out scans to 3 IP addresses within this network. If a scan finds a vulnerable computer, it infects the vulnerable computer immediately and this newly infected computer can start infecting others from the next discrete time tick. 

In this program, two kinds of scanning is simulated
 - Random Scanning: In this scanning technique, an infected computer x randomly picks another machine that is within the ip address space. 
 - Local preference Scanning: In this scanning strategy, an infected computer with IP value x, picks another machine with IP address y, where the value y is computed as follows: 
i) With probability p = 0.8, it picks a random value y such that  y ∈ [x-10, x+10]
ii). With the remaining probability 0.2, it picks a random IP value y between 1 to 100,000.

## Results and Discussion:
A total of 6 simulations is performed: three for random scanning technique and another three for local preference scanning technique. When we plot the number of infected computers at each time tick (Fig 1, Fig 2), it can be seen that for both of the scanning techniques, the spreading of the worm across the network follows a sigmoid curve (S-curve), which exhibits a progression from small beginnings that accelerates and approaches a climax over time.

Table 1 shows the time ticks taken by each simulation technique to infect all of the 1000 vulnerable computer in the network. For each of the three simulations, all of the vulnerable IPs in the network were infected by time ticks 464, 472 and 446 for random scanning, and time ticks 175, 199 and 189 for local preference scanning. Therefore, worm propagation through local preference scanning is seen to spread more quickly in the network than through random scanning technique. 

![html dark](https://github.com/sdevkota007/simulationOfInternetWormPropagation/blob/master/screenshots/random_scanning.png)
*Figure 1: Three simulation run on worm propagation by random scanning*

![html dark](https://github.com/sdevkota007/simulationOfInternetWormPropagation/blob/master/screenshots/local_preference_scanning.png)
*Figure 2: Three simulation run on worm propagation by local preference scanning*

![html dark](https://github.com/sdevkota007/simulationOfInternetWormPropagation/blob/master/screenshots/table.png)
*Table 1: Time ticks required to infect all vulnerable machines for Random scanning and Local preference scanning*

## Instruction on how to run the Program:
First, the following dependencies need to be installed to be able to run the program:
```
$ sudo apt-get install python-pip
$ pip2 install matplotlib
$ pip2 install numpy
```

To begin random scanning simulation
```
$ python2 random_scanning.py
```
To begin local preference scanning simulation
```
$ python2 local_preference_scanning.py
```
## Output:
A sample output of the program is shown below. Each simulation script takes around 3-5 minutes to complete. 

For random_scanning.py
```
*********Beginning Random Scanning Worm Propagation: Simulation 1***********
Simulation tick: 100 || IPs_infected: 7
Simulation tick: 200 || IPs_infected: 148
Simulation tick: 300 || IPs_infected: 791
Simulation tick: 400 || IPs_infected: 990
Simulation tick: 464 || IPs_infected: 1000. 
All IPs infected!!!

*********Beginning Random Scanning Worm Propagation: Simulation 2***********
Simulation tick: 100 || IPs_infected: 56
Simulation tick: 200 || IPs_infected: 570
Simulation tick: 300 || IPs_infected: 961
Simulation tick: 400 || IPs_infected: 996
Simulation tick: 472 || IPs_infected: 1000. 
All IPs infected!!!

*********Beginning Random Scanning Worm Propagation: Simulation 3***********
Simulation tick: 100 || IPs_infected: 21
Simulation tick: 200 || IPs_infected: 306
Simulation tick: 300 || IPs_infected: 900
Simulation tick: 400 || IPs_infected: 994
Simulation tick: 446 || IPs_infected: 1000. 
All IPs infected!!!
```

For local_preference_scanning.py
```
*********Beginning Local Preference Scanning Worm Propagation: Simulation 1***********
Simulation tick: 100 || IPs_infected: 479
Simulation tick: 175 || IPs_infected: 1000. 
All IPs infected!!!

*********Beginning Local Preference Scanning Worm Propagation: Simulation 2***********
Simulation tick: 100 || IPs_infected: 342
Simulation tick: 199 || IPs_infected: 1000. 
All IPs infected!!!

*********Beginning Local Preference Scanning Worm Propagation: Simulation 3***********
Simulation tick: 100 || IPs_infected: 712
Simulation tick: 189 || IPs_infected: 1000. 
All IPs infected!!!
```

