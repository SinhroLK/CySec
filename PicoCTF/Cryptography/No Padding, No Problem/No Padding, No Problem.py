from Crypto.Util.number import long_to_bytes
n= 103029907312908898652247798979642726048330304548114790647620058610333259603260529232770178799554435476410982675745390035749403293329153570257572577172703079210052258419701572972227532072398835338099278160182317408045677505477802365454887333918209367804032666332374395553035804781235268085504496818935321728741
e= 65537
ciphertext= 6897118380825859504816863627453946103600659886479188027333867178704872907173507442716437060843150816153216971645604709646662959177458439618734817297594144991744872337358754868542048416489130524538686532582007469551094825236456588065790717712018404168777412966065159706009321641583820092729029087783794040107
print(ciphertext+n)
decrypt = 290275030195850039473456618367455885069965748851278076756743720446703314517401359267322769037469251445384715145100230277245
print(long_to_bytes(decrypt))