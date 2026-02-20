from bs4 import BeautifulSoup, NavigableString

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')
grid = soup.find(id='services-grid')

cards = grid.find_all('div', class_='service-card', recursive=False)

card_map = {}
for card in cards:
    h3 = card.find('h3')
    if h3:
        title = h3.get_text(strip=True)
        card_map[title] = card

# All titles in current order, except "Dantų sveikatos pažyma" goes last
all_titles = list(card_map.keys())
target = 'Dantų sveikatos pažyma'
all_titles = [t for t in all_titles if t != target] + [target]

for card in cards:
    card.extract()
for child in list(grid.children):
    if isinstance(child, NavigableString):
        child.extract()

for title in all_titles:
    if title in card_map:
        grid.append(card_map[title])

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Done! Last card:", all_titles[-1])
