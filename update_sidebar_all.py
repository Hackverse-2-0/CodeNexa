import os
import re

SIDEBAR_HTML = """    <aside class="w-64 flex-shrink-0 flex flex-col justify-between bg-white dark:bg-slate-900 border-r border-slate-200 dark:border-slate-800 h-full z-20">
        <div class="flex flex-col gap-6 p-6 overflow-y-auto" style="-ms-overflow-style: none; scrollbar-width: none;">
            <style>aside div::-webkit-scrollbar { display: none; }</style>
            <!-- Profile Section -->
            <div class="flex items-center gap-3">
                <div class="relative bg-center bg-no-repeat bg-cover rounded-full h-12 w-12 shadow-sm border border-slate-200"
                    style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuC8XBXafHP-hEfaJ0c0RGZVsQXZnhbrwVRrbHZR_KN2h0fQp_uIESQMbqF-OQ6HST9aeAhDtnBJoVqO42pxaqvn_q6ZVQUFjeaFb7asMOlSErk6sGhnJVGuy7piPIejRL1bMURlJfImFHJRrVeU_v8aPTmH9LppSpi1ljhGTMZvyx_h68VMAvv_PJoknFQHJff8CC-dJCoQyB8i_DsoxhhKU-P9p80aFgubZd2d5s7qBu4Dy5suBk9CSoq94wciTR_Ne8eoFHd9OXdS");'>
                    <div class="absolute bottom-0 right-0 h-3 w-3 bg-green-500 rounded-full border-2 border-white dark:border-slate-900"></div>
                </div>
                <div class="flex flex-col">
                    <h1 class="text-slate-900 dark:text-white text-base font-bold leading-tight">Soumya</h1>
                    <p class="text-slate-500 dark:text-slate-400 text-xs font-medium">Student</p>
                </div>
            </div>
            <!-- Navigation -->
            <nav class="flex flex-col gap-2">
                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="index.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">dashboard</span>
                    <span class="text-sm font-medium">Dashboard</span>
                </a>
                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="learnsignlanguage.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">school</span>
                    <span class="text-sm font-medium">Learn Signs</span>
                </a>
                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="ISLdictionary.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">menu_book</span>
                    <span class="text-sm font-medium">Dictionary</span>
                </a>
                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="practice.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">sports_esports</span>
                    <span class="text-sm font-medium">Practice</span>
                </a>
                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="game.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">videogame_asset</span>
                    <span class="text-sm font-medium">Games</span>
                </a>
                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="videototext.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">translate</span>
                    <span class="text-sm font-medium">Translator</span>
                </a>
                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="globalranking.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">leaderboard</span>
                    <span class="text-sm font-medium">Leaderboard</span>
                </a>
                <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="about.html">
                    <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">info</span>
                    <span class="text-sm font-medium">About</span>
                </a>
            </nav>
        </div>
        <!-- Bottom Actions -->
        <div class="p-6 border-t border-slate-200 dark:border-slate-800">
            <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="profile.html">
                <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">person</span>
                <span class="text-sm font-medium">Profile</span>
            </a>
            <a class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-slate-800 transition-colors group" href="settings.html">
                <span class="material-symbols-outlined text-slate-500 group-hover:text-blue-600 transition-colors">settings</span>
                <span class="text-sm font-medium">Settings</span>
            </a>
        </div>
        <script>
            document.addEventListener("DOMContentLoaded", () => {
                const currentUrl = window.location.pathname.split('/').pop() || 'index.html';
                const sidebarLinks = document.querySelectorAll('aside nav a, aside div.p-6.border-t a');
                sidebarLinks.forEach(link => {
                    const href = link.getAttribute('href');
                    if (href === currentUrl || (href === 'index.html' && currentUrl === '')) {
                        link.classList.remove('text-slate-600', 'dark:text-slate-300', 'hover:bg-blue-50', 'dark:hover:bg-slate-800');
                        link.classList.add('bg-blue-50', 'text-blue-600', 'dark:bg-slate-800', 'font-semibold');
                        const icon = link.querySelector('.material-symbols-outlined');
                        if (icon) {
                            icon.classList.remove('text-slate-500', 'group-hover:text-blue-600');
                            icon.classList.add('text-blue-600');
                        }
                    }
                });
            });
        </script>
    </aside>"""

def replace_sidebar(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    filename = os.path.basename(filepath)

    if "<aside" in new_content.lower():
        # Using a proper replacement logic for `<aside>` blocks
        new_content = re.sub(r'<aside\b.*?</aside>', SIDEBAR_HTML, new_content, flags=re.DOTALL | re.IGNORECASE)
    elif "<!-- Sidebar -->" in new_content:
        # Match from <!-- Sidebar --> until <!-- Main Content -->
        new_content = re.sub(r'<!-- Sidebar -->.*?<!-- Main Content -->', "<!-- Sidebar -->\n" + SIDEBAR_HTML + "\n        <!-- Main Content -->", new_content, flags=re.DOTALL)
    else:
        # Custom logic for files without an obvious tag
        if filename == "practice.html":
            # the sidebar is the first div with w-72 inside flex h-screen
            # Replace lines 50 to 104 roughly
            start_str = r'<div class="hidden lg:flex w-72 flex-col justify-between border-r border-blue-100 bg-sidebar-bg p-4">'
            end_str = r'<div class="flex-1 flex flex-col h-full overflow-hidden bg-white relative">'
            new_content = re.sub(start_str + r'.*?(?=' + end_str + ')', SIDEBAR_HTML + '\n        ', new_content, flags=re.DOTALL)
            
        elif filename == "today'sgoal.html":
            # It's an absolute decorative div. Find <div class="absolute left-0 top-0 bottom-0 w-64 bg-white border-r border-slate-200 hidden lg:flex flex-col p-6 gap-6">
            start_str = r'<div\s+class="absolute left-0 top-0 bottom-0 w-64 bg-white border-r border-slate-200 hidden lg:flex flex-col p-6 gap-6">'
            end_str = r'<!-- Header placeholder -->'
            new_content = re.sub(start_str + r'.*?(?=' + end_str + ')', SIDEBAR_HTML + '\n        ', new_content, flags=re.DOTALL)

    if new_content != content:
        # Remove lg:ml-64 which makes content right padded assuming fixed sidebar
        new_content = re.sub(r'\blg:ml-64\b', '', new_content)
        # Also let's make sure the body/main container remains correctly flexed if it wasn't
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

directory = r"e:\MUDRA"
updated_files = []
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        if replace_sidebar(os.path.join(directory, filename)):
            updated_files.append(filename)

print("Updated files:", updated_files)
