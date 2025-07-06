import os
import time

# ✅ Known Devicon tools and languages
DEVICON_SUPPORTED = {
    "python": "python/python-original.svg",
    "c": "c/c-original.svg",
    "cpp": "cplusplus/cplusplus-original.svg",
    "java": "java/java-original.svg",
    "html": "html5/html5-plain.svg",
    "css": "css3/css3-plain.svg",
    "javascript": "javascript/javascript-plain.svg",
    "typescript": "typescript/typescript-original.svg",
    "php": "php/php-original.svg",
    "mysql": "mysql/mysql-original-wordmark.svg",
    "git": "git/git-original.svg",
    "github": "github/github-original.svg",
    "bash": "bash/bash-original.svg",
    "docker": "docker/docker-original.svg",
    "linux": "linux/linux-original.svg",
    "nodejs": "nodejs/nodejs-original.svg",
    "react": "react/react-original.svg",
    "vue": "vuejs/vuejs-original.svg",
    "flutter": "flutter/flutter-original.svg",
    "go": "go/go-original.svg",
    "ruby": "ruby/ruby-original.svg",
    "rust": "rust/rust-plain.svg"
}

# 🌈 Intro menu
def main_menu():
    print("\n🎉 Welcome to the GitHub Profile README Generator 🎉")
    print("-----------------------------------------------------")
    print("1. 🛠 Start Generator")
    print("2. ❓ Help (SVG typing banner)")
    print("3. 🚪 Exit\n")

    choice = input("Pick an option (1-3): ")
    if choice == "1":
        data = user_prompt()
        content = readme_generator(data)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(content.strip())
        print("\n✅ README.md created successfully!")
    elif choice == "2":
        show_help()
        main_menu()
    elif choice == "3":
        print("👋 Goodbye!")
        exit()
    else:
        print("❌ Invalid choice. Try again.")
        main_menu()

# 🆘 Help section for SVG typing banner
def show_help():
    print("\n📝 The 'SVG Typing Banner' shows animated typing text at the top of your README.")
    print("Example input: Welcome!👋;I'm Kieran!;I build cool tools 💻")
    print("Each ';' separates a new line of animated text.")
    print("It looks like this in your README:\n")
    print("https://readme-typing-svg.herokuapp.com\n")

# 🧠 Ask user questions and build their profile
def user_prompt():
    print("\n👤 Let's build your GitHub Profile!\n")

    name = input("🔤 What is your full name?\n> ")
    username = input("🔗 GitHub username:\n> ")
    color = input("🎨 Favourite HEX colour (no #, e.g. 067e00):\n> ").lstrip('#')
    svg_lines = input("⌨️ Typing SVG lines (e.g. Welcome!;I'm Kieran!):\n> ")
    title = input("💼 What do you call yourself? (e.g. Developer, Student)\n> ")
    skills = input("🧰 List 2–4 skills (e.g. Creator • Thinker • Debugger):\n> ")

    # 🔒 Require a decently long about description
    while True:
        print("\n🗣 Write a short paragraph about yourself (min 30 chars):")
        about = input("> ").strip()
        if len(about) < 30:
            print("⚠️ Too short! Give a bit more info.")
        else:
            break

    while True:
        print("\n📖 Describe your coding journey (min 30 chars):")
        journey = input("> ").strip()
        if len(journey) < 30:
            print("⚠️ Too short! Tell more of your story.")
        else:
            break

    tools = []
    while True:
        print("\n🛠 Languages & Tools (comma-separated, e.g. Python, C, Git):")
        raw = input("> ").lower().split(',')
        unknowns = [t.strip() for t in raw if t.strip() not in DEVICON_SUPPORTED]
        if unknowns:
            print(f"❌ These are not recognized: {', '.join(unknowns)}")
            print("Try again using tools from the supported list.\n")
            print(", ".join(DEVICON_SUPPORTED.keys()))
        else:
            tools = [t.strip() for t in raw if t.strip()]
            break

    return {
        "name": name,
        "username": username,
        "color": color,
        "svg_lines": svg_lines,
        "job_title": title,
        "skills": skills,
        "about": about,
        "journey": journey,
        "tools": tools
    }

# 🧱 Converts tool name to Devicon image tag
def tool_icon(tool):
    base = "https://github.com/devicons/devicon/blob/master/icons/"
    icon_path = DEVICON_SUPPORTED.get(tool)
    if icon_path:
        return f'<img align="left" alt="{tool}" width="30px" src="{base}{icon_path}" />'
    return f"`{tool}`"  # fallback

# 🧾 Generates the final README content
def readme_generator(data):
    lines = f"""
<a align="center" href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Righteous&size=50&pause=1000&color={data['color']}&center=true&vCenter=true&random=false&width=500&height=70&lines={data['svg_lines'].replace(' ', '+')}" alt="Typing SVG" />
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
        lines += tool_icon(tool) + "\n"

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

# 🚀 Entry point
if __name__ == "__main__":
    main_menu()
