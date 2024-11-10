def findSmallestAppealing(old_code: str, k: int) -> str:
    def is_attractive(num_str: str, k: int) -> bool:
        for i in range(len(num_str)):
            if i + k < len(num_str) and num_str[i] != num_str[i + k]:
                return False
        return True

    def generate_next_pattern(current: str, k: int) -> str:
        n = len(current)
        # Get the first k digits
        prefix = current[:k]

        # Try repeating current prefix first
        pattern = prefix * ((n + k - 1) // k)
        pattern = pattern[:n]

        if pattern >= current:
            return pattern

        # Need to increment the prefix
        curr_prefix = int(prefix)
        next_prefix = str(curr_prefix + 1)

        # Handle cases where prefix becomes longer than k
        if len(next_prefix) > k:
            next_prefix = "1" + "0" * (k - 1)

        # Pad with zeros if needed
        next_prefix = next_prefix.zfill(k)

        # Create the full pattern
        pattern = next_prefix * ((n + k - 1) // k)
        return pattern[:n]

    current = old_code
    while True:
        if is_attractive(current, k):
            return current
        current = generate_next_pattern(current, k)
