WEBSITE_CONFIGS = {
    'halooglasi.com': {
        'start_urls': [
            {'url': 'https://www.halooglasi.com/nekretnine/prodaja-stanova/', 'max_pages': 780},
            {'url': 'https://www.halooglasi.com/nekretnine/izdavanje-stanova/', 'max_pages': 220},
            {'url': 'https://www.halooglasi.com/nekretnine/prodaja-kuca/', 'max_pages': 180},
            {'url': 'https://www.halooglasi.com/nekretnine/izdavanje-kuca/', 'max_pages': 25}
        ],
        'ad_selector': 'h3.product-title a',
        'pagination_pattern': '?page={page_number}'
    },
    'nekretnine.rs': {
        'start_urls':[{'url': 'https://www.nekretnine.rs/stambeni-objekti/izdavanje-prodaja/lista/po-stranici/20/', 'max_pages':210}],
        'ad_selector': 'h2.offer-title a',
        'pagination_pattern': 'po-stranici/20/{page_number}/' 
    },
    'oglasi.rs': {
        'start_urls': [{'url': 'https://www.oglasi.rs/nekretnine/prodaja-stanova', 'max_pages': 770},
                       {'url': 'https://www.oglasi.rs/nekretnine/izdavanje-stanova', 'max_pages': 50},
                       {'url': 'https://www.oglasi.rs/nekretnine/prodaja-kuca', 'max_pages': 160},
                       {'url': 'https://www.oglasi.rs/nekretnine/izdavanje-kuca', 'max_pages': 10}],
        'ad_selector': 'a.fpogl-list-title',
        'pagination_pattern': '?i=96&p={page_number}'
    },
    'beogradskioglasi.com': {
        'start_urls': [{'url': 'https://www.beogradskioglasi.com/oglasi/nekretnine/', 'max_pages': 130}],
        'ad_selector': 'div.classified a',
        'pagination_pattern': '?page={page_number}'
    },
    '4zida.rs': {
        'start_urls': [{'url': 'https://www.4zida.rs/prodaja-stanova', 'max_pages': 101},
                       {'url': 'https://www.4zida.rs/izdavanje-stanova', 'max_pages': 101},
                       {'url': 'https://www.4zida.rs/prodaja-kuca', 'max_pages': 101},
                       {'url': 'https://www.4zida.rs/izdavanje-kuca', 'max_pages': 52}],
        'ad_selector': 'app-link a#internal',
        'pagination_pattern': '?strana={page_number}'
    },
    'sasomange.rs': {
        'start_urls': [{'url': 'https://sasomange.rs/c/stanovi-prodaja', 'max_pages': 870},
                       {'url': 'https://sasomange.rs/c/stanovi-iznajmljivanje', 'max_pages': 200},
                       {'url': 'https://sasomange.rs/c/kuce-prodaja', 'max_pages': 230},
                       {'url': 'https://sasomange.rs/c/kuce-iznajmljivanje', 'max_pages': 20}],
        'ad_selector': 'a.product-link',
        'pagination_pattern': '?currentPage={page_number}'
    },
    'nadjidom.com': {
        'start_urls': [{'url': 'https://www.nadjidom.com/sr/nekretnine', 'max_pages': 2260}],
        'ad_selector': 'a.card-img-top',
        'pagination_pattern': '&offset={offset}'
    },
}
