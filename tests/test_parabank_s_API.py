import pytest
import json
import logging

@pytest.mark.order(2)
def test_find_transactions_by_amount_API(api_client, config):
    try:    
        # Load account_id and JSESSIONID from previous UI test
        with open("utils/account_info.json", "r") as f:
            data = json.load(f)
        account_id = data["account_id"]

        with open("utils/user_state.json", "r") as j:
            state = json.load(j)
        cookies = state.get("cookies", [])
        jsessionid = next((c["value"] for c in cookies if c["name"] == "JSESSIONID"), None)

        # 1. Search transactions by amount
        amount = 5
        url = f"{config["API"]["base_url"]}/accounts/{account_id}/transactions/amount/{amount}?timeout=30000"
        headers = {"Cookie": f"JSESSIONID={jsessionid}"}
        response = api_client.get(url, headers=headers)
        response.raise_for_status()
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        # 2. Validate JSON response
        response_json = response.json()
        required_keys = {"id", "accountId", "type", "date", "amount", "description"}
        for fields in response_json:
            assert required_keys.issubset(fields.keys()), f"Missing keys in transaction: {fields}"
        assert any(txn["amount"] == 5 for txn in response_json), "No transaction with amount 5 found"
    except Exception as e:
        logging.error(f"Test failed due to error: {e}")