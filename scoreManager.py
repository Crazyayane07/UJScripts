import csv

class ScoreManager():

    def __init__(self):
        self.score = 0

    def addDefaultScore(self):
        self.score += 1

    def reset(self):
        self.score = 0

    def saveNewScore(self):
        with open('scores.csv','a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([str(self.score)])

    def getSavedScores(self):
        scores = []
        with open('scores.csv', newline='') as csvfile:
            writer = csv.reader(csvfile)
            for row in writer:
                if len(row) > 0:
                    scores.append(int(row[0]))
        return scores