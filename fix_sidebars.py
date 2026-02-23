import os

files_to_update = [
    "favsigns.html",
    "game1.html",
    "help&support.html",
    "liveinterpreter.html",
    "monthlyprogress.html",
    "practice complete.html",
    "sessioncomplete.html",
    "sessionhistory.html",
    "today'sgoal.html"
]

target_dir = r"e:\MUDRA"

games_link = """                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="game.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">videogame_asset</span>
                    <span class="text-sm font-medium">Games</span>
                </a>
"""

for filename in files_to_update:
    filepath = os.path.join(target_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'href="game.html"' in content:
            print(f"Skipping {filename} - already contains game.html")
            continue
            
        # Look for the Practice link and insert Games after it
        practice_marker = 'href="practice.html"'
        if practice_marker in content:
            # Find the end of the </a> tag following the practice marker
            marker_pos = content.find(practice_marker)
            end_tag_pos = content.find('</a>', marker_pos)
            if end_tag_pos != -1:
                insert_pos = end_tag_pos + 4
                new_content = content[:insert_pos] + "\n" + games_link + content[insert_pos:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"Could not find end tag for Practice in {filename}")
        else:
            print(f"Could not find Practice link in {filename}")
    else:
        print(f"File not found: {filename}")
