# 
# assumption: intelligence increase the probability of winning

import random

population = 100		# population
wealth = 1000			# total asset
total_simulation = 9900000		# total simulation
bet = 100

population_iq = 100
prodigy_iq = 120

n = {}

def not_bankrupt():
	global population, n
	arr = list()
	for i in range(0, population):
		if n[i]['wealth'] > 0:
			arr.append(i)
	return arr

def economy():
	global population, wealth, total_simulation, bet, n

	for i in range(0, population):
		n[i] = {
			'iq': population_iq,			# or general ability
			'wealth': wealth,
			}
		
	n[0]['iq'] = prodigy_iq		# higher than average iq

	for i in range(0, total_simulation):
		#n[i]['iq'] = 
		#print(i)
		ppl = not_bankrupt()
		if len(ppl) <= 1: break
		r1 = ppl[ random.randint(0, len(ppl)-1) ]
		r2 = ppl[ random.randint(0, len(ppl)-1) ]
		
		
		
		#print(r1, n[r1]['iq'])
		if r1 != r2:
			P1 = n[r1]['iq'] / (n[r1]['iq'] + n[r2]['iq'])
			if P1 > random.uniform(0,1):
				if n[r2]['wealth'] >= bet:
					n[r2]['wealth'] -= bet
					n[r1]['wealth'] += bet
				elif n[r2]['wealth'] < bet:
					n[r1]['wealth'] += n[r2]['wealth']
					n[r2]['wealth'] = 0
			else:
				if n[r1]['wealth'] >= bet:
					n[r1]['wealth'] -= bet
					n[r2]['wealth'] += bet
				elif n[r1]['wealth'] < bet:
					n[r2]['wealth'] += n[r1]['wealth']
					n[r1]['wealth'] = 0


	return n[0]['wealth']

	#money = 0

	#for i in range(0, population):
		#print(i, n[i]['iq'], n[i]['wealth'])
		#money += n[i]['wealth']

#print('total circulated money:', money)

total = 20
c = 0

for i in range(0, total):
	s = economy()
	print(i, '->', s)
	if s > 0:
		c += 1
	
print('P =', c/total)






'''
40 years timeframe
vs
1000 years timeframe
'''


