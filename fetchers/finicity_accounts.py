from utils.finicity_client import FinicityClient

def fetch_accounts():
    client = FinicityClient()
    accounts = client.get("/aggregation/v1/customers/{customerId}/accounts")  # Replace {customerId} with actual customer ID
    return accounts

if __name__ == "__main__":
    accounts_data = fetch_accounts()
    print(accounts_data)
