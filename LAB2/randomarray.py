import random
def generate_random_array(start_range, end_range):
    if end_range == 0 or start_range >= end_range:
        return []
    return [random.randint(start_range, end_range) for _ in range(end_range-start_range)]