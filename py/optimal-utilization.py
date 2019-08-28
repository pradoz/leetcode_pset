'''
Your task is to write an algorithm to optimize the sets of forward/return shipping route pairs that allow the aircraft to be optimally utilized, given a list a of forward routes and a list of return shipping routes.

INPUT
The input to the function/method consisits of three arguments:
maxTravelDist, an integer representing the maximum operating travel distance of the given aircraft;
forwardRouteList, a list of pairs of integers where the first integer represents the unique identifier of a forward shipping
route and the second integer represents the amount of travel distance required bu this shipping route;
returnRouteList, a list of pairs of integers where the first integer represents the unique identifer of a return shipping route
and the second integer represents the amount of travel distance required by this shipping route.

OUTPUT
Return a list of pairs of integers representing the pairs of IDs of forward and return shipping routes that optimally utilize the given aircraft. If no route is possible, return a list with empty pair.

Example 1:
Input:
maxTravelDist = 7000
forwardRouteList = [[1,2000],[2,4000],[3,6000]]
returnRouteList = [[1,2000]]

Output:
[[2,1]]

Explanation:
There are only three combinations [1,1],[2,1],and [3,1], which have a total of 4000, 6000, and 8000 miles, respectively. Since 6000 is the largest use that does tnot exceed 7000, [2,1] is the optimal pair.

Example 2:
Input:
maxTravelDist = 10,000
forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

Output:
[[2,4],[3,2]]

Explanation:
There are two pairs of forward and return shipping routes possible that optimally utilizes the given aircraft. Shipping Route ID#2 from the forwardShippingRouteList, required 5000 miles travelled, and Shipping Route ID#4 from returnShippingRouteList also required 5000 miles travelled. Combined, they add up to 10000 miles travelled. Similarily, Shipping Route ID#3 from forwardShippingRouteList requires 7000 miles travelled, and Shippping Route ID#2 from returnShippingRouteList requires 3000 miles travelled. These also add up to 10000 miles travelled. Therefore, the pairs of forward and return shipping routes that optimally utilize the aircraft are [2,4] and [3,2].
'''
def final_distance_traveled(maxTravelDist: int,
                            forwardRouteList,
                            returnRouteList: [[int]]) -> [int]:
    # sort the list by the first argument
    returnRouteList = sorted(returnRouteList, key=lambda x: x[1])
    return iter_binary_search(forwardRouteList, returnRouteList, maxTravelDist)

def iter_binary_search(l1, l2: [int], val: int):
    max_dict = {}
    for elem in l1:
        print(type(elem), elem[1], type(val))
        current_distance_to_location = val - elem[1]
        idx = binary_search(l2, current_distance_to_location)

        if idx == -1:
            continue
        else:
            best_dist = elem[1] + l2[idx][1]
            max_dict[best_dist] = max_dict.get(best_dist, []) + [[elem[0], l2[idx][0]]]

        if len(max_dict) == 0:
            return []
        print(max_dict.keys())
    return max_dict[max(max_dict.keys())]


def binary_search(lst: [int], target_distance: int) -> int:
    if len(lst) == 1 and lst[0][1] < target_distance:
        return 0

    if target_distance < 0:
         return -1

    idx = -1
    start = 0
    end = len(lst) - 1
    mid = (end - start) // 2

    while (end - start) >= 1:
        if lst[mid][1] == target_distance:
            return mid
        elif lst[mid][1] < target_distance:
            start = mid + 1
            mid = start + (end - start) // 2
            idx = mid
        else:
            end = mid - 1
            mid = start + (end - start) // 2
    return idx


maxTravelDist = 7000
forwardRouteList = [[1,2000],[2,4000],[3,6000]]
returnRouteList = [[1,2000]]
# print(final_distance_traveled(maxTravelDist, forwardRouteList, returnRouteList))
# [[2, 1]]

maxTravelDist = 10000
forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]
print(final_distance_traveled(maxTravelDist, forwardRouteList, returnRouteList))
# [[2,4],[3,2]]