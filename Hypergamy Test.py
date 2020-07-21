
# Hypergamy Test (brute force algorithm)


sample_size = 1000


# women ranking shift compared to men (range from -1 to 1)
# <= -1 : all men rank higher than women
#     0 : gender equality
#  >= 1 : all women rank higher than men
#women_status_shift = 0			# gender equal
#women_status_shift = -0.45		# 16% not married (real life): -0.45
#women_status_shift = 0.291		# 75% ever divorced (real life) : 0.291
women_status_shift = .9


P = 0	# Probability of men married to a lower status women
n = 0	# total number of outcome
c = 0	# counter of occurence

# populate & set rank / social status / SMV
men = list(range(0, sample_size))
women = list(range(0, sample_size))

# set women ranking status shift
for i in range(0, sample_size):
	women[i] += sample_size*women_status_shift



for i in range(0, sample_size):
	for j in range(0, sample_size):
		n += 1
		if men[i] > women[j]:
			c += 1

print('Marriage/Mating occurence =', str(c))
print('Number of possible outcome =', n)
print('P =', str(c/n), "({0:.2%})".format(c/n) )
