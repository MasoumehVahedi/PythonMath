"""
   There are A cities numbered from 1 to A. You have already visited M cities, the indices of which are given in an array B of M integers.

   If a city with index i is visited, you can visit either the city with index i-1 (i >= 2) or the city with index i+1 (i < A) if they
   are not already visited. Eg: if N = 5 and array M consists of [3, 4], then in the first level of moves, you can either visit 2 or 5.

   You keep visiting cities in this fashion until all the cities are not visited. Find the number of ways in which you can visit all the
   cities modulo 10^9+7.

    Problem Constraints
    1 <= A <= 1000
    1 <= M <= A
    1 <= B[i] <= A


    Input Format
    The 1st argument given is an integer A, i.e total number of cities.
    The 2nd argument given is an integer array B, where B[i] denotes ith city you already visited.


    Output Format
    Return an Integer X % (1e9 + 7), the number of ways in which you can visit all the cities.


    Example Input:
        A = 5
        B = [2, 5]


    Example Output:
        6

    Example Explanation
    All possible ways to visit remaining cities are:
    1. 1 -> 3 -> 4
    2. 1 -> 4 -> 3
    3. 3 -> 1 -> 4
    4. 3 -> 4 -> 1
    5. 4 -> 1 -> 3
    6. 4 -> 3 -> 1


    Solution:
    According to the constraints, we can solve this problem in O(N ^ 2).
    First, find all groups of consecutive unvisited cities and calculate the number of ways to combine them.
    Then for each group calculate the number of ways to visit all the cities of that group.

"""


####### Solution 1: Not totally correct ########
"""from itertools import permutations

def city_tour(A: int, B: list) -> int:
    # @param A : integer
    # @param B : list of integers
    # @return an integer

    unique_num = []
    for i in range(1, A+1):
        if i not in B:
            unique_num.append(i)

    all_routes = list(permutations(unique_num))
    # print(all_routes)
    for idx, route in enumerate(all_routes, start=1):
        print(f"{idx}. {' -> '.join(map(str, route))}")

    return len(all_routes)"""



####### Solution 2: Totally correct ########

MOD = 10**9 + 7

def cityTour(A: int, B: list) -> int:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    visited = set(B)
    return visitedCity(A, visited)


def visitedCity(A, visited):
    if len(visited) == A:
        return 1

    count = 0
    next_cities = set()

    # Find all unvisited cities adjacent to visited ones
    for city in visited:
        if city > 1 and (city - 1) not in visited:
            next_cities.add(city - 1)
        if city < A and (city + 1) not in visited:
            next_cities.add(city + 1)

    # Try visiting each possible next city
    for next_city in next_cities:
        visited.add(next_city)
        count = (count + visitedCity(A, visited)) % MOD
        visited.remove(next_city)

    return count




if __name__ == "__main__":
    A = 5
    B = [2, 5]
    count = cityTour(A, B)
    print(count)



