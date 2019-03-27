import random
import numpy as np
import matplotlib.pyplot as plt

OMEGA = 100000    # number of ip addresses
NUM_VULNERABLE = 1000     # total number of vulnerable ip addresses
SCAN_RATE = 3
SIMULATION_END_TIME = 10000

def generate_data():
    ip_addr_space = {}
    for i in range(OMEGA):
        ip_addr_space[i+1] = 'immune'

    for j in range(NUM_VULNERABLE/10):
        for k in range(10):
            ip_addr_space[k+1+(j*1000)] = 'vulnerable'

    return ip_addr_space



def random_scanning(runs = 1, plot=True):
    for run in range(runs):
        print("\n*********Beginning Random Scanning Worm Propagation: Simulation {}***********".format(run+1))
        ip_addr_space = generate_data()
        ip_addr_space[1001] = 'infected'
        infected_count = 1
        y_axis = []
        for i in range(SIMULATION_END_TIME):
            num_of_IPs_to_scan = infected_count * SCAN_RATE
            random_ips = random.sample(range(1, OMEGA+1), num_of_IPs_to_scan)
            for ip in random_ips:
                if ip_addr_space[ip] == 'immune':
                    pass
                elif ip_addr_space[ip] == 'infected':
                    pass
                elif ip_addr_space[ip] == 'vulnerable':
                    ip_addr_space[ip] = 'infected'
                    infected_count += 1
                    if infected_count == 1000:
                        break

            if (i+1)%100 == 0:
                print("Simulation tick: {0} || IPs_infected: {1}".format(i+1, infected_count))

            y_axis.append(infected_count)

            if infected_count == 1000:
                print("Simulation tick: {0} || IPs_infected: {1}. \nAll IPs infected!!!".format(i+1, infected_count))
                break

        if run==0:
            plt.plot(y_axis, "-", label = "Run #{}".format(run+1))
        elif run==1:
            plt.plot(y_axis, "-.", label = "Run #{}".format(run+1))
        elif run==2:
            plt.plot(y_axis, ":", label = "Run #{}".format(run+1))
        else:
            plt.plot(y_axis, label = "Run #{}".format(run+1))

    if plot:
        plt.xlabel("Time tick")
        plt.ylabel("Number of infected computers")
        plt.title("Random Scanning: {} Simulation Runs of Worm Propagation".format(runs))
        plt.legend()
        plt.show()


def get_IPs_with_local_preference(ip_addr_space, scan_rate):
    list_IPs_to_scan = []
    # np.random.choice([ ,range(1, OMEGA+1)], , p=[0.8,0.2] )
    for ip in ip_addr_space:
        if ip_addr_space[ip] == 'immune':
            pass
        elif ip_addr_space[ip] == 'vulnerable':
            pass
        elif ip_addr_space[ip] == 'infected':
            for _ in range(scan_rate):
                if ip<=10:
                    # preference = np.random.choice([range(0,ip+1+10),range(1, OMEGA+1)], 1 , p=[0.8,0.2] )
                    preference = np.random.choice(['local','global'], 1 , p=[0.8,0.2] )
                    if preference=='local':
                        result = random.sample(range(1,ip+1+10), 1)
                    elif preference == 'global':
                        result = random.sample(range(1, OMEGA+1), 1)
                elif ip >= (OMEGA - 10):
                    preference = np.random.choice(['local','global'], 1 , p=[0.8,0.2] )
                    if preference=='local':
                        result = random.sample(range(ip-10, OMEGA+1), 1)
                    elif preference == 'global':
                        result = random.sample(range(1, OMEGA+1), 1)
                else:
                    preference = np.random.choice(['local', 'global'], 1, p=[0.8, 0.2])
                    if preference == 'local':
                        result = random.sample(range(ip - 10, ip+1+10), 1)
                    elif preference == 'global':
                        result = random.sample(range(1, OMEGA + 1), 1)

                list_IPs_to_scan.append(result[0])

    return list_IPs_to_scan


def local_preference_scanning(runs = 1, plot=True):
    for run in range(runs):
        print("\n*********Beginning Local Preference Scanning Worm Propagation: Simulation {}***********".format(run+1))
        ip_addr_space = generate_data()
        ip_addr_space[1001] = 'infected'
        infected_count = 1
        y_axis = []
        for i in range(SIMULATION_END_TIME):
            random_ips = get_IPs_with_local_preference(ip_addr_space, SCAN_RATE)
            for ip in random_ips:
                if ip_addr_space[ip] == 'immune':
                    pass
                elif ip_addr_space[ip] == 'infected':
                    pass
                elif ip_addr_space[ip] == 'vulnerable':
                    ip_addr_space[ip] = 'infected'
                    infected_count += 1
                    if infected_count == 1000:
                        break

            if (i+1)%100 == 0:
                print("Simulation tick: {0} || IPs_infected: {1}".format(i+1, infected_count))

            y_axis.append(infected_count)

            if infected_count == 1000:
                print("Simulation tick: {0} || IPs_infected: {1}. \nAll IPs infected!!!".format(i+1, infected_count))
                break

        if run==0:
            plt.plot(y_axis, "-", label = "Run #{}".format(run+1))
        elif run==1:
            plt.plot(y_axis, "-.", label = "Run #{}".format(run+1))
        elif run==2:
            plt.plot(y_axis, ":", label = "Run #{}".format(run+1))
        else:
            plt.plot(y_axis, label = "Run #{}".format(run+1))

    if plot:
        plt.xlabel("Time tick")
        plt.ylabel("Number of infected computers")
        plt.title("Local Preference Scanning: {} Simulation Runs of Worm Propagation".format(runs))
        plt.legend()
        plt.show()



if __name__ == '__main__':
    random_scanning(runs=3, plot = True)
    local_preference_scanning(runs=3, plot= True)