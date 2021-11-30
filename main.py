round_down = lambda n: round_down(n - 1) if n % 3 != 0 else n
multiply_by_onefive = lambda amount, years: amount * 1.5 * (round_down(years) / 3)
renewal_calc = lambda amount, years: multiply_by_onefive(amount, years) if int(multiply_by_onefive(amount, years)) else amount


if __name__ == '__main__':
    print(renewal_calc(50000, 2))
