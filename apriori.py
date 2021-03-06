#count keys in D
def getC(D,keys):
	C=[]
	for key in keys:
		c=0
		for T in D:
			have=True
			for k in key:
				if k not in T:
					have=False
			if have:
				c+=1
		C.append(c)
	return C

#cut the keys with count less than minSup*length
def getCutKeys(keys,C,minSup,length):
	for i,key in enumerate(keys[:]):
		if float(C[i])/length<minSup:
			keys.remove(key)
	return keys

def keyinT(key,T):
	for k in key:
		if k not in T:
			return False
	return True

def apriori_gen(keys1,Last_keys):
	keys2=[]
	if [] in keys1:
		keys1.remove([])
	for i,k1 in enumerate(keys1):
		for j,k2 in enumerate(keys1):
			if i<j:
				key=[]
				length=len(k1)
				Same=True
				for l in range(length-1):
					if (k1[l]!=k2[l]):
						Same=False
					key.append(k1[l])
					

				
				if Same==True and (k1[length-1]!=k2[length-1]):
					c=k2[length-1]
					key.append(k1[length-1])
					key.append(c)
					key.sort()
					if key not in keys2:
						keys2.append(key)

					for i1,word1 in enumerate(key):
						rem=[]
						for j1,word2 in enumerate(key):
							if j1!=i1:
								rem.append(word2)
						rem.sort()
						if rem not in Last_keys:
							if key in keys2:
								keys2.remove(key)
					
	return keys2


def Apriori(D,minSup):
	C1={}
	for T in D:
		for I in T:
			if I in C1:
				C1[I]+=1
			else:
				C1[I]=1
	
	_keys1=C1.keys()
	
	keys1=[]
	for i in _keys1:
		keys1.append([i])

	n=len(D)
	cutKeys1=[]
	for k in keys1:
		if C1[k[0]]*1.0/n>=minSup:
			cutKeys1.append(k)

	cutKeys1.sort()
	
	keys=cutKeys1
	Last_keys=keys[:]
	all_keys=[]
	while keys!=[]:
		C=getC(D,keys)
		cutKeys=getCutKeys(keys,C,minSup,len(D))
		if [] in cutKeys:
			cutKeys.remove([])
		if len(cutKeys)==0:
			break
		for k in cutKeys:
			all_keys.append(k)
		keys=apriori_gen(cutKeys,Last_keys)
		Last_keys=keys[:]
	return all_keys



D = [['A','B','C','D'],['B','C','E'],['A','B','C','E'],['B','D','E'],['A','B','C','D']]
F=Apriori(D,0.5)
print '\nfrequent itemset:\n',F
