import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FinicityClient:
    def __init__(self):
        self.base_url = "https://api.finicity.com"
        self.partner_id = os.getenv("FINICITY_PARTNER_ID")
        self.partner_secret = os.getenv("FINICITY_PARTNER_SECRET")
        self.token = self.get_partner_access_token()

    def get_partner_access_token(self):
        url = f"{self.base_url}/aggregation/v1/partners/authentication"
        headers = {
            "Finicity-App-Key": self.partner_id,
            "Content-Type": "application/json"
        }
        body = {
            "partnerId": self.partner_id,
            "partnerSecret": self.partner_secret
        }
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()
        return response.json()['token']

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Finicity-App-Key": self.partner_id,
            "Finicity-App-Token": self.token
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
