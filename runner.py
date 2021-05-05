import  k_means


class Runner:
    def __init__(self,runs,points):
        self.points=points
        for run in runs:
            k_mean =k_means.KMeans(run["k"],run["iriration"])
            k_mean.run(self.points,run["seed"])
        pass
