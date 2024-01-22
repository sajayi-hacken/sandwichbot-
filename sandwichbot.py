from web3 import Web3
from colorama import Fore
import pyfiglet

# Display a header using pyfiglet for visual appeal
result = pyfiglet.figlet_format("5m477 Bot Sandwich Tracker", font="chunky")
print(f'{Fore.GREEN}Searching for Sandwich: \n {Fore.RED}{result}') 

# Setup Web3 connection to the Ethereum blockchain
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/cef58d75a70a4ee4894041a4fd531efe'))
block = web3.eth.get_block('latest')

# Initialize dictionaries to store transaction data
toFromPairs = {}  # Stores pairs of to/from addresses
transactionCount = {}  # Counts transactions for each 'to' address
txLookup = {}  # Lookup table for transactions
possibleSandwich = {}  # Stores potential sandwich attack transactions

# List of known DEX contract addresses (to be filled with actual addresses)
known_dex_contracts = ['0xdAC17F958D2ee523a2206206994597C13D831ec7, 0x152649eA73beAb28c5b49B26eb48f7EAD6d4c898']

def grabTransactions():
    """ Pulls down all transactions in the latest block and populates dictionaries
        with counts related to To/From Address Pairs and associated hashes. """
    if block and block.transactions: 
        for transaction in block.transactions: 
            tx_hash = transaction.hex()  # Convert txhashes from hexBytes format
            tx = web3.eth.get_transaction(tx_hash)

            # Filter transactions that interact with DEX contracts
            if tx.to in known_dex_contracts and tx.to is not None:
                if tx.to in toFromPairs:
                    if toFromPairs[tx.to] == tx["from"]:
                        transactionCount[tx.to] += 1 
                        txLookup[tx_hash] = [tx.to, tx["from"], tx.gasPrice]
                elif tx.to not in toFromPairs:
                    transactionCount[tx.to] = 1
                    toFromPairs[tx.to] = tx["from"]
                    txLookup[tx_hash] = [tx.to, tx["from"], tx.gasPrice]

def findBots():
    """ Identifies potential bots by finding to/from pairs with exactly 2 transactions
        in a single block for further review. """
    for transactionHash, pair in txLookup.items():    
        if transactionCount[pair[0]] == 2:
            possibleSandwich[transactionHash] = [pair[0], pair[2]]   

def findSandwich(possibleSandwich): 
    """ Analyzes the possible sandwich attacks by checking for variance in gas prices
        to filter out transactions that are likely not part of an attack. """
    allBots = {}
    duplicateBots = {}
    sandwiches = []

    # Check for duplicate gas values as these cannot be sandwich attacks
    for sHash, sGas in possibleSandwich.items(): 
        if sGas[1] in allBots.values():
            duplicateBots[sHash] = sGas[1]
        elif sGas[1] not in allBots.values():    
            allBots[sHash] = sGas[1]
            
    print(f'{len(allBots)} bot transactions parsed with 2 like pairs')
    print('---------------------------------------------------------')
    for bot in allBots.keys():
        print(bot)
    print('---------------------------------------------------------')

    # Filter out transactions that are not part of duplicateBots
    for sHash, bot in allBots.items():
        if duplicateBots:
            if bot not in duplicateBots.values():
               sandwiches.append(sHash) 

    return sandwiches           

if __name__ == "__main__":
    # Main execution flow
    grabTransactions()  # Retrieve and analyze transactions
    findBots()  # Identify potential bots

    # Process potential sandwich attacks and print results
    if possibleSandwich:
        sandwiches = findSandwich(possibleSandwich)
        for sandwich in sandwiches:
            print(f'{Fore.GREEN}Delicious Sandwich Found: \n {Fore.YELLOW}{sandwich}')        
