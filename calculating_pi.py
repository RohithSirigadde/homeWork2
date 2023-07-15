def calculating_pi(n_terms: int) -> float:
    dividend: float = 4.0
    divisor: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (dividend / divisor)
        divisor += 2.0
        operation *= -1.0
    return pi

if __name__ == "__main__":
    print(calculating_pi(2000000))
#### output is 3.141592153589724
