import random
def initialize_state():
    """
    Initialize the Keccak state with a capacity portion of all zeros
    and a rate portion with at least one nonzero bit per lane.
    """
    state = [[0] * 5 for _ in range(5)]  # 5x5 state matrix
    
    # Rate lanes (assumed nonzero in the first block P0)
    for x in range(5):
        for y in range(5):
            if x + 5 * y < 1024 // 64:  # 1024-bit rate divided into 64-bit lanes
                state[x][y] = random.randint(1, 0xFFFFFFFFFFFFFFFF)  # At least one nonzero bit
    return state

def track_zero_capacity(state):
    """
    Track the number of zero-initialized capacity lanes still unchanged.
    """
    zero_capacity = set()
    for x in range(5):
        for y in range(5):
            if x + 5 * y >= 1024 // 64:  # Capacity portion (initially all zero)
                zero_capacity.add((x, y))
    return zero_capacity

def absorb_message(state, zero_capacity):
    """
    Absorb message blocks into the state and track the zero capacity lanes.
    """
    rounds = 0
    while zero_capacity:
        rounds += 1
        new_values = [(x, y) for (x, y) in list(zero_capacity) if random.getrandbits(1)]
        for (x, y) in new_values:
            state[x][y] = random.randint(1, 0xFFFFFFFFFFFFFFFF)  # Introduce randomness
            zero_capacity.remove((x, y))
    return rounds

def main():
    state = initialize_state()
    zero_capacity = track_zero_capacity(state)
    rounds = absorb_message(state, zero_capacity)
    print(f"It took {rounds} rounds before all capacity lanes had at least one nonzero bit.")

if __name__ == "__main__":
    main()
