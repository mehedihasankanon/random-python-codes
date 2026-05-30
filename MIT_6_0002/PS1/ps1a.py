###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import copy

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    with open(filename, "r") as File:
        dic = {}
        lines = File.readlines()
        for line in lines:
            # print(line)
            ls = line.split(',')
            dic[ls[0]] = ls[1]
        return dic        
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    copy_cows = copy.deepcopy(cows)
    ans = []
    
    while copy_cows:
        current_list = []
        temp_store = {}
        temp_lim = 0
        while temp_lim < limit and copy_cows:
            max_key = max(copy_cows, key = copy_cows.get)
            if int(copy_cows[max_key]) + temp_lim > limit:
                temp_store[max_key] = copy_cows[max_key]
            else:
                current_list.append(max_key)
                temp_lim += int(copy_cows[max_key])
            
            copy_cows.pop(max_key)
            
        for k,v in temp_store.items():
            copy_cows[k] = v
        
        ans.append(current_list)
        
    return ans

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    partitions = list(get_partitions(cows))
    
    # print(partitions)
    
    opt_part = None
    for partition in partitions:
        possible_to_do_it = True
        for partition_level in partition:
            current_limit = 0
            for item in partition_level:
                current_limit += int(cows[item])
                if current_limit > limit:
                    possible_to_do_it = False
                    break
            if not possible_to_do_it:
                break
        if possible_to_do_it:
            if not opt_part or len(partition) < len(opt_part):
                opt_part = partition
                
    return opt_part
    
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    
    FILENAME = 'ps1_cow_data.txt'
    
    cows = load_cows(FILENAME)
    
    print(greedy_cow_transport(cows))
    print(brute_force_cow_transport(cows))
    
    
    pass


compare_cow_transport_algorithms()