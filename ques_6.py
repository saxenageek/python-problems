#...#
#...#
imat = [["#","#"],["#","#"]]
count = 0

for i in range(0, len(imat)):
	cols = imat[i]
	for j in range(0, len(cols)):
		if i == 0 and (j == 0 or j == len(cols) - 1) and cols[j] == "#":
			count += 2
		if i == 0 and j > 0 and j < len(cols) - 1 and cols[j] == "#":
			count += 1
		if i == 0 and cols[j] == "." and cols[j+2] != "." and i < len(cols) - 3:
			count += 1
		if i == 0 and cols[j] == "#":
			count += 1

print(count)
