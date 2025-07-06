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
