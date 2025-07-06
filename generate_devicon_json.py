import requests
import json

DEVICON_API_URL = "https://raw.githubusercontent.com/devicons/devicon/master/devicon.json"

def create_json():
    response = requests.get(DEVICON_API_URL)
    if response.status_code != 200:
        print("❌ Could not fetch Devicon data.")
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
