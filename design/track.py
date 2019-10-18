# You have a bunch of runners, running on a track. On the track, there are Y number of checkpoints. Design a system which will:

def getTime(runner):
    return runner.time

class CheckPoint():
    def __init__(self):
        self.finished = []

    def addFinisher(self, runnerID):
        self.finished.append(runnerID)

class Runner():
    def __init__(self,ID):
        self.runnerID = ID
        self.time = 0.00
        self.finished = False

class Track():
    def __init__(self, Y):
        self.checkpoints = [CheckPoint() for _ in range(Y)]
        self.runners = []

    # Logs a runner at the given checkpoint
    #(@signature Track int int -> None)
    def checkpoint(self, runnerId, checkpoint):
        checkpoint.addFinisher(runnerId)

    # return list of runner IDs of runners who have not finished yet but are k fastest on the track
    #(@signature Track int -> [int])
    def firstKRunners(self, k):
        ordered = self.runners.sort(key=getTime)
        return ordered[:k]

    # assume at least 3 ppl have finished, return their runner IDs
    #(@signature Track None -> [int])
    def top3Finishers(self):
        finished = [x for x in self.runners if x.finished]
        return self.firstKRunners(finished)
