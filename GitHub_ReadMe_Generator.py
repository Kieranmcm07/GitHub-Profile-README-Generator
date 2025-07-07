import os, sys, json, subprocess, requests
from datetime import datetime

# 📦 Auto-install profanity filter
try:
    from better_profanity import profanity
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "better_profanity"])
    from better_profanity import profanity

# 🔃 Load Devicon icons
with open("devicon_tools.json", "r", encoding="utf-8") as f:
    DEVICON = json.load(f)

# 🧠 Load or create settings
SETTINGS_FILE = "settings.json"
DEFAULT_SETTINGS = {
    "use_emojis": True,
    "stats_theme": "dark",
    "show_stats": True,
    "show_streaks": True,
    "show_languages": True,
    "add_gif_banner": False,
    "gif_url": "",
    "show_quote": True,
    "quote": "",
    "visitor_counter": False,
    "show_badges": True,
    "center_content": True,
    "show_journey": True
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)

SETTINGS = load_settings()
profanity.load_censor_words()

# 🚦 Utility
def pause():
    input("\n⏸️ Press Enter to continue...")

def is_clean(*args):
    return not any(profanity.contains_profanity(str(val)) for val in args)

def github_user_exists(username):
    return requests.get(f"https://api.github.com/users/{username}").status_code == 200

def get_tool_icon(tool):
    base = "https://github.com/devicons/devicon/blob/master/icons/"
    return f'<img align="left" alt="{tool}" width="30px" src="{base}{DEVICON[tool]}" />' if tool in DEVICON else f"`{tool}`"

# 🎨 Generate final README using all settings
def generate_readme(data):
    center_start = "<div align='center'>" if SETTINGS["center_content"] else ""
    center_end = "</div>" if SETTINGS["center_content"] else ""

    svg = f"Welcome!👋;Hi I'm {data['name']}! 💻"

    content = f"""
{center_start}
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Righteous&size=50&pause=1000&color={data['color']}&center=true&vCenter=true&random=false&width=500&height=70&lines={svg.replace(' ', '+')}" alt="Typing SVG" />
</a>
{center_end}

### Hi there {'👋' if SETTINGS['use_emojis'] else ''}, I'm {data['name']}

---

**`{data['job_title']} ({data['skills']})`**

{data['about']}

"""

    if SETTINGS["quote"]:
        content += f"> **_{SETTINGS['quote']}_**\n\n"

    if SETTINGS["add_gif_banner"] and SETTINGS["gif_url"]:
        content += f'<img src="{SETTINGS["gif_url"]}" width="100%" />\n\n'

    content += "---\n\n### 🧰 Languages & Tools\n\n"
    for tool in data['tools']:
        content += get_tool_icon(tool) + "\n"
    content += "\n<br />\n\n---\n\n"

    if SETTINGS["show_stats"]:
        content += f"### 📊 GitHub Stats\n\n"
        content += f"![{data['name']}'s GitHub stats](https://github-readme-stats.vercel.app/api?username={data['username']}&show_icons=true&theme={SETTINGS['stats_theme']})\n\n"

    if SETTINGS["show_streaks"]:
        content += f"![GitHub Streak](https://streak-stats.demolab.com/?user={data['username']}&theme={SETTINGS['stats_theme']})\n\n"

    if SETTINGS["show_languages"]:
        content += f"![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username={data['username']}&layout=compact&theme={SETTINGS['stats_theme']})\n\n"

    if SETTINGS["visitor_counter"]:
        content += f"![visitors](https://komarev.com/ghpvc/?username={data['username']}&label=Profile+views)\n\n"

    if SETTINGS["show_badges"]:
        content += "### 🏷️ Badges\n\n"
        content += "![Python](https://img.shields.io/badge/-Python-blue?style=flat&logo=python)\n"
        content += "![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat&logo=github)\n"
        content += "![Open Source](https://img.shields.io/badge/-Open%20Source-important?style=flat&logo=open-source-initiative)\n\n"

    if SETTINGS["show_journey"]:
        content += "---\n\n<details>\n <summary><h3>👨‍💻 My Coding Journey</h3></summary>\n\n"
        content += data['journey'] + "\n\n</details>\n"

    content += "\n---\n\n### 🙌 Credits\n\n"
    content += "Built with ❤️ by Kieran McMonagle\n"
    return content

# ⚙️ Settings Menu
def show_settings_menu():
    while True:
        clear()
        print("🔧 SETTINGS MENU")
        print("----------------------------")
        for i, (key, val) in enumerate(SETTINGS.items(), 1):
            print(f"{i}. {key.replace('_', ' ').title()}: {val}")
        print(f"{len(SETTINGS)+1}. Save and return")

        choice = input("\nChange setting number or press Enter to go back:\n> ")
        if not choice or choice == str(len(SETTINGS)+1):
            save_settings(SETTINGS)
            break

        try:
            idx = int(choice) - 1
            key = list(SETTINGS.keys())[idx]
            current = SETTINGS[key]

            if isinstance(current, bool):
                SETTINGS[key] = not current
            else:
                SETTINGS[key] = input(f"Enter new value for '{key}':\n> ").strip()
        except:
            print("❌ Invalid input.")
        pause()

# 📋 Input form
def collect_input():
    print("\n👤 Let's set up your GitHub Profile README!\n")
    while True:
        name = input("Your name:\n> ").strip()
        if is_clean(name): break
        print("❌ Please avoid inappropriate words.")

    while True:
        username = input("\nGitHub username:\n> ").strip()
        if github_user_exists(username) and is_clean(username):
            break
        print("❌ Invalid or offensive username.")

    color = input("\nHEX colour (no #, e.g. 067e00):\n> ").lstrip('#')

    while True:
        title = input("\nYour title (e.g. Developer):\n> ")
        skills = input("Top 3 skills (e.g. Creative • Debugger):\n> ")
        if is_clean(title, skills): break

    while True:
        about = input("\nAbout you (min 30 chars):\n> ")
        if len(about) >= 30 and is_clean(about): break

    while True:
        journey = input("\nDescribe your coding journey:\n> ")
        if len(journey) >= 30 and is_clean(journey): break

    while True:
        tools = input("\nTools/languages (comma-separated):\n> ").lower().split(",")
        tools = [t.strip() for t in tools if t.strip()]
        if all(t in DEVICON for t in tools): break
        print("❌ One or more tools not supported by Devicon.")
    return {
        "name": name,
        "username": username,
        "color": color,
        "job_title": title,
        "skills": skills,
        "about": about,
        "journey": journey,
        "tools": tools
    }

def show_help():
    print("\n🆘 How to Use")
    print("- Choose Start to enter your info.")
    print("- Visit Settings to toggle visual features (GIFs, streaks, quote).")
    print("- Everything is saved in 'settings.json'.")
    print("- README.md is created in this folder.")
    pause()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 🧭 Menu
def main_menu():
    while True:
        clear()
        print("🌟 GitHub Profile README Generator 🌟")
        print("====================================")
        print("1. 🚀 Start Generator")
        print("2. ⚙️  Settings")
        print("3. ❓ Help")
        print("4. 🙌 Credits")
        print("5. 🚪 Exit")

        choice = input("\nChoose an option:\n> ")
        if choice == "1":
            data = collect_input()
            result = generate_readme(data)
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(result.strip())
            print(f"\n✅ README.md created at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            pause()
        elif choice == "2":
            show_settings_menu()
        elif choice == "3":
            show_help()
        elif choice == "4":
            print("🙌 Created by Kieran McMonagle with love.")
            pause()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid input.")
            pause()

if __name__ == "__main__":
    main_menu()
