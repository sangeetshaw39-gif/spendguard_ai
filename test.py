from fastapi.testclient import TestClient
from main import app
import traceback

client = TestClient(app)

try:
    response = client.put(
        "/history/20260329_110813_messy_expense_data.csv",
        json={"new_name": "DATA"}
    )
    print("STATUS:", response.status_code)
    print("BODY:", response.json())
except Exception as e:
    print("EXCEPTION OCCURRED:", e)
    traceback.print_exc()

# Also try GET /history
response2 = client.get("/history")
try:
    print(response2.json()[0]["filename"])
except Exception as e:
    pass
