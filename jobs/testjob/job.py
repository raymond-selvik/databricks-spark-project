class Job:
    def __init__(self, sparkContext):
        self.sparkContext = sparkContext

    def sparkVersion(self):
        print(self.sparkContext.version)