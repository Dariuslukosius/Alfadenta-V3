"""
Generate Test Service Pages
Creates 5 simplified service pages based on the template
"""

from bs4 import BeautifulSoup
import os

BASE_DIR = "/Users/dariuslukosius/Desktop/3/svytintys dantys web/paslaugos"
TEMPLATE = "dantu-tiesinimas-ortopedija.html"

# Complete content configuration for 5 test pages  
SERVICES = {
    "burnos-higiena.html": {
        "meta_title": "Profesion ali Burnos Higiena Kaune – Dantų Valymas | Alfadenta",
        "meta_desc": "Profesionali burnos higiena Kaune. Dantų akmens šalinimas, balinimas, prevencija. Patyrusi burnos higienistė. Registruokitės ☎ +370 612 03030",
        "meta_keywords": "burnos higiena, dantų valymas, dantų akmens šalinimas, profesionali higiena kaunas, burnos higienistė",
        "og_url": "https://alfadenta.lt/paslaugos/burnos-higiena",
        "breadcrumb": "Burnos higiena",
        "h1": "Profesionali Burnos Higiena – Sveikos Dantenos ir Šviesi Šypsena",
        "intro": "Profesionali burnos higiena – tai ne tik estetika, bet ir sveikingumo pagrindas. Reguliarus dantų akmens ir apnašų šalinimas apsaugo nuo dantenų uždegimo, dantų ėduonies ir kitų periodontalinių ligų. Mūsų burnos higienistė naudoja švelnias, bet efektyvias technologijas, užtikrinančias ilg alaikius rezultatus.",
        "benefits": [
            ("Profesionalus dantų valymas", "šalinamas dantų akmuo ir apnašai"),
            ("Dantenų ligų prevencija", "apsauga nuo periodontito"),
            ("Dantų balinimas", "natūraliai šviesesnė šypsena"),
            ("Individualūs higienos patarimai", "kaip prižiūrėti dantis namuose")
        ],
        "photo": "../Photos/nuotraukos naujos/burnos higiena.jpg",
        "slug": "burnos-higiena",
        "doctor": {
            "name": "Agnė Širvinskaitė",
            "role": "Burnos higienistė",
            "desc": "15 metų patirtis profesionalioje burnos higienoje. Didelis dėmesys skiriamas profilaktikai, estetinei priežiūrai bei ilgalaikiams rezultatams.",
            "photo": "../Photos/Personalas/Doktor.png",
            "specialties": ["Profesionali burnos higiena", "Dantų balinimas"]
        },
        "faqs": [
            ("Kaip dažnai reikia atlikti profesionalią burnos higieną?", "Rekomenduojama lankytis pas burnos higienistę kas 6 mėnesius. Jei turite danteų problemų ar greitai kaupiasi dantų akmuo, dažniau – kas 3-4 mėnesius."),
            ("Ar procedūra skaudi?", "Procedūra nėra skaudi. Galite pajusti nedidelį diskomfortą, ypač jei turite jautrių dantenų. Esant reikalui galime panaudoti vietinę anesteziją."),
            ("Ar galima valgyti po procedūros?", "Taip, galite valgyti iš karto po procedūros. Tačiau pirmą dieną ven kite labai karštų gėrimų ir dažančių produktų (kava, arbata, raudonas vynas)."),
            ("Kiek kainuoja profesionali burnos higiena?", "Kaina priklauso nuo procedūros apimties. Standartinė profesionali higiena kainuoja nuo 50-80 EUR. Tikslią kainą sužinosite konsultacijos metu."),
            ("Ar balinsis dantys po higienos?", "Taip, pašalinus dantų akmenį ir apnašus, dantys tampa švieresni ir grąžinamas natūralus atspalvis. Tai nėra dantų balinimas, bet estetinis pagerėjimas yra akivaizdus.")
        ]
    },
    
    "dantu-balinimas-lazeriu.html": {
        "meta_title": "Dantų Balinimas Lazeriu Kaune – Balta Šypssena per 1 val. | Alfadenta",
        "meta_desc": "Dantų balinimas lazeriu Kaune. Profesionalus, saugus balinimas iki 8 atspalvių. Be skausmo, greitas rezultatas. Registracija ☎ +370 612 03030",
        "meta_keywords": "dantų balinimas, balinimas lazeriu, dantų balinimas kaunas, profesionalus balinimas, balta šypsena",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-balinimas-lazeriu",
        "breadcrumb": "Dantų balinimas lazeriu",
        "h1": "Dantų Balinimas Lazeriu – Balta Šypsena per Vieną Valandą",
        "intro": "Dantų balinimas lazeriu – moderniausias ir efektyviausias būdas pasiekti baltą, žėrinčią šypseną. Procedūra yra saugi, neskausminga ir trunka vos 45-60 minučių. Galite pašviesinti dantis iki 6-8 atspalvių, o rezultatas işlieka ilgam.",
        "benefits": [
            ("Greitas rezultatas", "per 45-60 minučių"),
            ("Iki 8 atspalvių šviesesni", "akivaizdus pokytis"),
            ("Saugi ir neskausminga", "lazeriu metodu"),
            ("Ilgalaikis efektas", "išlieka 1-3 metus")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu balinimas.jpg",
        "slug": "dantu-bal inimas-lazeriu",
        "doctor": {
            "name": "Agnė Širvinskaitė",
            "role": "Burnos higienistė",
            "desc": "Specializuojasi profesionalioje burnos hygiene ir estetiniuose balinimo procedurose. Individualus požiūris į kiekvieną pacientą.",
            "photo": "../Photos/Personalas/Doktor.png",
            "specialties": ["Dantų balinimas lazeriu", "Profesionali burnos higiena"]
        },
        "faqs": [
            ("Ar balinimas pakenkia dantims?", "Ne, profesionalus dantų balinimas lazeriu yra saugus. Naudojame aukščiausios kokybės gelį, kuris nesugadina emalio. Prieš procedūrą įvertiname dantų būklę."),
            ("Kiek laiko išlieka rezultatas?", "Rezultatas išlieka 1-3 metus, priklausomai nuo jūsų įpročių. Jei rūkote, gėriate daug kavos ar raudoną vyną, efektas gali išblėsti greičiau."),
            ("Ar bus jautrumas po procedūros?", "Galimas trumpalaikis dantų jautrumas 24-48 valandas po procedūros. Tai normalu ir greitai praeina. Rekomenduojame dantų pastą jautriems dantims."),
            ("Ar galima balinti dantis su plombomis?", "Taip, tačiau plombos ir karūnėlės nebalinasi. Jei turite didelių plombų priekinėse dalyse, po balinimo jos gali išsiskirti spalva. Tokiu atveju jas reikės pake isti."),
            ("Ką daryti prieš balinimą?", "Prieš 1-2 savaites rekomenduojame atlikti profesionalią burnos higieną. Tai užtikrins geresnį ir tolygesnį balinimo rezultatą.")
        ]
    },
    
    "estetinis-plombavimas.html": {
        "meta_title": "Estetinis Plombavimas Kaune – Nematomos Plombos | Alfadenta",
        "meta_desc": "Estetinis dantų plombavimas Kaune. Nematomos šviesoje kietėjančios kompozitinės plombos. Natūral us rezultatas. Tel. ☎ +370 612 03030",
        "meta_keywords": "estetinis plombavimas, kompozitinės plombos, dantų plombavimas, estetinis gydymas kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/estetinis-plombavimas",
        "breadcrumb": "Estetinis plombavimas",
        "h1": "Estetinis Plombavimas – Nematomos Plombos, Tobula Šypsena",
        "intro": "Estetinis plombavimas – tai dabarties odontologijos standartas. Naudojame aukščiausios kokybės šviesoje kietėjančius kompozitus, kurie idealiai atitinka natūralų dantų atspalvį. Plombos yra nematomos, tvirtos ir ilgaamžės.",
        "benefits": [
            ("Natūralus atspalvis", "plomba nematoma"),
            ("Aukšta kokybė", "šviesoje kietėjantys kompozitai"),
            ("Ilgaamžiškumas", "tarnauja 5-10+ metų"),
            ("Neskausminga procedūra", "su vietine anestezija")
        ],
        "photo": "../Photos/nuotraukos naujos/estetinis plombavimas.jpg",
        "slug": "estetinis-plombavimas",
        "doctor": {
            "name": "Kornelija Virbukaitė",
            "role": "Tiesinimo kapomis koordinatorė",
            "desc": "Profesionali estetinio plombavimas ir terapinio gydymo specialistė. Nuolat tobulina ž inias estetinės odontologijos seminaruose.",
            "photo": "../Photos/Personalas/Kornelija Virbukaite.jpg",
            "specialties": ["Estetinė odontologija", "Terapinis gydymas"]
        },
        "faqs": [
            ("Kuo estetinis plombavimas skiriasi nuo paprasto?", "Estetinis plombavimas naudoja šviesoje kietėjančius kompozitus, kurie tiksliai atitinka dantų spalvą ir struktūrą. Paprasti amalgaminiai plomba yra metalo spalvos ir matomos."),
            ("Kiek laiko trunka procedūra?", "Paprastai 30-60 minučių, priklausomai nuo ėduonies dydžio. Naudojame vietinę anesteziją, todėl procedūra yra neskausminga."),
            ("Ar plomba gali atkristi?", "Kokybiška plomba atitinkamai įdėta gali tarnauti 5-10+ metų. Svarbu laikytis burnos higienos ir reguliariai lankytis pas odontologą patikroms."),
            ("Ar galima plombuoti priekinius dantis?", "Taip! Estetinis plombavimas puikiai tinka priekiniams dantims. Galime atkurti nulūžusius kampus, užpildyti tarpus ar pagerinti dantų formą."),
            ("Ar skauda po plombavimo?", "Nedidelis jautrumas 1-2 dienas po procedūros yra normalus. Jei skausmas nepraeina arba stiprėja, kreipkitės į mus – gali būti reikalinga korekcija.")
        ]
    },
    
    "ortodontinis-gydymas.html": {
        "meta_title": "Ortodontinis Gydymas Kaune – Breketai, Kapos | Alfadenta",
        "meta_desc": "Ortodontinis dantų gydymas Kaune. Breketai, skaidrios kapos vaikams ir suaugusiems. 30 metų patirtis. Konsultacija ☎ +370 612 03030",
        "meta_keywords": "ortodontinis gydymas, breketai, dantų tiesinimas, ortodontas kaunas, kapos dantims",
        "og_url": "https://alfadenta.lt/paslaugos/ortodontinis-gydymas",
        "breadcrumb": "Ortodontinis gydymas",
        "h1": "Ortodontinis Gydymas – Taisyklinga Šypsena ir Sveikas Sukandimas",
        "intro": "Ortodontinis gydymas ne tik sukuria gražią šypseną, bet ir atkuria taisyklingą kramtymo funkciją bei ilgalaikę dantų sveikatą. Siūlome modernius sprendimus vaikams ir suaugusiems: tradiciniai breketai, keramikini breketai, skaidrios kapos. Kiekvienas gydymo planas yra individualus ir pritaikytas jūsų poreikiams.",
        "benefits": [
            ("Modernios ortodontinės sistemos", "breketai, skaidrios kapos"),
            ("Individualus gydymo planas", "kiekvienam pacientui"),
            ("Tinka vaikams ir suaugusiems", "be amžiaus ribų"),
            ("Patyrusi ortodontė", "30 metų klinikinė patirtis")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu tiesinimas.jpg",
        "slug": "ortodontinis-gydymas",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Ortodontė, Klinikos Vadovė",
            "desc": "30 metų klinikinė patirtis ortodontiniu gydymu ir dantų tiesinimų kapomis. Specializuojasi sudėtingų ortodontinių atvejų gydyme.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Ortodontinis gydymas", "Dantų tiesinimas kapomis"]
        },
        "faqs": [
            ("Kiek laiko trunka ortodontinis gydymas?", "Gydymo trukmė labai individuali ir priklauso nuo atvejo sudėtingumo. Vidutiniškai breketais trunka 1.5-2 metus, kapomis – 6-18 mėnesių."),
            ("Ar skaudu dėvėti breketus?", "Uždė jus breketus, 2-3 dienas gali būti jaučiamas nedidelis spaudimas ir diskomfortas. Tai normalu ir rodo, kad dantys pradeda judėti. Diskomfortą galima malšinti vaistais nuo skausmo."),
            ("Ar yra amžiaus riba ortodontiniam gydymui?", "Ne! Dantis tiesinti galima ir vaikams, ir suaugusiems, ir senjorams. Svarbiausia, kad dantys ir dantenos būtų sveiki."),
            ("Kiek kainuoja ortodontinis gydymas?", "Kaina priklauso nuo gydymo metodo ir trukmės. Breketai kainuo ja nuo 1500-3000 EUR, skaidrios kapos – nuo 2000-4000 EUR. Siūlome išsimokėtinas mokėjimo sąlygas."),
            ("Kaip dažnai reikia lankytis pas ortodontą gydymo metu?", "Gydymo breketais metu – kas 4-6 savaites. Gydymo kapomis metu – kas 6-8 savaites. Vizitai trumpi, tinkami tik korekcijai."),
            ("Ar pasikeis mano veidas?", "Ortodontinis gydymas gali šiek tiek pakeisti veido proporcijas – paprastai į gerąją pusę. Pakilęs kandis, taisyklingas sukandimas gali pagerinti veido estetiką.")
        ]
    },
    
    "dantu-implantavimas.html": {
        "meta_title": "Dantų Implantacija Kaune – Atstatykite Trūkstamus Dantis | Alfadenta",
        "meta_desc": "Dantų implantacija Kaune. Kokybiški titano implantai, greitas gijimas, ilgalaikė garantija. Patyrę specialistai. Registracija ☎ +370 612 03030",
        "meta_keywords": "dantų implantacija, dantų implantai, implantavimas kaunas, titano implantai, dantų atstatymas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-implantavimas",
        "breadcrumb": "Dantų implantacija",
        "h1": "Dantų Implantacija – Patikimiausias Būdas Atstatyti Trūkstamus Dantis",
        "intro": "Dantų implantacija – tai moderniausias ir patikimiausias būdas atstatyti trūkstamus dantis. Titano implantas įauginamas į kaulą ir tarnauja kaip natūrali danties šaknis, ant kurios pritvirtinama karūnėlė, tiltelis ar protezas. Rezultatas – stabilus, patogus ir atrodantis natūraliai.",
        "benefits": [
            ("Kokybiški titano implantai", "ilgaamžiai ir biokompatibilūs"),
            ("Natūralus rezultatas", "atrodo ir jaučiasi kaip tikras dantis"),
            ("Ilgalaikė garantija", "implantai tarnauja 20+ metų"),
            ("Modernios technologijos", "3D planavimas, kompiuterinė navigacija")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu implantacija.jpg",
        "slug": "dantu-implantavimas",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Klinikos Vadovė",
            "desc": "30 metų patirtis odontologijoje, specializuojasi dantų implantacijoje ir estetinėje odontologijoje. Daugiau nei 1000 sėkmingų implantacijų.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Dantų implantacija", "Estetinė odontologija"]
        },
        "faqs": [
            ("Ar implantacija skaudi?", "Ne, procedūra atliekama su vietine arba bendrąja anestezija, todėl skausmo nejaučiate. Po procedūros 2-3 dienas gali būti nedidelis patinimas ir diskomfortas, kuris lengvai malšinamas vaistais."),
            ("Kiek laiko trunka implanto įgyijimas?", "Implanto įauginimas (oseointegracija) trunka 3-6 mėnesius. Po to galima tvirtinti galutinę karūnėlę. Kai kuriais atvejais galima vienmomentė implantacija su laikina karūnėlės."),
            ("Ar implantai yra saugūs?", "Taip! Titano implantai yra biokompatibilūs ir organizmas juos priima kaip savo. Atmestis yra labai retas – sėkmės rodiklis >95%."),
            ("Kiek laiko tarnauja implantai?", "Kokybiški implantai gali tarnauja 20-30+ metų arba net visą gyvenimą, jei tinkamai prižiūrimi. Svarbu laikytis burnos higienos ir reguliariai lankytis patikroms."),
            ("Ar galima implantus visiems?", "Dauguma žmonių gali gauti implantus, tačiau yra kontraindikacijų: nekontroliuojamas cukraus diabetas, vėžys, tam tikri kaulų ligos. Konsultacijos metu įvertiname jūsų tinkumą."),
            ("Kiek kainuoja dantų implantacija?", "Vieno implanto su karūnėle kaina pradeda nuo 800-1500 EUR, priklausomai nuo implanto gamintojo ir gydymo sudėtingumo. Siūlome išsimokėtinas mokėjimo sąlygas.")
        ]
    }
}

def load_template():
    """Load the template file"""
    template_path = os.path.join(BASE_DIR, TEMPLATE)
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_page(filename, config, template):
    """Generate a single service page"""
    print(f"\nGenerating: {filename}")
    
    # Parse template
    soup = BeautifulSoup(template, 'html.parser')
    
    # Update title
    title = soup.find('title')
    if title:
        title.string = config['meta_title']
        print(f"  ✓ Title: {config['meta_title'][:50]}...")
    
    # Update meta description
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc:
        meta_desc[' content'] = config['meta_desc']
        print(f"  ✓ Meta description updated")
    
    # Update meta keywords
    meta_keywords = soup.find('meta', {'name': 'keywords'})
    if meta_keywords:
        meta_keywords['content'] = config['meta_keywords']
    
    # Update OG URL
    og_url = soup.find('meta', {'property': 'og:url'})
    if og_url:
        og_url['content'] = config['og_url']
   
    # Update breadcrumb
    breadcrumb = soup.select_one('.text-indigo-500.font-medium')
    if breadcrumb:
        breadcrumb.string = config['breadcrumb']
        print(f"  ✓ Breadcrumb: {config['breadcrumb']}")
    
    # Update H1
    h1 = soup.find('h1')
    if h1:
        h1.string = config['h1']
        print(f"  ✓ H1: {config['h1'][:50]}...")
    
    # Update intro text
    intro_p = soup.select_one('section.py-16.bg-gray-50 p.text-lg')
    if intro_p:
        intro_p.string = config['intro']
        print(f"  ✓ Intro text updated")
    
    # Update benefits list
    benefits_ul = soup.select_one('section.py-16.bg-gray-50 ul.space-y-3')
    if benefits_ul:
        # Clear existing list items
        for li in benefits_ul.find_all('li'):
            li.decompose()
        
        # Add new benefits
        for title, desc in config['benefits']:
            new_li = soup.new_tag('li', **{'class': 'flex items-center'})
            icon = soup.new_tag('i', **{'class': 'fas fa-check-circle text-indigo-500 mr-3 text-xl'})
            span = soup.new_tag('span', **{'class': 'text-gray-700'})
            strong = soup.new_tag('strong')
            strong.string = title
            span.append(strong)
            span.append(f" – {desc}")
            new_li.append(icon)
            new_li.append(span)
            benefits_ul.append(new_li)
        print(f"  ✓ Benefits: {len(config['benefits'])} items")
    
    # Update hero image
    hero_img = soup.select_one('section.py-16.bg-gray-50 img')
    if hero_img:
        hero_img['src'] = config['photo']
        hero_img['alt'] = config['h1']
        print(f"  ✓ Image: {config['photo']}")
    
    # Update booking link
    booking_link = soup.select_one(f'a[href*="booking.html"]')
    if booking_link:
        booking_link['href'] = f"../booking.html?service={config['slug']}"
    
    # Update doctor section
    doctor = config['doctor']
    doctor_name = soup.select_one('h3.text-2xl.font-bold')
    if doctor_name:
        doctor_name.string = f"Gyd. {doctor['name']}"
        print(f"  ✓ Doctor: {doctor['name']}")
    
    doctor_role = soup.select_one('p.text-indigo-600.font-semibold')
    if doctor_role:
        doctor_role.string = doctor['role']
    
    doctor_desc = soup.select_one(".flex.items-center.bg-gradient-to-r p.text-gray-600")
    if doctor_desc:
        doctor_desc.string = doctor['desc']
    
    doctor_img = soup.select_one('section.py-16.bg-white img')
    if doctor_img:
        doctor_img['src'] = doctor['photo']
        doctor_img['alt'] = f"Gyd. {doctor['name']}"
    
    # Update doctor specialties badges
    badges_div = soup.select_one('.flex.flex-wrap.gap-2.mt-3')
    if badges_div:
        for badge in badges_div.find_all('span'):
            badge.decompose()
        
        for specialty in doctor['specialties']:
            new_badge = soup.new_tag('span', **{'class': 'bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full text-xs font-semibold'})
            new_badge.string = specialty
            badges_div.append(new_badge)
    
    # Update FAQ section
    faq_container = soup.select_one('.max-w-3xl.mx-auto.space-y-4')
    if faq_container:
        # Clear existing FAQs
        for faq_div in faq_container.find_all('div', class_='bg-white'):
            faq_div.decompose()
        
        # Add new FAQs
        for idx, (question, answer) in enumerate(config['faqs'], 1):
            faq_id = f"faq{idx}"
            
            faq_div = soup.new_tag('div', **{'class': 'bg-white rounded-lg p-6 shadow-md'})
            
            button = soup.new_tag('button', **{
                'class': 'w-full text-left flex justify-between items-center faq-toggle',
                'data-target': faq_id
            })
            
            h3 = soup.new_tag('h3', **{'class': 'font-bold text-gray-800'})
            h3.string = question
            
            icon = soup.new_tag('i', **{'class': 'fas fa-chevron-down text-indigo-500 transition-transform'})
            
            button.append(h3)
            button.append(icon)
            
            answer_div = soup.new_tag('div', **{
                'id': faq_id,
                'class': 'hidden mt-4 text-gray-600 leading-relaxed border-t pt-4 border-gray-200'
            })
           
            p = soup.new_tag('p')
            p.string = answer
            answer_div.append(p)
            
            faq_div.append(button)
            faq_div.append(answer_div)
            faq_container.append(faq_div)
        
        print(f"  ✓ FAQs: {len(config['faqs'])} questions")
    
    # Write to file
    output_path = os.path.join(BASE_DIR, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    print(f"  ✅ Saved: {filename}")
    return True

def main():
    """Main execution"""
    print("=" * 60)
    print("GENERATING 5 TEST SERVICE PAGES")
    print("=" * 60)
    
    # Load template
    print("\nLoading template...")
    template = load_template()
    print(f"✓ Template loaded: {TEMPLATE}")
    
    # Generate each page
    print(f"\nGenerating {len(SERVICES)} pages...")
    success_count = 0
    
    for filename, config in SERVICES.items():
        try:
            if generate_page(filename, config, template):
                success_count += 1
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
    
    print("\n" + "=" * 60)
    print(f"COMPLETE: {success_count}/{len(SERVICES)} pages generated successfully")
    print("=" * 60)
    print(f"\nCreated files:")
    for filename in SERVICES.keys():
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"  ✓ {filename} ({size:,} bytes)")

if __name__ == "__main__":
    main()
