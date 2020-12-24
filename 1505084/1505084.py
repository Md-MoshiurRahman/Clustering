import random
import matplotlib.pyplot as plt
import numpy as py

def dataPrepos(filetrain):
    lines = filetrain.readlines()
    data = []
    datax = []
    datay = []
    for i in range(len(lines)):
        inner = []
        line = lines[i].split()
        for value in line:
            inner.append(float(value))
        data.append(inner)
        datax.append(float(line[0]))
        datay.append(float(line[1]))

    return data,datax,datay


def DBSCAN(data,eps,minpts):
    distance = []
    for i in range(len(data)):
        inner = []
        distance.append(inner)

    for i in range(len(data)):
        for j in range(len(data)):
            dis = (data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2
            distance[i].append(dis)

    forthdistance = []
    count = []
    for i in range(len(data)):
        distance[i].sort()
        forthdistance.append(distance[i][minpts-1])
        count.append(i)
    forthdistance.sort()

    plt.plot(count, forthdistance)
    plt.xlabel('Points Sorted According to 4th Nearest Neighbour')
    plt.ylabel('4-th Nearest Neighbour Distance')
    plt.show()

    corepoints = []
    visited = []
    for i in range(len(data)):
        if distance[i][minpts-1] >= eps:
            corepoints.append(i)
        visited.append(0)

    #print(len(corepoints))
    clustercount = 0
    clusterpoints = [[],[]]

    for i in range(len(corepoints)):
        if visited[corepoints[i]] != 1:
            clustercount += 1
            clusterpoints[0].append(data[corepoints[i]][0])
            clusterpoints[1].append(data[corepoints[i]][1])
        for j in range(len(data)):
            dis = (data[corepoints[i]][0] - data[j][0]) ** 2 + (data[corepoints[i]][1] - data[j][1]) ** 2
            if dis <= eps:
                visited[j] = 1


    #print(clustercount)
    plt.scatter(clusterpoints[0], clusterpoints[1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    return clustercount



def K_means(data,datax,datay,k):
    clusters = []
    clustermeancount = []
    clustersum = []
    for i in range(k):
        index = random.randint(0, len(data))
        clusters.append([datax[index],datay[index]])
        clustermeancount.append(0)
        clustersum.append([0,0])
        print(index)

    datawithclus = []
    for i in range(len(data)):
        datawithclus.append(-1)

    for l in range(600):
        for i in range(len(data)):
            min = 99999
            minindex = -1
            for j in range(len(clusters)):
                dis = (data[i][0] - clusters[j][0]) ** 2 + (data[i][1] - clusters[j][1]) ** 2
                if dis < min:
                    min = dis
                    minindex = j
            datawithclus[i] = minindex

        # print(datawithclus)
        for i in range(len(data)):
            clustersum[datawithclus[i]][0] += data[i][0]
            clustersum[datawithclus[i]][1] += data[i][1]
            clustermeancount[datawithclus[i]] += 1

        for i in range(k):
            clusters[i][0] = clustersum[i][0] / clustermeancount[i]
            clusters[i][1] = clustersum[i][1] / clustermeancount[i]

        #print(clusters)

    plt.scatter(datax, datay, label="dot", c=datawithclus, cmap="rainbow" , marker=".", s=20)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == "__main__":
    filetrain = open("moons.txt")
    data,datax,datay = dataPrepos(filetrain)
    eps =0.030
    minpts = 4
    clustercount = DBSCAN(data,eps,minpts)
    K_means(data, datax, datay, clustercount)

    #filetrain = open("blobs.txt")
    #data, datax, datay = dataPrepos(filetrain)
    #eps = 1.5
    #minpts = 4
    #clustercount = DBSCAN(data, eps, minpts)
    #K_means(data, datax, datay, clustercount)

    #filetrain = open("bisecting.txt")
    #data, datax, datay = dataPrepos(filetrain)
    #eps = 0.285
    #minpts = 4
    #clustercount = DBSCAN(data, eps, minpts)
    #K_means(data, datax, datay, clustercount)
