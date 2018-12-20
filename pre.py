import pandas as pd


def txt2csv():
    for i in range(26):
        name = "/home/wml/PycharmProjects/SimulatingPedestrianMovement/data/" + str(i + 1) + ".txt"
        rename = "/home/wml/PycharmProjects/SimulatingPedestrianMovement/data/" + str(i + 1) + ".csv"
        f = open(name, 'r')
        string = f.read()
        string = string.replace("    ", ",")
        res = open(rename, 'w')
        res.write("x,y\n")
        res.write(string)
        res.flush()


def TrainGenerate():
    info =
    for i in range(26):
        name = "/home/wml/PycharmProjects/SimulatingPedestrianMovement/data/" + str(i + 1) + ".csv"
        rename = "/home/wml/PycharmProjects/SimulatingPedestrianMovement/data/" + str(i + 1) + "_train.csv"
        f = pd.read_csv(name)

        return 0

#txt2csv()
TrainGenerate()
