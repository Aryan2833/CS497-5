def lexicalOrder(n):
    result = []

    current = 1
    for _ in range(n):
        result.append(current)

        if current * 10 <= n:
            current *= 10
        elif current + 1 <= n and current % 10 < 9:
            current += 1
        else:
            while (current // 10) % 10 == 9:
                current //= 10
            current = current // 10 + 1

    return result

# Test cases
n1 = 13
print(lexicalOrder(n1))

n2 = 2
print(lexicalOrder(n2)) 
