
import os
import re

def extract_faqs():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find all FAQ answers
            # Looking for div with inside p
            # <div class="..." id="faq..."> <p> ... </p> </div>
            
            # Regex to find id="faq..." and then capture content until </div>
            # This is a bit rough for regex, but should work for this consistent structure
            matches = re.finditer(r'id="faq\d+"[^>]*>\s*<p>(.*?)</p>', content, re.DOTALL)
            
            count = 0
            for match in matches:
                answer = match.group(1).strip()
                count += 1
                # Check for suspicious answers
                if len(answer) < 5 or "lorem" in answer.lower() or "atsakymas" in answer.lower():
                    print(f"SUSPICIOUS in {file}: {answer}")
                # print(f"{file}: {answer[:30]}...")
            
            if count == 0 and 'faq-toggle' in content:
                 print(f"WARNING: {file} has faq-toggle but no answers found with regex")
            if count == 0 and 'faq-toggle' not in content:
                print(f"INFO: {file} has NO FAQ section")

if __name__ == "__main__":
    extract_faqs()
