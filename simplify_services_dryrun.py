"""
Service Pages Simplification Script
Restructures all service pages to match the dantu-tiesinimas-ortopedija.html template
"""

import os
import re
from bs4 import BeautifulSoup

# Configuration
BASE_DIR = "/Users/dariuslukosius/Desktop/3/svytintys dantys web/paslaugos"
TEMPLATE_FILE = "dantu-tiesinimas-ortopedija.html"

# Service-specific content mappings
SERVICE_CONFIG = {
    "burnos-higiena.html": {
        "title": "Profesionali Burnos Higiena",
        "service_name": "Burnos higiena",
        "photo": "../Photos/nuotraukos naujos/burnos higiena.jpg",
        "doctor": "Agnė Širvinskaitė",
        "doctor_photo": "../Photos/Personalas/Doktor.png",
        "doctor_role": "Burnos higienistė",
        "doctor_desc": "Didelį dėmesį skirianti profilaktikai, estetinei burnos priežiūrai bei ilgalaikiams rezultatams",
        "specialties": ["Profesionali burnos higiena", "Dantų balinimas"]
    },
    "dantu-balinimas-lazeriu.html": {
        "title": "Dantų Balinimas Lazeriu",
        "service_name": "Dantų balinimas lazeriu",
        "photo": "../Photos/nuotraukos naujos/dantu balinimas.jpg",
        "doctor": "Agnė Širvinskaitė",
        "doctor_photo": "../Photos/Personalas/Doktor.png",
        "doctor_role": "Burnos higienistė",
        "doctor_desc": "Specializuojasi profesionalioje burnos higienoje ir estetiniuose balinimo procedurose",
        "specialties": ["Dantų balinimas", "Profesionali burnos higiena"]
    },
    "estetinis-plombavimas.html": {
        "title": "Estetinis Plombavimas",
        "service_name": "Estetinis plombavimas",
        "photo": "../Photos/nuotraukos naujos/estetinis plombavimas.jpg",
        "doctor": "Kornelija Virbukaitė", 
        "doctor_photo": "../Photos/Personalas/Kornelija Virbukaite.jpg",
        "doctor_role": "Tiesinimo kapomis koordinatorė",
        "doctor_desc": "Profesionali estetinio plombavimo ir terapinio gydymo specialistė",
        "specialties": ["Estetinė odontologija", "Terapinis gydymas"]
    },
    "ortodontinis-gydymas.html": {
        "title": "Ortodontinis Gydymas",
        "service_name": "Ortodontinis gydymas",
        "photo": "../Photos/nuotraukos naujos/dantu tiesinimas.jpg",
        "doctor": "Sigita Morkuvienė",
        "doctor_photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
        "doctor_role": "Ortodontė, Klinikos Vadovė",
        "doctor_desc": "30 metų klinikinė patirtis ortodontiniu gydymu ir dantų tiesinim kapomis",
        "specialties": ["Ortodontinis gydymas", "Danţų tiesinimas kapomis"]
    },
    # Add more configs as needed...
}

# Default doctor if not specified
DEFAULT_DOCTOR = {
    "doctor": "Sigita Morkuvienė",
    "doctor_photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
    "doctor_role": "Klinikos Vadovė",
    "doctor_desc": "30 metų klinikinė patirtis visose odontologijos srityse",
    "specialties": ["Estetinė odontologija", "Ortodontinis gydymas"]
}

def extract_existing_content(filepath):
    """Extract H1 title and meta description from existing file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract H1
        h1 = soup.find('h1')
        title = h1.text.strip() if h1 else "Paslau ga"
        
        # Extract meta description
        meta_desc = soup.find('meta', {'name': 'description'})
        description = meta_desc['content'] if meta_desc and meta_desc.get('content') else ""
        
        # Extract image if exists
        img = soup.find('img', alt=re.compile(r'.*', re.I))
        photo = img['src'] if img else None
        
        return {
            'title': title,
            'description': description,
            'photo': photo
        }
    except Exception as e:
        print(f"Error extracting from {filepath}: {e}")
        return {'title': 'Paslauga', 'description': '', 'photo': None}

def simplify_service_page(filename):
    """Simplify a single service page"""
    filepath = os.path.join(BASE_DIR, filename)
    
    # Skip if template or doesn't exist
    if filename == TEMPLATE_FILE or not os.path.exists(filepath):
        return False
        
    print(f"\nProcessing: {filename}")
    
    # Get config or use defaults
    config = SERVICE_CONFIG.get(filename, {})
    
    # Extract existing content
    existing = extract_existing_content(filepath)
    
    # Merge config with existing
    service_title = config.get('title', existing['title'])
    service_name = config.get('service_name', service_title)
    photo = config.get('photo', existing.get('photo', '../Photos/nuotraukos naujos/placeholder.jpg'))
    
    # Doctor info
    doctor_info = {
        'name': config.get('doctor', DEFAULT_DOCTOR['doctor']),
        'photo': config.get('doctor_photo', DEFAULT_DOCTOR['doctor_photo']),
        'role': config.get('doctor_role', DEFAULT_DOCTOR['doctor_role']),
        'desc': config.get('doctor_desc', DEFAULT_DOCTOR['doctor_desc']),
        'specialties': config.get('specialties', DEFAULT_DOCTOR['specialties'])
    }
    
    print(f"  Title: {service_title}")
    print(f"  Doctor: {doctor_info['name']}")
    print(f"  Photo: {photo}")
    
    return True

def main():
    """Main execution"""
    print("=" * 60)
    print("SERVICE PAGES SIMPLIFICATION - DRY RUN")
    print("=" * 60)
    
    # Get all HTML files in paslaugos directory
    files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]
    
    print(f"\nFound {len(files)} HTML files")
    print(f"Template: {TEMPLATE_FILE}")
    print(f"Files to process: {len(files) - 1}\n")
    
    processed = 0
    skipped = 0
    
    for filename in sorted(files):
        if filename == TEMPLATE_FILE:
            print(f"⊙ SKIP: {filename} (template)")
            skipped += 1
            continue
            
        result = simplify_service_page(filename)
        if result:
            processed += 1
            print(f"✓ PROCESSED: {filename}")
        else:
            skipped += 1
            print(f"✗ SKIPPED: {filename}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: Processed {processed}, Skipped {skipped}")
    print("=" * 60)
    print("\n⚠️  This was a DRY RUN - no files were modified")
    print("To execute changes, modify the script to actually write files\n")

if __name__ == "__main__":
    main()
