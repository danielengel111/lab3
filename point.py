class Point:
    def __init__(self, name, coordinates=None):
        self.name = name
        self.coordinates = []
        if coordinates:
            self.set_coordinates(coordinates)

    def distance_to(self, coordinates):
        if not self.coordinates:
            print('Point', self.name, 'not initiated. Please provide coordinates in init or call set_coordinates')
            return 0
        dis=0
        for my, his in zip(self.coordinates, coordinates):
            if((my-his)<0):
                dis+=his-my
            else:
                dis+=my-his
        return dis
        #return sum([(my-his) for my, his in zip(self.coordinates, coordinates)])

    def set_coordinates(self, coordinates):
        self.coordinates = [float(x) for x in coordinates]
