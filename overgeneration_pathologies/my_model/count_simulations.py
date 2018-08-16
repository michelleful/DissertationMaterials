from simulation import Simulation

count_at_least_one_nonconcat = 0
count_at_least_half_nonconcat = 0
count_at_least_one_unattested = 0
count_at_least_half_unattested = 0

num_words = 100

for i in range(1000):
    s = Simulation()
    counts = s.simulate(num_words)
    if counts['nonconcat_cv'] + counts['unattested'] > 1:
        count_at_least_one_nonconcat += 1
    if counts['nonconcat_cv'] + counts['unattested'] > m / 2:
        count_at_least_half_nonconcat += 1
    if counts['unattested'] > 1:
        count_at_least_one_unattested += 1
    if counts['unattested'] > m / 2:
        count_at_least_half_unattested += 1

print(count_at_least_one_nonconcat)
print(count_at_least_half_nonconcat)
print(count_at_least_one_unattested)
print(count_at_least_half_unattested)


# num_words = 20
# i = 1000
# 998  at least one nonconcat
# 142  at least half nonconcat
# 998  at least one unattested
# 115  at least half unattested

# num_words = 100
# i = 1000
# 1000 at least one nonconcat
# 3 at least half nonconcat
# 1000 at least one unattested
# 1 at least half unattested
