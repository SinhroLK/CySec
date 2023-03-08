p = 29
ints = [14, 6, 11]

residue = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(residue)}")