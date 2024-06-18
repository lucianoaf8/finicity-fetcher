from utils.finicity_client import FinicityClient

def fetch_liabilities():
    client = FinicityClient()
    liabilities = client.get("/aggregation/v1/customers/{customerId}/accounts/liabilities")  # Replace {customerId} with actual customer ID
    return liabilities

if __name__ == "__main__":
    liabilities_data = fetch_liabilities()
    print(liabilities_data)
