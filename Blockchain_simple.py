# Simple BlockChain project, with the help of an online guide.
# Todo: find the guide and reference it, since I used it heavily for guidance.


# basically --> implement a database that is distributed across many computers, with a set of rules for verifying new additions to the database.


# to start with, just make a distributed database for 2 people.



import hashlib
import json
import sys
import random


# first, need wrap out hashing algorithm with a helper function

def hashMe(msg = ''):
	if type(msg) != str:
		msg = json.dumps(msg, sort_keys = True)

	return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()


random.seed(0)


def makeTransaction(maxValue=10):
	# will generate random transcations of size between 0 and maxValue

	sign = int(random.getrandbits(1))*2 - 1
	# randomly generates an integer with 1 bit. (so either 1 or 0)
	# then multiple by 2 and subtract 1, to generate either -1 or +1.


	amount = random.randint(1, maxValue)

	APays = sign*amount
	BPays = (-1)*APays
	# 2 people transaction, person A and person B



	return {u'A':APays, u'B':BPays}
	# where {} is a SET. 
	# and the u just before the string A - e.g. u'A' - means that a UNICODE string is created.


# Now, make a crap-tonne of transactions.

txnBuffer = []
for i in range(0,75):
	txnBuffer.append(makeTransaction())


#txnBuffer = [makeTransaction() for i in range(0,5)]
# also, just use list comprehensions
# txnBuffer = transaction buffer


# Now, need to make actual Blocks.
# For this, need to define a set of simple rules.

# Rule 1 - sum of transaction between A, B must  = 0
# Rule 2 - A,B accounts must have money in them ($>0)

# Transaction should only pass if Rule 1,2 are both valid.

###################################
#state = {u'A':5, u'B':5}

def updateState(txn, state):
	# A function to actually CARRY OUT THE TRANSACTIONS.
	# state = state of A,B accounts

	# if txn is VALID, then you implement updateState.

	state = state.copy()


	for key in txn:
		if key in state.keys():
			state[key] += txn[key]
			# add to state, if key is already present

		else:
			state[key] = txn[key]
			# craete state, if key was not present




def isValidTxn(txn, state):
	# the function to see if the txn is actually valid.
    if sum(txn.values()) is not 0:
        return False

    for i in txn.keys():
        if i in state.keys():
            acctBalance = state[i]
        else:
            acctBalance = 0

        if (acctBalance + txn[i]) < 0:
            return False
        else:
            return True
    




#print(isValidTxn({u'A': -3, u'B': 3},state))
# this will come out as True.
# for A: 5 - 3 > 0. All good.
# for B: 5 + 3 > 0. All good.
# Both Rule 1 and Rule 2 are satisfied.

#print(isValidTxn({u'A': -1, u'B': 3},state))
# False, because the transaction doesnt balance to 0. Rule 1 broken.

#print(isValidTxn({u'A': -7, u'B': 7},state))
# False, because A doesnt have £7 to take out. Rule 2 broken.


# Now, need to implement BLOCKs.
# Each block has:
# 	- a batch of txns
#	- a reference to the HASH of the previous block.
# 	- and a hash of its own contents, and the header.


# 'genesis block' = first block of the chain. This doesnt have a previous block, so it will not reference the HASH of any other blocks.



state = {u'A':50, u'B':50} #set the initial state
#ok nope, have to set it as something different to the function input.
# so use state12 instead.
state12 = {u'A':10, u'B':10}


genesisBlockTxns = [state12]
genesisBlockContents = {u'blockNumber':0,
						u'parentHash':None,
						u'txnCount':1, 
						u'txns':genesisBlockTxns }


genesisHash = hashMe( genesisBlockContents ) # dunno why spaces (_aaa_)
genesisBlock = {u'hash':genesisHash, u'contents':genesisBlockContents}
genesisBlockStr = json.dumps(genesisBlock, sort_keys = True)


# this is our first block. Everything else in the chain will link from here onwards.

# our chain will start off with just the first block. just a list.

chain = [genesisBlock]

"""
for each block, we need to:
	- collect a set of txns
	- create a header for this
	- hash it
	- add this to chain

"""

def makeBlock(txns, chain):
	# can take a bunch of txns, process them into a block, then add them to the end of the chain
	parentBlock = chain[-1] #last element within the chain
	parentHash = parentBlock[u'hash'] #look into this last element, to gets its hash
	blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
	txnCount = len(txns)

	blockContents = {u'blockNumber':blockNumber, 
					 u'parentHash':parentHash,
					 u'txnCount':len(txns),
					 u'txns':txns }

	blockHash = hashMe( blockContents ) # again, not sure why spaces are there.

	block = {u'hash':blockHash, u'contents':blockContents}

	return block



blockSizeLimit = 5 #numberof txns allowed per block. Arbitrary, can choose anything.

while len(txnBuffer) > 0:
#for i in range(0,4):
	bufferStartSize = len(txnBuffer)

	txnList = []

	while (len(txnBuffer) > 0) & (len(txnList) < blockSizeLimit):
		newTxn = txnBuffer.pop()
		validTxn = isValidTxn(newTxn, state12) #if txn is invalid, this will return False.

		if validTxn: # if returns True...
			txnList.append(newTxn)
			state = updateState(newTxn, state12)

		else:
			print('Transaction has been ignored')
			#sys.stdout.flush()
			continue 

	myBlock = makeBlock(txnList, chain)
	#ok, so makeBlock just makes a block, but doesnt really attach it to any chain.
	chain.append(myBlock)
	# now, we attach the created block to our blockchain :)
	# NOTE!: This is an infinite while loop, that lasts as long as the txnBuffer has stuff in it.



# the functions dont recognise the dictionary 'state'
# instead, you have to write state12.
# i think its because the input to the function cant be the same name as what it is referred to.


print(chain[0])
print("*"*15)
print(chain[1])
print("*"*15)
print(chain[2])
print("*"*15)


#seems that the transaction validity checker isnt working properly. Invalid transactions still pass through (I think...)
# need to fix/check this. or maybe im being dumb...not sure yet, will find out soon.

