import os
import re

def update_links(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Replace "index.html" with "dashboard.html" EXCEPT in index.html itself 
            # (or be careful with what index.html should link to)
            # Actually, most pages link to Dashboard. 
            # If a page links to Home/Dashboard, it should now go to dashboard.html.
            
            # Use regex to find href="index.html" or href='./index.html' etc.
            new_content = re.sub(r'href=["\']index\.html["\']', 'href="dashboard.html"', content)
            
            if content != new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated links in {filename}")

if __name__ == "__main__":
    update_links("e:/MUDRA")
