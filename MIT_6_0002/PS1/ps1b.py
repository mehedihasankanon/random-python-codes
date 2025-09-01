###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1

def process_dp(egg_weights = [], current_index = 0, current_weight = 0, current_number = 0, target_weight = 0, memo = {}):
    
    if current_index >= len(egg_weights):
        return
    
    if current_weight > target_weight:
        return
    
    memo[current_weight] = min(memo.get(current_weight, 99999999999), current_number)
    
    process_dp(egg_weights, current_index, current_weight + egg_weights[current_index], current_number + 1, target_weight, memo)
    process_dp(egg_weights, current_index + 1, current_weight, current_number, target_weight, memo)
    
        


def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # this is basically the coin change problem LMAO
    
    process_dp(list(egg_weights), 0, 0, 0, target_weight, memo)
    print(memo)
    return memo.get(target_weight, -1)

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()