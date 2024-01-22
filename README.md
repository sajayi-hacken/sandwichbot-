# README for Sandwich Bot Tracker

Overview
The "5m477 Bot Sandwich Tracker" is a Python script designed to identify potential sandwich attack transactions on the Ethereum blockchain. It utilizes the Web3 library to interact with the Ethereum network, pyfiglet for visual headers, and colorama for colored console output. The script analyzes transactions in the latest block and flags transactions that could be part of a sandwich attack, a type of manipulation where a bot places transactions before and after a target transaction to profit from the price slippage.


Features
Block Analysis: Connects to the Ethereum blockchain and retrieves the latest block's transactions.

Transaction Tracking: Identifies transactions interacting with specified Decentralized Exchange (DEX) contracts.

Bot Detection: Detects potential bots by finding pairs of addresses with exactly two transactions in a single block.

Sandwich Attack Identification: Analyzes possible sandwich attacks by checking for variance in gas prices to identify likely attack transactions.





Requirements
Python 3.x

Web3.py library (pip install web3)

pyfiglet library (pip install pyfiglet)

colorama library (pip install colorama)




How to Use
Setup: Ensure all required libraries are installed.

Run the Script: Execute the script in a Python environment.

Data Analysis: The script will automatically:

Connect to the Ethereum blockchain.

Retrieve and analyze the latest block's transactions.

Identify potential sandwich attack transactions.




Functions
grabTransactions(): Pulls down all transactions in the latest block and populates dictionaries with related data.

findBots(): Identifies potential bots based on transaction patterns.

findSandwich(possibleSandwich): Filters and identifies likely sandwich attack transactions.






Customization

Known DEX Contracts: Modify the known_dex_contracts list to include addresses of DEX contracts you want to monitor.

Connection Details: Change the Web3 HTTPProvider URL to connect to a different Ethereum node or network.





Note
This script is for educational and analytical purposes. It does not execute any transactions and relies on public blockchain data. Accuracy of bot and sandwich attack identification may vary.
