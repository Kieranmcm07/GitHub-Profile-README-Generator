import requests
import json

DEVICON_API_URL = "https://raw.githubusercontent.com/devicons/devicon/master/devicon.json"

def create_json():
    try:
        response = requests.get(DEVICON_API_URL)
        # 🔥 FIX THIS LINE: Remove 'response.status_code != 200' from except clause
        if response.status_code != 200:
            print("❌ Could not fetch Devicon data.")
            return
    except Exception as e:  # Catch any network errors
        print(f"❌ Connection error: {str(e)}")
        return

    data = response.json()
    tools = {}

    for item in data:
        name = item['name'].lower()
        tools[name] = f"{name}/{name}-original.svg"

    with open("devicon_tools.json", "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2)

    print(f"✅ Saved {len(tools)} tools to devicon_tools.json")

if __name__ == "__main__":
    create_json()