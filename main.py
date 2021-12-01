round_down = lambda n: round_down(n - 1) if n % 3 != 0 else n
renewal_calc = lambda amount, years: int(amount * 1.5 * (round_down(years) / 3)) or int(amount)

private_calc = lambda amount, years: int(amount * 1.5 * years) or int(amount)


if __name__ == '__main__':
    print(renewal_calc(50000, 2))
