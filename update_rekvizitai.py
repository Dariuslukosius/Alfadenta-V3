import os
import re

def update_footer_rekvizitai(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # The new block content
        new_block_content = """<li>Įm. k.: 303415894</li>
                                        <li>PVM mokėtojas: ne PVM mokėtojas</li>
                                        <li>Bankas: Luminor bankas</li>
                                        <li>SWIFT: AGBLLT2X</li>
                                        <li>A.s.: LT87 4010 0510 0217 6965</li>"""

        # Pattern to match the old block (handling whitespace/newlines)
        # We need to match efficiently. The key anchor is the company code.
        # We look for the sequence: Im. k. ... Bankas ... A.s.
        pattern = r'(<li>Įm\. k\.: 303415894</li>.*?<li>A\.s\.: LT87 4010 0510 0217 6965</li>)'
        
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # We found the block
            # To handle indentation, we could check the indentation of the first line of the match
            # But simpler is to just replace.
            new_content = count = re.sub(pattern, new_block_content, content, count=1, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")
            return True
        else:
            print(f"Pattern not found in {file_path}")
            return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# List of files to check
root_dir = "/Users/dariuslukosius/Desktop/3 2/Alfa denta web page"
files_to_update = []

# Walk through directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html"):
            files_to_update.append(os.path.join(dirpath, filename))

count = 0
for file_path in files_to_update:
    if update_footer_rekvizitai(file_path):
        count += 1

print(f"Total files updated: {count}")
