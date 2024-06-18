from utils.finicity_client import FinicityClient

def fetch_balances():
    client = FinicityClient()
    balances = client.get("/aggregation/v1/customers/{customerId}/accounts/balances")  # Replace {customerId} with actual customer ID
    return balances

if __name__ == "__main__":
    balances_data = fetch_balances()
    print(balances_data)
