from sys import argv
import os
from point import Point
from k_means import KMeans


def load_data(input_path):
    """
    Loads data from given csv
    :param input_path: path to csv file
    :return: returns data as list of Point
    """
    points = []
    with open(input_path, 'r') as f:
        for row in f.readlines():
            row = row.strip()
            values = row.split(' ')
            points.append(Point(values[0], values[1:]))
    return points

def itirate_kmeans(k,num_iterations,random_seed,points):
    runner = KMeans(k, num_iterations)
    runner.run(points, random_seed)
    runner.print_distance(random_seed)


def run_kmeans():
    if len(argv) < 4:
        print('Not enough arguments provided. Please provide 3 arguments: K, num_iterations, path_to_input')
        exit(1)

    input_path = argv[3]
    if not os.path.exists(input_path):
        print('Input file does not exist')
        exit(1)
    points = load_data(input_path)
    print("seed K SL1")
    if len(argv) == 5:
        for random_seed in [1, 12]:
            for k in [3,4,5]:
            #k = int(argv[1])
                for num_iterations in [10]:
            #num_iterations = int(argv[2])
                    if k <= 1 or num_iterations <= 0:
                        print('Please provide correct parameters')
                        exit(1)
                    if k >= len(points):
                        print('Please set K less than size of dataset')
                        exit(1)

                    itirate_kmeans(k, num_iterations, random_seed, points)
                        #random_seed = int(argv[4])


if __name__ == '__main__':
    run_kmeans()
