from utils.finicity_client import FinicityClient

def fetch_transactions():
    client = FinicityClient()
    transactions = client.get("/aggregation/v1/customers/{customerId}/transactions")  # Replace {customerId} with actual customer ID
    return transactions

if __name__ == "__main__":
    transactions_data = fetch_transactions()
    print(transactions_data)
