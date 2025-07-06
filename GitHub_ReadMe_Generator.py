# ReadMe tool for GitHub repositories

# This script generates a README.md file for a GitHub repository.

import os


def user_prompt():
    print("Temp Heading")
    print("\*\*\* GitHub Profile README Generator \*\*\*")
    
    
    print("This script will ask you a series of questions to generate a README.md file for your GitHub profile.\n Pleae answer the questions as accurately as possible.\n")
    
    real_name = input("What is your real name?\n\n > ")
    github_username = input("What is your GitHub username?\n\n > ")
    colour_scheme = input("What is your preferred colour scheme? (e.g. 'blue', 'red', 'green' Please answer in a HEX code format)\n\n > ")
    
    svg_lines = input("Typing SVG lines (separate with ; like 'Welcome!👋;I'm Kieran!')\n\n > ")
    
    job_title = input("What do you call yourself? (e.g., Software Engineer, Web Developer, Student, etc.)\n\n > ")
    skills = input("List 3 skills or qualities (e.g., Developer • Creator • Problem Solver)\n\n >  ")
    
    print("\nWrite a short paragraph about yourself (who you are, what you're into):")
    about = input("(Press Enter when done):\n > ")

    print("\nHow did you get into coding? Describe your journey or origin story:")
    journey = input("(Press Enter when done):\n > ")
    
    print("\nEnter the languages & tools you want to show (separate with commas). Options include:")
    print("Python, C, HTML, CSS, JavaScript, PHP, MySQL, Git, GitHub\n")
    tools = input("Languages & tools: ").lower().split(',')

    return {
        "name": real_name,
        "username": github_username,
        "color": colour_scheme,
        "svg_lines": svg_lines,
        "job_title": job_title,
        "skills": skills,
        "about": about,
        "journey": journey,
        "tools": [t.strip() for t in tools]
    }


def tool_icons(tool):
    icons = {
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
    return f'<img align="left" alt="{tool.title()}" width="30px" src="{base_url}{icons[tool]}" />' if tool in icons else ""


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
        icon = tool_icons(tool)
        if icon:
            lines += icon + "\n"

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

    print("\n✅ README.md has been created in this folder!\n")

if __name__ == "__main__":
    main()