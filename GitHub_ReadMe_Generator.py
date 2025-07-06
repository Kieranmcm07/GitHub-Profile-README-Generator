import os

def user_prompt():
    print("=== GitHub Profile README Generator ===\n")
    print("This script will generate a beautiful README.md file for your GitHub profile.\n")

    real_name = input("What is your name?\n> ")
    github_username = input("GitHub username?\n> ")
    colour_scheme = input("Favourite colour (HEX only, e.g. 067e00)?\n> ").lstrip('#')

    svg_lines = input("Typing SVG lines (separate with ; like 'Welcome!👋;I'm Kieran!')\n> ")

    job_title = input("What do you call yourself? (e.g. Student, Developer)\n> ")
    skills = input("List 2-4 skills/traits (e.g. Creative • Logical • Learner)\n> ")

    # Minimum character check for about
    while True:
        print("\nWrite a paragraph about yourself (minimum 30 characters):")
        about = input("> ").strip()
        if len(about) < 30:
            print("⚠️ Too short. Please add more detail.")
        else:
            break

    while True:
        print("\nDescribe your coding journey (minimum 30 characters):")
        journey = input("> ").strip()
        if len(journey) < 30:
            print("⚠️ Too short. Add more about how you got into coding.")
        else:
            break

    print("\nEnter the languages & tools you want to show (comma separated):")
    tools = input("> ").lower().split(',')

    return {
        "name": real_name,
        "username": github_username,
        "color": colour_scheme,
        "svg_lines": svg_lines,
        "job_title": job_title,
        "skills": skills,
        "about": about,
        "journey": journey,
        "tools": [t.strip() for t in tools if t.strip()]
    }

def tool_icons(tool):
    known_icons = {
        "python": "python/python-original.svg",
        "c": "c/c-original.svg",
        "html": "html5/html5-plain.svg",
        "css": "css3/css3-plain.svg",
        "javascript": "javascript/javascript-plain.svg",
        "php": "php/php-original.svg",
        "mysql": "mysql/mysql-original-wordmark.svg",
        "git": "git/git-original.svg",
        "github": "github/github-original.svg"
    }
    base_url = "https://github.com/devicons/devicon/blob/master/icons/"
    if tool in known_icons:
        return f'<img align="left" alt="{tool.title()}" width="30px" src="{base_url}{known_icons[tool]}" />'
    else:
        return f"`{tool}`"  # fallback for unknown tools

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
        lines += tool_icons(tool) + "\n"

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

def main():
    data = user_prompt()
    readme_content = readme_generator(data)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content.strip())

    print("\n✅ README.md has been created successfully!\n")

if __name__ == "__main__":
    main()
