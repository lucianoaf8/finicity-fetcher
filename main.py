from fetchers.finicity_accounts import fetch_accounts
from fetchers.finicity_balances import fetch_balances
from fetchers.finicity_transactions import fetch_transactions
from fetchers.finicity_liabilities import fetch_liabilities
from fetchers.finicity_assets import fetch_assets

def main():
    accounts = fetch_accounts()
    print("Accounts:", accounts)

    balances = fetch_balances()
    print("Balances:", balances)

    transactions = fetch_transactions()
    print("Transactions:", transactions)

    liabilities = fetch_liabilities()
    print("Liabilities:", liabilities)

    assets = fetch_assets()
    print("Assets:", assets)

if __name__ == "__main__":
    main()
