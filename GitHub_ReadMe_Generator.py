import os
import subprocess
import sys
import time
import json
import requests
from datetime import datetime

# 📦 Auto-install better_profanity if needed
try:
    from better_profanity import profanity
except ImportError:
    print("📦 Installing 'better_profanity' library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "better_profanity"])
    from better_profanity import profanity

# 🔃 Load Devicon tool list
with open("devicon_tools.json", "r", encoding="utf-8") as f:
    DEVICON = json.load(f)

# 🧼 Setup profanity filter
profanity.load_censor_words()

def is_clean(*args):
    return not any(profanity.contains_profanity(val) for val in args)

def github_user_exists(username):
    return requests.get(f"https://api.github.com/users/{username}").status_code == 200

def get_tool_icon(tool):
    base = "https://github.com/devicons/devicon/blob/master/icons/"
    return (f'<img align="left" alt="{tool}" width="30px" src="{base}{DEVICON[tool]}" />'
            if tool in DEVICON else f"`{tool}`")

def generate_readme(data):
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

### 🙌 Credits

Made with ❤️ by Kieran McMonagle using Python.  
Powered by Devicon, GitHub Stats Card, Typing SVG & better_profanity.

---
"""
    return lines

def collect_input():
    print("\n👤 Let's set up your GitHub Profile README!\n")
    while True:
        name = input("🔤 Your name:\n> ").strip()
        if is_clean(name): break
        print("❌ Please avoid inappropriate words.")

    while True:
        username = input("\n🔗 GitHub username:\n> ").strip()
        if not github_user_exists(username):
            print("❌ GitHub user not found. Try again.")
        elif not is_clean(username):
            print("❌ Inappropriate words detected.")
        else:
            break

    color = input("\n🎨 HEX colour (e.g. 067e00, no '#'):\n> ").lstrip('#')
    while True:
        job_title = input("\n💼 Your role (e.g. Developer, Student):\n> ").strip()
        skills = input("\n🔧 Skills (e.g. Creator • Learner • Debugger):\n> ").strip()
        if is_clean(job_title, skills): break
        print("❌ Please avoid inappropriate language.")

    while True:
        print("\n📜 About you (min 30 chars):")
        about = input("> ").strip()
        if len(about) < 30:
            print("⚠️ Too short.")
        elif not is_clean(about):
            print("❌ Please reword without swearing.")
        else:
            break

    while True:
        print("\n📖 How did you get into coding? (min 30 chars):")
        journey = input("> ").strip()
        if len(journey) < 30:
            print("⚠️ Please write more.")
        elif not is_clean(journey):
            print("❌ Please reword that.")
        else:
            break

    while True:
        print("\n🧰 Languages & Tools (comma-separated):")
        raw = [t.strip() for t in input("> ").lower().split(",")]
        if not is_clean(*raw):
            print("❌ Profanity detected. Please re-enter.")
            continue
        invalid = [t for t in raw if t not in DEVICON]
        if invalid:
            print(f"❌ Unsupported tools: {', '.join(invalid)}")
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
    print("\n🆘 How to Use This Program")
    print("-----------------------------")
    print("1. Run the script and select 'Start Generator'.")
    print("2. Answer prompts (they're checked for profanity).")
    print("3. Your README.md will be generated here.")
    print("4. Tip: HEX colour sets your banner colour.")
    print("5. Need icons? Use names from Devicon (e.g. python, rust).\n")

def show_settings():
    print("\n⚙️ Settings (future features)")
    print("-------------------------------")
    print("- Theme toggle")
    print("- Emoji on/off")
    print("- Load/save profiles\n")

def show_credits():
    print("\n🙌 Credits")
    print("-----------")
    print("Created by Kieran McMonagle")
    print("Uses: Devicon, Typing SVG, GitHub Stats, better_profanity\n")

def main_menu():
    while True:
        print("\n✨ GitHub Profile README Generator ✨")
        print("===================================")
        print("1. 🚀 Start Generator")
        print("2. ❓ Help")
        print("3. ⚙️ Settings")
        print("4. 🙌 Credits")
        print("5. 🚪 Exit")
        choice = input("\nPick an option (1–5): ")
        if choice == "1":
            data = collect_input()
            readme = generate_readme(data)
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(readme.strip())
            print(f"\n✅ README.md created at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        elif choice == "2":
            show_help()
        elif choice == "3":
            show_settings()
        elif choice == "4":
            show_credits()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Choose 1–5.\n")

if __name__ == "__main__":
    main_menu()
