"""
Generate Remaining Service Pages
Creates the remaining 17 simplified service pages based on the template
"""

from bs4 import BeautifulSoup
import os

BASE_DIR = "/Users/dariuslukosius/Desktop/3/svytintys dantys web/paslaugos"
TEMPLATE = "dantu-tiesinimas-ortopedija.html"

# Content configuration for remaining 17 pages  
SERVICES = {
    # 1. Balinimas Kapomis
    "balinimas-kapomis.html": {
        "meta_title": "Dantų Balinimas Kapomis Namuose | Alfadenta Kaunas",
        "meta_desc": "Saugus dantų balinimas kapomis namuose. Individualiai pagamintos kapos, profesionalus gelis, ilgalaikis rezultatas. Konsultacija ☎ +370 612 03030",
        "meta_keywords": "dantų balinimas kapomis, balinimas namuose, balinimo kapos, dantų balinimas kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/balinimas-kapomis",
        "breadcrumb": "Balinimas kapomis",
        "h1": "Dantų Balinimas Kapomis – Saugus Balinimas Namuose",
        "intro": "Balinimas kapomis – tai patogus ir saugus būdas pasiekti norimą dantų baltumą namuose. Mes pagaminame individualias kapas, kurios tiksliai tinka jūsų dantims, ir parenkame tinkamos koncentracijos balinimo gelį.",
        "benefits": [
            ("Patogumas", "balinkite dantis jums patogiu metu"),
            ("Individualios kapos", "tiksliai pritaikytos jūsų dantims"),
            ("Kontroliuojamas procesas", "patys sprendžiate, kada sustoti"),
            ("Ekonomiškas sprendimas", "kapas galite naudoti pakartotinai")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu balinimas.jpg",
        "slug": "balinimas-kapomis",
        "doctor": {
            "name": "Agnė Širvinskaitė",
            "role": "Burnos higienistė",
            "desc": "Specializuojasi profesionalioje burnos higienoje ir saugiuose balinimo metoduose.",
            "photo": "../Photos/Personalas/Doktor.png",
            "specialties": ["Dantų balinimas", "Profesionali burnos higiena"]
        },
        "faqs": [
            ("Kiek laiko reikia balinti?", "Paprastai kursas trunka 10-14 dienų, dėvint kapas po 2-4 valandas per dieną arba naktį."),
            ("Ar tai saugu?", "Taip, naudojant profesionalų gelį ir laikantis instrukcijų, emalis nėra pažeidžiamas."),
            ("Kada matysis rezultatas?", "Pirmieji rezultatai matomi jau po 3-4 dienų."),
            ("Kiek laiko išlieka baltumas?", "Rezultatas išlieka 1-2 metus, priklausomai nuo mitybos ir žalingų įpročių."),
            ("Ar galima naudoti senas kapas?", "Jei dantų forma nepasikeitė (nebuvo protezavimo), senas kapas galima naudoti, tereikia įsigyti gelio.")
        ]
    },

    # 2. Visi ant 4
    "dantu-atstatymas-visi-ant-4.html": {
        "meta_title": "Visi ant 4 (All-on-4) Implantacija Kaune | Alfadenta",
        "meta_desc": "Dantų atstatymas 'Visi ant 4' metodu Kaune. Viso žandikaulio dantų atkūrimas ant 4 implantų per vieną dieną. Fiksuoti protezai. ☎ +370 612 03030",
        "meta_keywords": "visi ant 4, all on 4, dantų atstatymas, implantacija kaunas, viso žandikaulio protezavimas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-atstatymas-visi-ant-4",
        "breadcrumb": "Visi ant 4",
        "h1": "Dantų Atstatymas „Visi ant 4“ – Nauja Šypsena per Vieną Dieną",
        "intro": "„Visi ant 4“ metodika leidžia atkurti viso žandikaulio dantis naudojant tik 4 implantus. Tai idealus sprendimas praradusiems visus ar daugumą dantų. Jau tą pačią dieną galite džiaugtis fiksuotais, stabiliais dantimis.",
        "benefits": [
            ("Fiksuoti dantys", "nereikia išiminėti nakčiai"),
            ("Greitas rezultatas", "dantys per 24 valandas"),
            ("Mažiau implantų", "tik 4 implantai visam žandikauliui"),
            ("Kaulo augmentacijos nereikia", "dažniausiai išvengiama kaulo priauginimo")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu implantacija.jpg",
        "slug": "dantu-atstatymas-visi-ant-4",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Klinikos Vadovė",
            "desc": "Specializuojasi sudėtingose implantacijose ir viso žandikaulio reabilitacijoje.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Dantų implantacija", "Visi ant 4 metodika"]
        },
        "faqs": [
            ("Kiek kainuoja Visi ant 4?", "Kaina prasideda nuo 4000-5000 EUR vienam žandikauliui (su laikinu protezu). Galutinė kaina priklauso nuo pasirinktų medžiagų."),
            ("Ar skauda po operacijos?", "Po operacijos būna patinimas ir diskomfortas 3-5 dienas, tačiau skausmas efektyviai valdomas vaistais."),
            ("Kiek laiko tarnauja?", "Implantai dažniausiai tarnauja visą gyvenimą. Protezą gali reikėti atnaujinti po 5-10 metų."),
            ("Ar sunku prižiūrėti?", "Priežiūra panaši į natūralių dantų – valymas šepetėliu, tarpdančių siūlu (specialiu) ir irigatoriumi."),
            ("Ar tinka visiems?", "Tinka daugumai pacientų, net ir tiems, kurie turi mažai kaulo.")
        ]
    },

    # 3. Dantų Gydymas (Terapinis)
    "dantu-gydymas.html": {
        "meta_title": "Terapinis Dantų Gydymas Kaune – Ėduonies Gydymas | Alfadenta",
        "meta_desc": "Profesionalus terapinis dantų gydymas Kaune. Ėduonies šalinimas, plombavimas, estetinis atstatymas. Aukščiausia kokybė. ☎ +370 612 03030",
        "meta_keywords": "dantų gydymas, ėduonies gydymas, terapinis gydymas, dantų plombavimas kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-gydymas",
        "breadcrumb": "Dantų gydymas",
        "h1": "Terapinis Dantų Gydymas – Išsaugokite Savo Natūralius Dantis",
        "intro": "Terapinis gydymas skirtas ėduonies pažeistų dantų atstatymui. Mūsų tikslas – kuo ilgiau išsaugoti jūsų natūralius dantis, naudojant minimaliai invazyvius metodus ir aukščiausios kokybės plombines medžiagas.",
        "benefits": [
            ("Minimaliai invazyvus", "saugome sveiką danties audinį"),
            ("Estetinis vaizdas", "plombos pritaikytos prie danties spalvos"),
            ("Neskausminga", "naudojame efektyvią nejautrą"),
            ("Ilgalaikis rezultatas", "naudojame kokybiškus kompozitus")
        ],
        "photo": "../Photos/nuotraukos naujos/Dantu gydimas.jpg",
        "slug": "dantu-gydymas",
        "doctor": {
            "name": "Kornelija Virbukaitė",
            "role": "Gydytoja Odontologė",
            "desc": "Specializuojasi terapiniame gydyme ir estetiniame plombavime. Kruopštumas ir atidumas detalėms.",
            "photo": "../Photos/Personalas/Kornelija Virbukaite.jpg",
            "specialties": ["Terapinis gydymas", "Estetinis plombavimas"]
        },
        "faqs": [
            ("Kada reikia gydyti danti?", "Kai jaučiate skausmą, jautrumą šalčiui/saldumui, matote skylutę ar tamsią dėmę."),
            ("Ar skauda gręžti?", "Su vietine nejautra skausmo nejaučiate. Gali būti tik vibracijos pojūtis."),
            ("Kiek laiko laiko plomba?", "Kokybiška plomba tarnauja 5-10 metų ar ilgiau, priklausomai nuo burnos higienos."),
            ("Ką daryti jei iškrito plomba?", "Kuo skubiau kreipkitės į gydytoją, kad ėduonis neplistų giliau."),
            ("Kiek kainuoja plombavimas?", "Kaina priklauso nuo plombos dydžio, paprastai nuo 50 iki 100 EUR.")
        ]
    },

    # 4. Dantų Implantų Rūšys
    "dantu-implantu-rusys.html": {
        "meta_title": "Dantų Implantų Rūšys – Straumann, Neodent | Alfadenta Kaunas",
        "meta_desc": "Plačiausias dantų implantų pasirinkimas Kaune. Straumann, Neodent ir kiti pasauliniai lyderiai. Konsultacija ir parinkimas. ☎ +370 612 03030",
        "meta_keywords": "dantų implantai, straumann, neodent, implantų rūšys, implantacija kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-implantu-rusys",
        "breadcrumb": "Implantų rūšys",
        "h1": "Dantų Implantų Rūšys – Tik Geriausi Pasauliniai Gamintojai",
        "intro": "Mes dirbame tik su patikimais, laiko patikrintais implantų gamintojais. Siūlome įvairių kainų lygių sprendimus, tačiau visada garantuojame kokybę ir ilgaamžiškumą. Padėsime išsirinkti jums tinkamiausią variantą.",
        "benefits": [
            ("Premium klasė", "Straumann (Šveicarija)"),
            ("Optimalus santykis", "Neodent ir kiti patikimi gamintojai"),
            ("Visos situacijos", "nuo pavienių implantų iki viso žandikaulio"),
            ("Garantija", "implantams suteikiama viso gyvenimo garantija")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu implantacija.jpg",
        "slug": "dantu-implantu-rusys",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Klinikos Vadovė",
            "desc": "Padės išsirinkti geriausią implantų sistemą pagal jūsų klinikinę situaciją ir biudžetą.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Dantų implantacija", "Protezavimas"]
        },
        "faqs": [
            ("Kuo skiriasi implantai?", "Skiriasi paviršiaus apdorojimu, prigijimo greičiu, jungtimi su protezu ir kaina."),
            ("Kodėl Straumann brangesni?", "Tai pasaulinis lyderis su daugiausiai mokslinių tyrimų ir geriausiais prigijimo rodikliais."),
            ("Ar pigesni implantai blogi?", "Ne, mes naudojame tik sertifikuotus implantus. Pigesni gali turėti mažiau protezavimo galimybių sudėtingais atvejais."),
            ("Kaip išsirinkti?", "Gydytojas įvertins jūsų kaulo būklę ir pasiūlys tinkamiausius variantus konsultacijos metu."),
            ("Ar visi implantai prigyja?", "Šiuolaikinių implantų prigijimo rodiklis yra labai aukštas (96-98%).")
        ]
    },

    # 5. Dantų Laminatės
    "dantu-laminates.html": {
        "meta_title": "Dantų Laminatės (Venyrai) Kaune – Holivudinė Šypsena | Alfadenta",
        "meta_desc": "Keramikos dantų laminatės Kaune. Koreguokite dantų formą, spalvą ir tarpus. Minimali invazija, maksimali estetika. ☎ +370 612 03030",
        "meta_keywords": "dantų laminatės, venyrai, estetinė odontologija, holivudinė šypsena, laminatės kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-laminates",
        "breadcrumb": "Dantų laminatės",
        "h1": "Dantų Laminatės – Tobula Šypsena su Minimalia Intervencija",
        "intro": "Dantų laminatės – tai plonos keramikos plokštelės, tvirtinamos prie danties paviršiaus. Jos leidžia kardinaliai pakeisti šypsenos estetiką: spalvą, formą, uždaryti tarpus, paslėpti nelygumus. Tai populiariausias būdas sukurti „Holivudinę šypseną“.",
        "benefits": [
            ("Maksimali estetika", "atrodo kaip idealūs natūralūs dantys"),
            ("Minimalus šlifavimas", "saugomas danties audinys"),
            ("Nekinta spalva", "keramika netamsėja nuo kavos/vyno"),
            ("Ilgaamžiškumas", "tarnauja 10-15+ metų")
        ],
        "photo": "../Photos/nuotraukos naujos/estetinis plombavimas.jpg",
        "slug": "dantu-laminates",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Estetinės odontologijos specialistė",
            "desc": "Ekspertė estetinio protezavimo srityje. Kuria natūraliai atrodančias, harmonijas šypsenas.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Estetinis protezavimas", "Dantų laminatės"]
        },
        "faqs": [
            ("Ar reikia šlifuoti dantis?", "Dažniausiai reikia minimaliai pašiaušti emalį (0.3-0.5mm), kad laminatė gražiai priglustų."),
            ("Kiek laiko tarnauja laminatės?", "Vidutiniškai 10-15 metų, kartais ir ilgiau, priklausomai nuo priežiūros."),
            ("Ar jos gali nulūžti?", "Keramika yra tvirta, bet trapi. Reikia vengti kramtyti labai kietą maistą, riešutus, nekąsti nagų."),
            ("Kiek vizitų reikia?", "Paprastai 2-3 vizitų: planavimas, paruošimas/atspaudai, ir cementavimas."),
            ("Kokia kaina?", "Vienos laminatės kaina apie 400-600 EUR.")
        ]
    },

    # 6. Dantų Plombavimas (Generic/Repeat of Terapinis? - combine mostly)
    "dantu-plombavimas.html": {
        "meta_title": "Kokybiškas Dantų Plombavimas Kaune | Alfadenta",
        "meta_desc": "Dantų plombavimas Kaune kokybiškomis medžiagomis. Atstatome dantis po ėduonies ar traumų. Neskausminga procedūra. ☎ +370 612 03030",
        "meta_keywords": "dantų plombavimas, plombos, karieso gydymas, dantis skylė",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-plombavimas",
        "breadcrumb": "Plombavimas",
        "h1": "Kokybiškas Dantų Plombavimas – Funkcijos ir Estetikos Atkūrimas",
        "intro": "Dantų plombavimas yra dažniausia odontologinė procedūra. Mes naudojame tvirtas ir estetiškas kompozitines medžiagas, kurios atkurią prarastą danties audinį ir neleidžia infekcijai plisti.",
        "benefits": [
            ("Aukšta kokybė", "naudojame tik sertifikuotas medžiagas"),
            ("Estetika", "plombos spalva pritaikoma idealiai"),
            ("Tvirtumas", "atlaiko kramtymo krūvį"),
            ("Neskausminga", "vietinė nejautra kiekvienu atveju")
        ],
        "photo": "../Photos/nuotraukos naujos/Dantu gydimas.jpg",
        "slug": "dantu-plombavimas",
        "doctor": {
            "name": "Kornelija Virbukaitė",
            "role": "Gydytoja Odontologė",
            "desc": "Kruopščiai atlieka dantų plombavimą, atkurdama natūralią danties formą.",
            "photo": "../Photos/Personalas/Kornelija Virbukaite.jpg",
            "specialties": ["Terapinis gydymas", "Plombavimas"]
        },
        "faqs": [
            ("Kiek laiko trunka plombavimas?", "Apie 30-60 minučių vienam dančiui."),
            ("Ar gali skaudėti po plombavimo?", "Gali būti trumpalaikis jautrumas 1-2 dienas."),
            ("Kada keisti senas plombas?", "Kai jos tampa nesandarios, pakeičia spalvą arba skyla."),
            ("Ar naudojate sidabrines plombas?", "Ne, naudojame tik estetiškas kompozitines (baltas) plombas."),
            ("Kokia garantija?", "Suteikiame garantiją atliktiems darbams.")
        ]
    },

    # 7. Dantų Protezavimas
    "dantu-protezavimas.html": {
        "meta_title": "Dantų Protezavimas Kaune – Vainikėliai, Tiltai | Alfadenta",
        "meta_desc": "Dantų protezavimas Kaune. Cirkonio keramika, metalo keramika, protezavimas ant implantų. Atkurkite kramtymo funkciją. ☎ +370 612 03030",
        "meta_keywords": "dantų protezavimas, dantų karūnėlės, cirkonio keramika, dantų tiltai, protezai kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-protezavimas",
        "breadcrumb": "Dantų protezavimas",
        "h1": "Dantų Protezavimas – Kramtymo Funkcijos ir Estetikos Atkūrimas",
        "intro": "Kai danties neįmanoma atkurti plomba, reikalingas protezavimas. Gaminame aukščiausios kokybės vainikėlius ir tiltus iš cirkonio arba bemetalės keramikos. Tai užtikrina tvirtumą, ilgaamžiškumą ir puikią estetiką.",
        "benefits": [
            ("Tvirtumas", "atlaiko didelį kramtymo krūvį"),
            ("Estetika", "cirkonio keramika atrodo natūraliai"),
            ("Tikslumas", "skaitmeninis atspaudų ėmimas"),
            ("Ilgaamžiškumas", "tarnauja daug metų")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu protezavimas.jpg",
        "slug": "dantu-protezavimas",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Gydytoja Odontologė",
            "desc": "Didelė patirtis sudėtingame dantų protezavime ir sąkandžio kėlime.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Dantų protezavimas", "Estetinė odontologija"]
        },
        "faqs": [
            ("Kada reikia protezuoti?", "Kai dantis stipriai pažeistas, nulūžęs, po šaknų kanalų gydymo arba trūksta danties."),
            ("Kas geriau: cirkonis ar metalo keramika?", "Cirkonis yra estetiškesnis, tvirtesnis ir biologiškai suderinamesnis. Metalo keramika pigesnė, bet mažiau estetiška."),
            ("Kiek laiko trunka gamyba?", "Paprastai 5-10 darbo dienų. Tuo metu esate su laikinais dantimis."),
            ("Ar protezuoti dantys genda?", "Protezuotas dantis po karūnėle gali gesti, jei netinkama higiena. Būtina valyti."),
            ("Kiek kainuoja karūnėlė?", "Cirkonio keramikos karūnėlė kainuoja apie 350-450 EUR.")
        ]
    },

    # 8. Dantų Šalinimas
    "dantu-salinimas.html": {
        "meta_title": "Dantų Šalinimas Kaune – Saugiai ir Be Skausmo | Alfadenta",
        "meta_desc": "Chirurginis dantų šalinimas Kaune. Protinių dantų rovimas, sugedusių dantų šalinimas. Neskausminga procedūra. ☎ +370 612 03030",
        "meta_keywords": "dantų šalinimas, dantų rovimas, protinių dantų šalinimas, chirurginė odontologija kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-salinimas",
        "breadcrumb": "Dantų šalinimas",
        "h1": "Dantų Šalinimas – Saugus ir Neskausmingas Gydymas",
        "intro": "Danties šalinimas yra kraštutinė priemonė, kai danties neįmanoma išgelbėti. Mūsų klinikoje ši procedūra atliekama greitai, profesionaliai ir visiškai be skausmo, naudojant efektyvią nejautrą.",
        "benefits": [
            ("Be skausmo", "visiškas nuskausminimas"),
            ("Greitas gijimas", "minimali trauma audiniams"),
            ("Protinių dantų šalinimas", "sudėtingų atvejų sprendimas"),
            ("Paruošimas implantacijai", "išsaugant kaulą")
        ],
        "photo": "../Photos/Logotipas/alfadenta logotipas.png", # Fallback or Generic
        "slug": "dantu-salinimas",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Klinikos Vadovė",
            "desc": "Atlieka dantų šalinimo procedūras, ruošia burną implantacijai.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Chirurginė odontologija", "Implantacija"]
        },
        "faqs": [
            ("Ar skaudės?", "Procedūros metu – ne. Po procedūros galimas maudimas, kurį numalšinsite vaistais."),
            ("Ką daryti po rovimo?", "Nevalgyti 2 val., neskalauti burnos tą dieną, nerūkyti, vengti karšto maisto."),
            ("Kada reikia šalinti protinius dantis?", "Kai jie dygsta kreivai, remiasi į kitus dantis, sukelia uždegimą ar skausmą."),
            ("Ar galima iškart implantą?", "Taip, dažnai galima atlikti vienmomentę implantaciją iškart po rovimo."),
            ("Kiek kainuoja rovimas?", "Paprastas rovimas ~50-80 EUR, chirurginis/protinis ~100-200 EUR.")
        ]
    },

    # 9. Dantų Tiesinimas Vaikams
    "dantu-tiesinimas-vaikams.html": {
        "meta_title": "Dantų Tiesinimas Vaikams Kaune – Plokštelės, Treineriai | Alfadenta",
        "meta_desc": "Ortodontinis gydymas vaikams Kaune. Dantų plokštelės, treineriai, profilaktika. Ankstyvas sąkandžio koregavimas. ☎ +370 612 03030",
        "meta_keywords": "dantų tiesinimas vaikams, plokštelės, ortodontinės plokštelės, vaikų ortodontas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-tiesinimas-vaikams",
        "breadcrumb": "Tiesinimas vaikams",
        "h1": "Dantų Tiesinimas Vaikams – Laiku Pradėtas Gydymas",
        "intro": "Vaikystė – geriausias laikas formuoti taisyklingą sąkandį. Naudojame nuimamus aparatus (plokšteles, treinerius) ir funkcinius aparatus, kurie nukreipia žandikaulių augimą tinkama linkme ir užtikrina vietą nuolatiniams dantims.",
        "benefits": [
            ("Ankstyva intervencija", "lengvesnis gydymas ateityje"),
            ("Nuimami aparatai", "plokštelės, kurias lengva valyti"),
            ("Žandikaulių plėtimas", "sukuriama vieta dantims"),
            ("Įpročių korekcija", "kvėpavimo, rijimo funkcijos gerinimas")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu tiesinimas.jpg",
        "slug": "dantu-tiesinimas-vaikams",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Ortodontė",
            "desc": "Specializuojasi vaikų ortodontijoje ir ankstyvajame gydyme.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Vaikų ortodontija", "Ortodontinis gydymas"]
        },
        "faqs": [
            ("Kada pirmą kartą pas ortodontą?", "Rekomenduojama apie 6-7 metus, kai išdygsta pirmieji nuolatiniai krūminiai dantys."),
            ("Ar plokštelė trukdo kalbėti?", "Pirmas dienas gali būti sunku, bet vaikas greitai pripranta."),
            ("Kiek laiko nešioti?", "Dažniausiai visą naktį ir kelias valandas dieną. Gydymas trunka 1-2 metus."),
            ("Kiek kainuoja plokštelė?", "Apie 150-250 EUR už vieną žandikaulį."),
            ("Ar skaudės?", "Gali spausti pirmas dienas po aktyvavimo (prisukimo).")
        ]
    },

    # 10. Dantų Tiesinimas (General)
    "dantu-tiesinimas.html": {
        "meta_title": "Dantų Tiesinimas Kaune – Breketai ir Kapos | Alfadenta",
        "meta_desc": "Visapusiškas dantų tiesinimas Kaune. Breketų sistemos, nematomos kapos. Konsultacija pas ortodontę. ☎ +370 612 03030",
        "meta_keywords": "dantų tiesinimas, breketai, kapos, ortodontija kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/dantu-tiesinimas",
        "breadcrumb": "Dantų tiesinimas",
        "h1": "Dantų Tiesinimas – Kelias į Pasitikėjimą Savimi",
        "intro": "Tiesūs dantys – tai ne tik grožis, bet ir sveikata. Kreivi dantys sunkiau valomi, greičiau genda, o netaisyklingas sąkandis kenkia žandikaulio sąnariui. Siūlome efektyviausius tiesinimo būdus pagal jūsų gyvenimo būdą.",
        "benefits": [
            ("Įvairūs metodai", "nuo metalinių breketų iki nematomų kapų"),
            ("Estetika", "keramikiniai breketai"),
            ("Sveikata", "geresnė burnos higiena ir kramtymas"),
            ("Konsultacija", "išsamus gydymo plano sudarymas")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu tiesinimas.jpg",
        "slug": "dantu-tiesinimas",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Ortodontė",
            "desc": "Ilgametė patirtis tiesinant dantis įvairaus amžiaus pacientams.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Ortodontija", "Dantų tiesinimas"]
        },
        "faqs": [
            ("Ką rinktis: breketus ar kapas?", "Kapos yra estetiškesnės ir patogesnės, breketai tinka sudėtingesniems atvejams ir yra pigesni."),
            ("Ar galima tiesinti tik vieną dantį?", "Ortodontija veikia visą lanką, todėl dažniausiai reikia tiesinti visą žandikaulį."),
            ("Kiek trunka gydymas?", "Nuo 6 mėnesių iki 2 metų."),
            ("Ar skauda?", "Diskomfortas jaučiamas tik pradžioje ir po aktyvavimo vizitų.")
        ]
    },

    # 11. Endodontinis Gydymas
    "endodontinis-gydymas.html": {
        "meta_title": "Endodontinis Gydymas Kaune – Kanalų Gydymas | Alfadenta",
        "meta_desc": "Profesionalus dantų šaknų kanalų gydymas Kaune. Mikroskopinė endodontija, moderni įranga, dantų išsaugojimas. ☎ +370 612 03030",
        "meta_keywords": "endodontinis gydymas, kanalų gydymas, dantų šaknų gydymas, endodontas kaunas",
        "og_url": "https://alfadenta.lt/paslaugos/endodontinis-gydymas",
        "breadcrumb": "Endodontinis gydymas",
        "h1": "Endodontinis Gydymas – Danties Išsaugojimas",
        "intro": "Endodontinis gydymas reikalingas, kai infekcija pasiekia danties pulpą (nervą). Tai paskutinė galimybė išsaugoti nuosavą dantį. Naudojame modernią įrangą kanalų valymui ir plombavimui.",
        "benefits": [
            ("Skausmo šalinimas", "pašalinamas uždegimas ir skausmas"),
            ("Danties išsaugojimas", "išvengiama rovimo"),
            ("Moderni diagnostika", "rentgeno kontrolė"),
            ("Kokybiškas plombavimas", "hermetiškas kanalų užpildymas")
        ],
        "photo": "../Photos/Logotipas/alfadenta logotipas.png", # Fallback
        "slug": "endodontinis-gydymas",
        "doctor": {
            "name": "Kornelija Virbukaitė",
            "role": "Gydytoja Odontologė",
            "desc": "Atlieka kokybišką endodontinį gydymą.",
            "photo": "../Photos/Personalas/Kornelija Virbukaite.jpg",
            "specialties": ["Terapinis gydymas", "Endodontija"]
        },
        "faqs": [
            ("Kodėl skauda dantį?", "Dažniausiai dėl nervo uždegimo (pulpito), kurį sukelia gilus ėduonis."),
            ("Kiek vizitų reikia?", "Paprastai 1-2 vizitų."),
            ("Ar skaudės per gydymą?", "Ne, atliekama su nejautra."),
            ("Kas bus po gydymo?", "Dantis gali būti jautresnis kelias dienas. Vėliau jį reikia protezuoti arba plombuoti."),
            ("Kaina?", "Kanalų gydymas kainuoja nuo 100 EUR priklausomai nuo kanalų skaičiaus.")
        ]
    },

    # 12. Implantacijos Eiga
    "implantacijos-eiga.html": {
        "meta_title": "Dantų Implantacijos Eiga – Žingsnis po Žingsnio | Alfadenta",
        "meta_desc": "Sužinokite kaip vyksta dantų implantacija. Konsultacija, operacija, gijimas, protezavimas. Viskas, ką reikia žinoti. ☎ +370 612 03030",
        "meta_keywords": "implantacijos eiga, dantų implantavimas, implantavimo etapai",
        "og_url": "https://alfadenta.lt/paslaugos/implantacijos-eiga",
        "breadcrumb": "Implantacijos eiga",
        "h1": "Dantų Implantacijos Eiga – Žingsnis po Žingsnio",
        "intro": "Dantų implantacija yra procesas, susidedantis iš kelių etapų. Supratimas, kas vyks kiekvieno vizito metu, suteikia ramybės ir pasitikėjimo. Mes lydėsime jus kiekviename žingsnyje.",
        "benefits": [
            ("1. Konsultacija", "ištyrimas ir planavimas"),
            ("2. Implantacija", "trumpa chirurginė procedūra"),
            ("3. Gijimas", "3-6 mėnesiai oseointegracijos"),
            ("4. Protezavimas", "galutinio danties tvirtinimas")
        ],
        "photo": "../Photos/nuotraukos naujos/dantu implantacija.jpg",
        "slug": "implantacijos-eiga",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Klinikos Vadovė",
            "desc": "Detaliai paaiškins visą gydymo eigą ir atsakys į rūpimus klausimus.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Implantacija", "Planavimas"]
        },
        "faqs": [
            ("Kada gausiu dantį?", "Laikinas dantis gali būti dedamas iškart, nuolatinis – po prigijimo (3-6 mėn)."),
            ("Ar reikia nedarbingumo?", "Dažniausiai kitą dieną galima eiti į darbą."),
            ("Ar reikia ruoštis?", "Specialaus pasiruošimo nereikia, tik pavalgyti prieš procedūrą."),
            ("Ką daryti jei skauda?", "Gerti paskirtus vaistus nuo skausmo ir uždegimo.")
        ]
    },

    # 13. Išsami Vaikų Dantų Patikra
    "issami-vaiku-dantu-patikra.html": {
        "meta_title": "Vaikų Dantų Patikra Kaune – Profilaktika | Alfadenta",
        "meta_desc": "Išsami vaikų dantų patikra Kaune. Ėduonies diagnostika, sąkandžio vertinimas, higienos apmokymas. Jauki aplinka vaikams. ☎ +370 612 03030",
        "meta_keywords": "vaikų dantų patikra, vaikų odontologas, dantų tikrinimas vaikams",
        "og_url": "https://alfadenta.lt/paslaugos/issami-vaiku-dantu-patikra",
        "breadcrumb": "Vaikų patikra",
        "h1": "Išsami Vaikų Dantų Patikra – Sveikos Šypsenos Pradžia",
        "intro": "Reguliariai tikrinti vaikų dantis yra būtina, norint išvengti skausmo ir sudėtingo gydymo. Mūsų klinikoje patikra vyksta žaidimo forma, be streso ir baimės. Įvertiname ne tik dantis, bet ir sąkandį bei higienos įgūdžius.",
        "benefits": [
            ("Ėduonies patikra", "ankstyva diagnostika"),
            ("Sąkandžio vertinimas", "ortodontinių problemų prevencija"),
            ("Higienos pamokėlė", "mokome taisyklingai valytis"),
            ("Jauki aplinka", "vaikai jaučiasi saugiai")
        ],
        "photo": "../Photos/Logotipas/alfadenta logotipas.png", # Fallback
        "slug": "issami-vaiku-dantu-patikra",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Gydytoja",
            "desc": "Moka rasti bendrą kalbą su mažaisiais pacientais.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Vaikų odontologija", "Profilaktika"]
        },
        "faqs": [
            ("Kada pirmoji patikra?", "Išdygus pirmajam dantukui arba 1 metų amžiaus."),
            ("Kaip paruošti vaiką?", "Pasakoti apie dantukų skaičiavimą, negąsdinti."),
            ("Ką daryti jei vaikas bijo?", "Mes pradedame nuo adaptacinio vizito, nieko nedarome per prievartą."),
            ("Kiek kainuoja?", "Patikra kainuoja apie 20-30 EUR.")
        ]
    },

    # 14. Nuodugnus Ištyrimas
    "nuodugnus-dantu-bukles-istyrimas.html": {
        "meta_title": "Nuodugnus Dantų Ištyrimas ir Gydymo Planas | Alfadenta",
        "meta_desc": "Išsamus dantų būklės ištyrimas Kaune. Rentgeno diagnostika, gydymo plano sudarymas, konsultacija. Sužinokite tikslią kainą. ☎ +370 612 03030",
        "meta_keywords": "dantų ištyrimas, gydymo planas, odontologo konsultacija, rentgeno nuotrauka",
        "og_url": "https://alfadenta.lt/paslaugos/nuodugnus-dantu-bukles-istyrimas",
        "breadcrumb": "Ištyrimas",
        "h1": "Nuodugnus Dantų Būklės Ištyrimas – Pirmas Žingsnis į Sveikatą",
        "intro": "Prieš pradedant bet kokį gydymą, būtina tiksli diagnostika. Atliekame išsamią burnos apžiūrą, vertiname rentgeno nuotraukas ir sudarome detalų gydymo planą su tiksliomis kainomis ir terminais.",
        "benefits": [
            ("Panoraminė nuotrauka", "matome visą situaciją"),
            ("Gydymo planas", "aiškūs etapai ir kainos"),
            ("Konsultacija", "atsakymai į visus klausimus"),
            ("Kolegialus sprendimas", "tariasi keli specialistai")
        ],
        "photo": "../Photos/Logotipas/alfadenta logotipas.png",
        "slug": "nuodugnus-dantu-bukles-istyrimas",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Klinikos Vadovė",
            "desc": "Sudaro kompleksinius gydymo planus ir koordinuoja gydymą.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Diagnostika", "Gydymo planavimas"]
        },
        "faqs": [
            ("Kiek kainuoja konsultacija?", "Pirminė konsultacija su planu – 30-50 EUR."),
            ("Ar reikia registruotis?", "Taip, būtina išankstinė registracija."),
            ("Kiek trunka?", "Apie 30-45 minutes."),
            ("Ar gausiu planą raštu?", "Taip, atspausdiname arba atsiunčiame el. paštu.")
        ]
    },

    # 15. Periodontologinis Gydymas
    "periodontologinis-gydymas.html": {
        "meta_title": "Periodontito Gydymas Kaune – Dantenų Gydymas | Alfadenta",
        "meta_desc": "Dantenų uždegimo ir periodontito gydymas Kaune. Giluminis valymas, kišenių gydymas, dantenų operacijos. Sustabdykite ligą. ☎ +370 612 03030",
        "meta_keywords": "periodontito gydymas, parodontozė, dantenų gydymas, kraujuoja dantenos",
        "og_url": "https://alfadenta.lt/paslaugos/periodontologinis-gydymas",
        "breadcrumb": "Periodontologija",
        "h1": "Periodontologinis Gydymas – Išsaugokite Dantis",
        "intro": "Periodontitas (paradantozė) yra pagrindinė dantų netekimo priežastis suaugusiems. Laiku diagnozavus ir pradėjus gydymą, ligą galima sustabdyti. Atliekame giluminį valymą, kišenių kiuretažą ir kitas procedūras.",
        "benefits": [
            ("Uždegimo stabdymas", "mažėja kraujavimas"),
            ("Dantų stabilizavimas", "mažėja klibėjimas"),
            ("Blogas kvapas", "šalinama priežastis"),
            ("Profesionali priežiūra", "reguliari stebėsena")
        ],
        "photo": "../Photos/Logotipas/alfadenta logotipas.png",
        "slug": "periodontologinis-gydymas",
        "doctor": {
            "name": "Agnė Širvinskaitė",
            "role": "Burnos higienistė",
            "desc": "Atlieka profesionalią higieną ir padeda valdyti periodontitą.",
            "photo": "../Photos/Personalas/Doktor.png",
            "specialties": ["Burnos higiena", "Periodontologija"]
        },
        "faqs": [
            ("Kodėl kraujuoja dantenos?", "Tai pirmas uždegimo požymis. Būtina higiena."),
            ("Ar periodontitas pagydomas?", "Liga lėtinė, ją galima sustabdyti, bet prarastas kaulas neatauga."),
            ("Ar skauda gydyti?", "Su nuskausminimu – ne."),
            ("Kaip dažnai lankytis?", "Periodonto pacientams – kas 3 mėnesius.")
        ]
    },

    # 16. Tyrimai ir Diagnostika
    "tyrimai-ir-diagnostika.html": {
        "meta_title": "Dantų Diagnostika ir Rentgenas Kaune | Alfadenta",
        "meta_desc": "Tiksli dantų diagnostika. Dentalinės ir panoraminės nuotraukos, klinikinis ištyrimas. Moderni įranga. ☎ +370 612 03030",
        "meta_keywords": "dantų rentgenas, panoraminė nuotrauka, diagnostika, odontologijos klinika",
        "og_url": "https://alfadenta.lt/paslaugos/tyrimai-ir-diagnostika",
        "breadcrumb": "Diagnostika",
        "h1": "Tikslūs Tyrimai ir Diagnostika – Sėkmingo Gydymo Pagrindas",
        "intro": "Be tikslios diagnostikos neįmanomas kokybiškas gydymas. Mūsų klinikoje atliekame visus reikalingus rentgeno tyrimus, vitališkumo testus ir kitus diagnostinius veiksmus, kad nustatytume tikslią problemos priežastį.",
        "benefits": [
            ("Skaitmeninis rentgenas", "maža apšvita, aukšta raiška"),
            ("Greitas rezultatas", "nuotrauka iškart ekrane"),
            ("Tiksli diagnozė", "nematomų problemų nustatymas"),
            ("Saugumas", "moderni ir saugi įranga")
        ],
        "photo": "../Photos/Logotipas/alfadenta logotipas.png",
        "slug": "tyrimai-ir-diagnostika",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Klinikos Vadovė",
            "desc": "Vadovaujasi tiksliais duomenimis priimant gydymo sprendimus.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Diagnostika", "Konsultavimas"]
        },
        "faqs": [
            ("Ar rentgenas kenkia?", "Šiuolaikiniai aparatai skleidžia minimalią dozę, tai saugu."),
            ("Ar galima nėščioms?", "Tik esant būtinybei ir laikantis saugumo priemonių."),
            ("Kiek kainuoja nuotrauka?", "Dentalinė ~10 EUR, panoraminė ~20-30 EUR.")
        ]
    },

    # 17. Vaikų Odontologija (General)
    "vaiku-odontologija.html": {
        "meta_title": "Vaikų Odontologija Kaune – Gydymas Be Baimės | Alfadenta",
        "meta_desc": "Vaikų dantų gydymas Kaune. Pieninių dantų plombavimas, silantai, rovimas. Kantrūs gydytojai, žaisminga aplinka. ☎ +370 612 03030",
        "meta_keywords": "vaikų odontologija, vaikų dantų gydymas, pieniniai dantys, silantai",
        "og_url": "https://alfadenta.lt/paslaugos/vaiku-odontologija",
        "breadcrumb": "Vaikų odontologija",
        "h1": "Vaikų Odontologija – Draugystė su Dantukų Fėja",
        "intro": "Mūsų tikslas – kad vaikas pas odontologą jaustųsi saugiai ir ramiai. Gydymą paverčiame žaidimu, viską paaiškiname suprantama kalba. Gydome pieninius ir nuolatinius dantis, dengiame silantais.",
        "benefits": [
            ("Be skausmo", "švelni nejautra"),
            ("Kantrūs gydytojai", "psichologinis pasiruošimas"),
            ("Silantai", "apsauga nuo ėduonies"),
            ("Dovanėlės", "motyvacija po vizito")
        ],
        "photo": "../Photos/Logotipas/alfadenta logotipas.png",
        "slug": "vaiku-odontologija",
        "doctor": {
            "name": "Sigita Morkuvienė",
            "role": "Gydytoja",
            "desc": "Myli vaikus ir moka su jais bendrauti.",
            "photo": "../Photos/Personalas/Sigita_Morkuviene.jpg",
            "specialties": ["Vaikų odontologija", "Profilaktika"]
        },
        "faqs": [
            ("Ar reikia gydyti pieninius?", "Būtina, nes infekcija gali pakenkti nuolatinių dantų užuomazgoms."),
            ("Kas yra silantai?", "Tai skysta plomba krūminių dantų vagelėms, apsauganti nuo ėduonies."),
            ("Ką daryti jei ištino?", "Skubiai kreiptis į gydytoją, tai infekcija."),
            ("Kiek kainuoja?", "Pieninio danties plombavimas ~40-60 EUR.")
        ]
    }
}

def load_template():
    """Load the template file"""
    template_path = os.path.join(BASE_DIR, TEMPLATE)
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading template: {e}")
        return None

def generate_page(filename, config, template):
    """Generate a single service page"""
    print(f"\nGenerating: {filename}")
    
    # Parse template
    soup = BeautifulSoup(template, 'html.parser')
    
    # Update title
    title = soup.find('title')
    if title:
        title.string = config['meta_title']
    
    # Update meta description
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc:
        meta_desc['content'] = config['meta_desc']
    
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
    
    # Update H1
    h1 = soup.find('h1')
    if h1:
        h1.string = config['h1']
    
    # Update intro text
    intro_p = soup.select_one('section.py-16.bg-gray-50 p.text-lg')
    if intro_p:
        intro_p.string = config['intro']
    
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
    
    # Update hero image
    hero_img = soup.select_one('section.py-16.bg-gray-50 img')
    if hero_img:
        hero_img['src'] = config['photo']
        hero_img['alt'] = config['h1']
    
    # Update booking link
    booking_link = soup.select_one(f'a[href*="booking.html"]')
    if booking_link:
        booking_link['href'] = f"../booking.html?service={config['slug']}"
    
    # Update doctor section
    doctor = config['doctor']
    doctor_name = soup.select_one('h3.text-2xl.font-bold')
    if doctor_name:
        doctor_name.string = f"Gyd. {doctor['name']}"
    
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
    
    # Write to file
    output_path = os.path.join(BASE_DIR, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    print(f"  ✅ Saved: {filename}")
    return True

def main():
    """Main execution"""
    print("=" * 60)
    print("GENERATING REMAINING 17 SERVICE PAGES")
    print("=" * 60)
    
    template = load_template()
    if not template:
        return

    success_count = 0
    for filename, config in SERVICES.items():
        try:
            if generate_page(filename, config, template):
                success_count += 1
        except Exception as e:
            print(f"  ✗ ERROR generating {filename}: {e}")
    
    print("\n" + "=" * 60)
    print(f"COMPLETE: {success_count}/{len(SERVICES)} pages generated successfully")
    print("=" * 60)

if __name__ == "__main__":
    main()
