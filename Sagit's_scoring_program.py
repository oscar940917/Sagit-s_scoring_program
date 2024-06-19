def calculate_score(N):
    if N <= 10:
        return N * 6
    elif N <= 20:
        return 10 * 6 + (N - 10) * 2
    elif N <= 40:
        return 10 * 6 + 10 * 2 + (N - 20) * 1
    else:
        return 100

def main():
    import sys
    input_data = sys.stdin.read().strip()
    N = int(input_data)
    print(calculate_score(N))

if __name__ == "__main__":
    main()
