COUNTERS_URL = "https://www.avito.ru/avito-care/eco-impact"
COUNTERS_INIT_ROUTE = "**/ecoImpact/init"

TIMEOUT_MS = 60000
SELECTOR_CONF = '''(selector) => {
            document.querySelector(selector).scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });
        }'''
COUNTER_CLIP = {
        'x': 530,        
        'y': 250,        
        'width': 226,    
        'height': 226    
    }

WATER_COUNTER_SELECTOR = "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(4)"
CO2_COUNTER_SELECTOR = "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(2)"
ENERGY_COUNTER_SELECTOR = "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(6)"