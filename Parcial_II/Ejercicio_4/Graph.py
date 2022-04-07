import matplotlib.pyplot as plt

if __name__ == "__main__":
    file = open("time.txt", "r")
    
    index, fr, ftr, fi = [], [], [], []
    for line in file:
        times = line.split(" ")

        if (times[0] != "ERROR"):
            times = list(map(int, times))
            index.append(times[0])
            fr.append(times[1])
            ftr.append(times[2])
            fi.append(times[3])

    file.close()
    plt.figure(figsize=(10,30))
    plt.plot(index, fr, 'r-')
    plt.plot(index, ftr, 'b-')
    plt.plot(index, fi, 'g-')
    plt.legend(['Recursive', 'Tail recursive', "Iterative"])
    plt.rcParams['ytick.labelsize'] = 6
    plt.show()

