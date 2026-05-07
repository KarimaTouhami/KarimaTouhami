import datetime
import random

status_messages = [
    "Compiling thoughts...",
    "Refactoring reality.",
    "Optimizing the workflow.",
    "Debugging the day.",
    "Pointers point to success."
]

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = random.choice(status_messages)
content_to_insert = f"_Last Pulse: {now} | Status: {message}_"

with open("README.md", "r") as f:
    readme = f.read()

# Locate the markers and swap the content
start_marker = "<!-- START_UPDATE -->"
end_marker = "<!-- END_UPDATE -->"

start_index = readme.find(start_marker) + len(start_marker)
end_index = readme.find(end_marker)

new_readme = readme[:start_index] + "\n" + content_to_insert + "\n" + readme[end_index:]

with open("README.md", "w") as f:
    f.write(new_readme)
