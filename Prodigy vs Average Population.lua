--[[
IQ   P (lowest)
101    0.05
102    0.15
103    0.2
105    0.3
106    0.35
110    0.65
120    0.75
130    0.8
138    0.9
140    0.9
150    0.9

]]



-- assumption: intelligence increase the probability of winning

population = 100				-- population
wealth = 1000					-- total asset
total_simulation = 9900000		-- total simulation
bet = 100

population_iq = 100
prodigy_iq = 102

n = {}

math.randomseed(os.time())

function not_bankrupt()
	arr = {}
	for i=1, population do
		if n[i].wealth > 0 then
			table.insert(arr, i)
		end
	end
	return arr
end

function economy()
	for i=1, population do
		n[i] = {
			iq = population_iq,			-- or general ability
			wealth = wealth,
			}
	end
	
	n[1].iq = prodigy_iq		-- higher than average iq

	for i=1, total_simulation do
		ppl = not_bankrupt()
		if #ppl <= 1 then break end
		
		r1 = ppl[ math.random(1,#ppl) ]
		r2 = ppl[ math.random(1,#ppl) ]
		
		if r1 ~= r2 then
			P1 = n[r1].iq / (n[r1].iq + n[r2].iq)
			if P1 > math.random() then
				if n[r2].wealth >= bet then
					n[r2].wealth = n[r2].wealth - bet
					n[r1].wealth = n[r1].wealth + bet
				elseif n[r2].wealth < bet then
					n[r1].wealth = n[r1].wealth + n[r2].wealth
					n[r2].wealth = 0
				end
			else
				if n[r1].wealth >= bet then
					n[r1].wealth = n[r1].wealth - bet
					n[r2].wealth = n[r2].wealth + bet
				elseif n[r1].wealth < bet then
					n[r2].wealth = n[r2].wealth + n[r1].wealth
					n[r1].wealth = 0
				end
			end
		end
	end

	return n[1].wealth
end

	--money = 0

	--for i in range(0, population):
		--print(i, n[i]['iq'], n[i]['wealth'])
		--#money += n[i]['wealth']

--print('total circulated money:', money)

total = 20
c = 0

for i=1, total do
	s = economy()
	print(i .. ' -> ' .. s)
	--io.flush()
	io.stdout:flush()
	if s > 0 then
		c = c + 1
	end
end
	
print('P = ' .. c/total)




