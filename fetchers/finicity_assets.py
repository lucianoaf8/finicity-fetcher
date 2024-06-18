from utils.finicity_client import FinicityClient

def fetch_assets():
    client = FinicityClient()
    assets = client.get("/aggregation/v1/customers/{customerId}/accounts/assets")  # Replace {customerId} with actual customer ID
    return assets

if __name__ == "__main__":
    assets_data = fetch_assets()
    print(assets_data)
