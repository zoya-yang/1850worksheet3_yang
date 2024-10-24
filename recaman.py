def recaman_sequence(n):
    if n <= 0:
        return []
    sequence = [0]
    seen = {0}
    for k in range(1, n):
        prev = sequence[k - 1]
        candidate = prev - k
        if candidate > 0 and candidate not in seen:
            sequence.append(candidate)
            seen.add(candidate)
        else:
            candidate = prev + k
            sequence.append(candidate)
            seen.add(candidate)

    return sequence

n = int(input("Enter the length of the Recaman sequence: "))
result = recaman_sequence(n)

print("Recaman sequence of length", n, "is:", result)
