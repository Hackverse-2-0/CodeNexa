import os
import re

directory = r"c:\Users\SOUMYA RANJAN NAYAK\OneDrive\Desktop\MUDRA"

mapping = {
    'dashboard': 'index.html',
    'lesson': 'learnsignlanguage.html',
    'learn': 'learnsignlanguage.html',
    'practice': 'practice.html',
    'game': 'game1.html',
    'about': 'about.html',
    'profile': 'profile.html',
    'setting': 'settings.html',
    'dictionary': 'ISLdictionary.html',
    'support': 'help&support.html',
    'help': 'help&support.html',
    'history': 'sessionhistory.html',
    'progress': 'monthlyprogress.html',
    'video': 'videototext.html',
    'live': 'liveinterpreter.html',
    'fav': 'favsigns.html',
    'goal': "today'sgoal.html",
    'translate': 'videototext.html',
    'translator': 'videototext.html',
    'leaderboard': 'globalranking.html',
    'home': 'index.html',
    'person': 'profile.html',
}

a_tag_pattern = re.compile(r'(<a\s+[^>]*href=["\'])(#|)(["\'][^>]*>)(.*?)(</a>)', re.IGNORECASE | re.DOTALL)

def get_link_for_text(text):
    text_lower = text.lower()
    for key, val in mapping.items():
        if key in text_lower:
            return val
    return None

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        prefix = match.group(1)
        href_val = match.group(2)
        suffix = match.group(3)
        inner_html = match.group(4)
        closing = match.group(5)
        
        if href_val not in ("#", ""):
            return match.group(0)

        new_href = get_link_for_text(inner_html)
        if new_href:
            return f"{prefix}{new_href}{suffix}{inner_html}{closing}"
        else:
            return match.group(0)

    new_content = a_tag_pattern.sub(replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

updated_files = []
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        if process_file(os.path.join(directory, filename)):
            updated_files.append(filename)

print("Updated files:", updated_files)
