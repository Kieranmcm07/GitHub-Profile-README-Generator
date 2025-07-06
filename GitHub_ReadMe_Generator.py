import os
import time
import json
import requests
from datetime import datetime
from better_profanity import profanity

# 🔃 Load full Devicon list
with open("devicon_tools.json", "r", encoding="utf-8") as f:
    DEVICON = json.load(f)

# 🔍 Profanity filter setup
profanity.load_censor_words()

def is_clean(text):
    """Checks if text is free of profanity."""
    return not profanity.contains_profanity(text)

def github_user_exists(username):
    """Checks if the GitHub profile exists using GitHub API."""
    res = requests.get(f"https://api.github.com/users/{username}")
    return res.status_code == 200

def get_tool_icon(tool):
    """Returns Devicon <img> tag or fallback if not found."""
    base = "https://github.com/devicons/devicon/blob/master/icons/"
    return f'<img align="left" alt="{tool}" width="30px" src="{base}{DEVICON[tool]}" />' if tool in DEVICON else f"`{tool}`"

def generate_readme(data):
    """Creates README markdown content."""
    svg = f"Welcome!👋;Hi I'm {data['name']}! 💻"
    lines = f"""
<a align="center" href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Righteous&size=50&pause=1000&color={data['color']}&center=true&vCenter=true&random=false&width=500&height=70&lines={svg.replace(' ', '+')}" alt="Typing SVG" />
</a>

### Hi there <img src="https://raw.githubusercontent.com/nixin72/nixin72/master/wave.gif" width="30px">, I'm {data['name']}

---

**`{data['job_title']} ({data['skills']})`**

{data['about']}

🧠 Self-taught. 🧩 Solution-driven. 🚀 Future-focused.

---

### 🧰 Languages & Tools
"""
    for tool in data['tools']:
        lines += get_tool_icon(tool) + "\n"

    lines += "\n<br /><br />\n\n---\n\n"

    lines += f"""### 📊 GitHub Stats

![{data['name']}'s GitHub stats](https://github-readme-stats.vercel.app/api?username={data['username']}&show_icons=true&theme=dark)

---

<details>
 <summary><h3>👨‍💻 My Coding Journey</h3></summary>

{data['journey']}

</details>

---
"""
    return lines

def collect_input():
    """Gathers user input and validates fields."""
    print("\n👤 Let's set up your profile...\n")

    name = input("🔤 Your name:\n> ").strip()

    while True:
        username = input("\n🔗 GitHub username:\n> ").strip()
        if github_user_exists(username):
            break
        print("❌ That GitHub profile doesn't exist. Try again.")

    color = input("\n🎨 Favourite HEX colour (e.g. 067e00):\n> ").lstrip('#')
    job_title = input("\n💼 What do you call yourself? (e.g. Developer, Student):\n> ").strip()
    skills = input("\n🧠 List your top 2–4 skills (e.g. Debugger • Learner • Creator):\n> ").strip()

    # About section
    while True:
        print("\n📜 Tell us about yourself (min 30 chars):")
        about = input("> ").strip()
        if len(about) < 30:
            print("⚠️ Too short.")
        elif not is_clean(about):
            print("❌ Inappropriate words detected.")
        else:
            break

    # Coding journey
    while True:
        print("\n📖 Tell us how you got into coding (min 30 chars):")
        journey = input("> ").strip()
        if len(journey) < 30:
            print("⚠️ Too short.")
        elif not is_clean(journey):
            print("❌ Inappropriate words detected.")
        else:
            break

    # Tools & languages
    tools = []
    while True:
        print("\n🧰 List your languages/tools (comma-separated):")
        raw = input("> ").lower().split(",")
        raw = [t.strip() for t in raw if t.strip()]
        invalid = [t for t in raw if t not in DEVICON]
        if invalid:
            print(f"❌ These are not supported by Devicon: {', '.join(invalid)}")
        else:
            tools = raw
            break

    return {
        "name": name,
        "username": username,
        "color": color,
        "job_title": job_title,
        "skills": skills,
        "about": about,
        "journey": journey,
        "tools": tools
    }

def show_help():
    print("\nℹ️ Typing SVG Help")
    print("------------------------")
    print("Typing SVG is the animated text banner at the top of your README.")
    print("It includes:\n - Welcome!👋\n - Hi I'm [Your Name]! 💻\n")

def show_settings():
    print("\n⚙️ Settings (future update placeholder)")
    print("You could add themes, emoji modes, etc. in the future.\n")

def main_menu():
    while True:
        print("\n=== GitHub README Generator ===")
        print("1. Start 🛠️")
        print("2. Help ❓")
        print("3. Settings ⚙️")
        print("4. Exit 🚪")
        choice = input("\nChoose an option: ")

        if choice == "1":
            data = collect_input()
            readme = generate_readme(data)
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(readme.strip())
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n✅ README.md created at {timestamp}\n")
        elif choice == "2":
            show_help()
        elif choice == "3":
            show_settings()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.\n")

if __name__ == "__main__":
    main_menu()
