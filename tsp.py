import math
import sys
from common import print_tour, read_input


def greedy(distance,cities):
    n = len(cities)
    tour = [] 
    not_visited_cities = set(range(1,n))

    for i in range(n):
        current_city = i 
        new_tour = [current_city]
        not_visited_cities = set(range(1,n))
        while not_visited_cities:
            next_city = min(not_visited_cities,key = lambda city: distance[current_city][city]) #未訪問の都市のうち最短距離のものを辿る
            not_visited_cities.remove(next_city)
            new_tour.append(next_city)
            current_city = next_city
    
        if culculate_length(distance,tour) > culculate_length(distance,new_tour) or tour == []:
            tour = new_tour.copy()

    return tour

def two_opt(distance,tour):
    n = len(tour)
    while True:
        cross = False
        for i in range(n - 2):
            for j in range(i + 2,n):
                if distance[tour[i]][tour[(i + 1) % n]] + distance[tour[j]][tour[(j + 1) % n]] > distance[tour[i]][tour[j]] + distance[tour[(i + 1) % n]][tour[(j + 1) % n]]:
                    tour[i + 1: j + 1] = (tour[i + 1: j + 1])[::-1]
                    cross = True
                    break
        if cross == False:
            break
    return tour

def culculate_length(distance,tour):
    n = len(tour)
    length = 0
    for i in range(len(tour)):
        length += distance[tour[i]][tour[(i + 1) % n]]

    return length
        
def solve(cities):
    n = len(cities)
    distance = [[0] * n for i in range(n)] #都市間の距離を記録する行列
    for i in range(n):
        for j in range(n):
            distance[i][j] = math.sqrt((cities[i][0]-cities[j][0]) ** 2 + (cities[i][1]-cities[j][1]) ** 2)

    tour = greedy(distance, cities) #貪欲法
    tour = two_opt(distance,tour) #2-opt

    length = culculate_length(distance, tour)
    return tour, length

if __name__ == "__main__":
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
    
