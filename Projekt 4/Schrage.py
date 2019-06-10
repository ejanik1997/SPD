import numpy
import copy


class job:
    def __init__(self, taskid, r, p, q):
        self.taskid = taskid
        self.r = r
        self.p = p
        self.q = q

    def __str__(self):
        return str('taskid ' + str(self.taskid) + '   '+ str(self.r) + ' ' + str(self.p) + ' ' + str(self.q))

    def __getitem__(self, index):
        if index == 0:
            return self.r
        if index == 1:
            return self.p
        if index == 2:
            return self.q
        else:
            return -1

    def __setitem__ (self, index, value):
        if index == 0:
            self.r = value
        if index == 1:
            self.p = value
        if index == 2:
            self.q = value
        else:
            return -1


def read_from_file(filename):
    with open(filename) as f:
        number_of_jobs, columns = [int(x) for x in next(f).split()]
        p_time = numpy.zeros((number_of_jobs, columns)) #processing time
        for i in range(number_of_jobs):
            p_i = f.readline().split()
            for j in range(columns):
                p_time[i][j] = p_i[j]
    return columns, number_of_jobs, p_time


def schrage(D):
    order =[]
    ng = []
    nn = D
    cmax = 0
    t = min(nn, key=lambda x: x[0])[0]
    while ng != [] or nn != []:
        while nn != [] and min(nn, key=lambda x: x[0])[0] <= t:
            currtask = min(nn, key=lambda x: x[0])
            ng.append(currtask)
            nn.remove(currtask)
        if ng == []:
            t = min(nn, key=lambda x: x[0])[0]
        else:
            currtask = max(ng, key=lambda x: x[2])
            ng.remove(currtask)
            order.append(currtask)
            t = t + currtask[1]
            cmax = max(t + currtask[2], cmax)
    return order, cmax


def schragepmtn(N):
    order = []
    ng = []
    nn = N
    cmax = 0
    t = 0
    othertask = nn[0]
    while ng != [] or nn != []:
        while nn != [] and min(nn, key=lambda x: x[0])[0] <= t:
            currtask = min(nn, key=lambda x: x[0])
            ng.append(currtask)
            nn.remove(currtask)
            if currtask[2] > othertask[2]:
                temptask = copy.copy(othertask)
                temptask[1] = t - currtask[0]
                t = currtask[0]
                if temptask[1] > 0:
                    othertask[2] = 0
                    temptask[0] = 0
                    othertask[1] = othertask[1] - temptask[1]
                    ng.append(temptask)
        if ng == []:
            t = min(nn, key=lambda x: x[0])[0]
        else:
            currtask = max(ng, key=lambda x: x[2])
            ng.remove(currtask)
            othertask = currtask
            order.append(currtask)
            t = t + currtask[1]
            cmax = max(cmax, t + currtask[2])
    return order, cmax


col, nbj, data = read_from_file("in50.txt")
newdata =[]
for i in range(len(data)):
   task = job(i, data[i][0], data[i][1], data[i][2])
   newdata.append(task)


ord, cma = schrage(newdata)
for i in range(len(ord)):
   print(ord[i])
print("Cmax: ", cma)


newdata = []
for i in range(len(data)):
    task = job(i, data[i][0], data[i][1], data[i][2])
    newdata.append(task)
print("===================================")
ord, cma = schragepmtn(newdata)
for i in range(len(ord)):
    print(ord[i])
print("Cmax ", cma)



