@echo off
python -m pip install requests better_profanity --quiet
python generate_devicon_json.py
python GitHub_ReadMe_Generator.py
pause