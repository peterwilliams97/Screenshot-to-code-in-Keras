from math import log
# Melbourne's current population
pop0 = 4.8e6

# Current year
year0 = 2018


def population(year, rate):
    """Returns Melbourne's population in year `year` after growing at rate 'rate' from today's
        population
        'rate' is a percentage
    """
    # Convert percentage growth rate to a ratio
    r = 1.0 + rate / 100.0

    # Number of years from now until `year`
    n_years = year - year0

    return int(pop0 * r ** n_years)


def doubles(rate):
    return reaches(rate, 2.0 * pop0)


def reaches(rate, pop):
    r = 1.0 + rate / 100.0
    assert pop > pop0, (pop, pop0, pop / pop0)
    return log(pop / pop0, r)


australia = 2.47e7
aussie = [100.0 * x / australia for x in (1.75e5, 3.5e5, 5e5)]
rates = [0.5, 1, 2, 2.4] + aussie
assert all(rates)


for rate in rates:
    print('Growth rate: %.1f%% (%d K / year)' % (rate, int(rate * australia / 1000 / 100)))
    d = doubles(rate)
    r12 = reaches(rate, 1.2e7)
    print('Doubles in %.1f years (%d)' % (d, int(d + year0)))
    print('Reaches 12 M in %.1f years (%d)' % (r12, int(r12 + year0)))
    for year in (2030, 2050, 2070, 2090):
        pop = population(year, rate)
        print('\tyear=%d population=%.1f M' % (year, pop / 1e6))
