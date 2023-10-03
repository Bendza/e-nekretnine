WEBSITE_CONFIGS = {
    'halooglasi.com': {
        'start_urls': [
            {'url': 'https://www.halooglasi.com/nekretnine/prodaja-stanova/', 'max_pages': 800},
            {'url': 'https://www.halooglasi.com/nekretnine/izdavanje-stanova/', 'max_pages': 250},
            {'url': 'https://www.halooglasi.com/nekretnine/prodaja-kuca/', 'max_pages': 250},
            {'url': 'https://www.halooglasi.com/nekretnine/izdavanje-kuca/', 'max_pages': 200}
        ],
        'ad_selector': 'h3.product-title a',
        'pagination_pattern': '?page={page_number}'
    },
    'nekretnine.rs': {
        'start_urls':[
            {'url': 'https://www.nekretnine.rs/stambeni-objekti/izdavanje-prodaja/lista/po-stranici/20/', 'max_pages': 200},
        ],
        'ad_selector': 'h2.offer-title a',
        'pagination_pattern': 'po-stranici/20/{page_number}/' 
    }
}
