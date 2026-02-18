import os
import re

def remove_links(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Patterns to remove <li>...<a ...>...</a>...</li> blocks containing specific text
                # We need to be careful to match the list item structure
                
                # Pattern for Vienmomentė implantacija (checking both spellings if needed, but assuming user input)
                # In dovanu-kuponai.html it was: <li>\n<a ... href="vienmomete-implantacija.html">\nVienmomentė\nimplantacija\n</a>\n</li>
                # The structure involves newlines.
                
                # Regex for "Vienmomentė implantacija"
                # Matches <li>...href="...vienmome?nte-implantacija..."...</li>
                # or just text content.
                
                # Let's try to match by href to be safer, or strict text.
                
                # Removing "Vienmomentė implantacija"
                content = re.sub(r'<li>\s*<a[^>]*href="[^"]*vienmome?nte-implantacija\.html"[^>]*>[\s\S]*?</a>\s*</li>', '', content, flags=re.IGNORECASE)
                
                 # Removing "Dantų protezavimas"
                content = re.sub(r'<li>\s*<a[^>]*href="[^"]*dantu-protezavimas\.html"[^>]*>[\s\S]*?</a>\s*</li>', '', content, flags=re.IGNORECASE)

                # Also remove "Dantų implantavimas" if user meant that too? 
                # User said: "Išimti - vienmomentė implantacija, Protezavimas"
                # dovanu-kuponai.html had "Dantų implantacija" separately. I should probably leave it unless asked.
                # But "Protezavimas" usually refers to "Dantų protezavimas".
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

# Run on the main directory
remove_links("/Users/dariuslukosius/Desktop/3 2/Alfa denta web page")
