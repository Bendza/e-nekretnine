WEBSITE_CONFIGS = {
    'halooglasi.com': {
        'start_urls': [
            {'url': 'https://www.halooglasi.com/nekretnine/prodaja-stanova/', 'max_pages': 780},
            {'url': 'https://www.halooglasi.com/nekretnine/izdavanje-stanova/', 'max_pages': 220},
            {'url': 'https://www.halooglasi.com/nekretnine/prodaja-kuca/', 'max_pages': 180},
            {'url': 'https://www.halooglasi.com/nekretnine/izdavanje-kuca/', 'max_pages': 25}
        ],
        'ad_selector': "//div[@class='product-item product-list-item Premium real-estates my-product-placeholder']",
        'pagination_pattern': '?page={page_number}',
        'fields': {
            "url": ".//h3[@class='product-title']/a/@href",
            "title": ".//h3[@class='product-title']/a/text()",
            "price": ".//div[@class='central-feature']/span/i/text()",
            "city": ".//ul[@class='subtitle-places']/li[1]/text()",
            "street": ".//ul[@class='subtitle-places']/li[last()]/text()",
            "surface": ".//ul[@class='product-features ']/li[1]/div/text()",
            "date": ".//span[@class='publish-date']/text()",
            "image": ".//a[@class='a-images']/img/@src",
        }
    },
    'nekretnine.rs': {
        'start_urls': [
            {'url': 'https://www.nekretnine.rs/stambeni-objekti/izdavanje-prodaja/lista/po-stranici/20/', 'max_pages': 210},
        ],
        'ad_selector': "//div[@class='row offer']",  # XPath selector for the ad container
        'fields': {
            "url": ".//h2[@class='offer-title text-truncate w-100']/a/@href",
            "title": ".//h2[@class='offer-title text-truncate w-100']/a/text()",
            "price": ".//p[@class='offer-price']/span/text()",
            "city": "substring-before(substring-after(.//p[contains(@class, 'offer-location text-truncate')]/text(), ','), ',')",
            "street": "substring-before(.//p[contains(@class, 'offer-location text-truncate')]/text(), ',')",
            "surface": ".//div[@class='text-right']/p[@class='offer-price offer-price--invert']/span/text()",
            "date": "substring-before(.//div[contains(@class, 'offer-meta-info offer-adress')]/text(), ' |')",
            "image": ".//img[contains(@class, 'img-fluid')]/@data-src",
        },
    },
    'oglasi.rs': {
        'start_urls': [{'url': 'https://www.oglasi.rs/nekretnine/prodaja-stanova', 'max_pages': 770},
                       {'url': 'https://www.oglasi.rs/nekretnine/izdavanje-stanova', 'max_pages': 50},
                       {'url': 'https://www.oglasi.rs/nekretnine/prodaja-kuca', 'max_pages': 160},
                       {'url': 'https://www.oglasi.rs/nekretnine/izdavanje-kuca', 'max_pages': 10}],
        'ad_selector': "//div[contains(@class, 'fpogl-holder advert_list_item_normalan')]",
        'pagination_pattern': '?i=96&p={page_number}',
        'fields': {
            "url": ".//a[@class='fpogl-list-title']/@href",
            "title": ".//a[@class='fpogl-list-title']/h2/text()",
            "price": ".//span[@class='text-price']/strong/text()",
            "city": ".//a[@itemprop='category'][contains(@href, '/nekretnine/prodaja-stanova/')]/text()",
            "street": ".//a[@itemprop='category'][contains(@href, '/nekretnine/prodaja-stanova/')][last()]/text()",
            "surface": ".//div[contains(text(), 'Kvadratura:')]/strong/text()",
            "date": "normalize-space(.//time/text())",
            "image": ".//a[@class='fpogl-list-image']/img/@src",
        }
    },
    'beogradskioglasi.com': {
        'start_urls': [
            {'url': 'https://www.beogradskioglasi.com/oglasi/nekretnine/', 'max_pages': 130}
        ],
        'ad_selector': "//div[@class='classified']",
        'pagination_pattern': '?page={page_number}',
        'fields': {
            "url": ".//a/@href",
            "title": ".//div[@class='title']/h3/text()",
            "image": ".//div[@class='lfloat gallery-img-bg smallimg sl-image']/img/@src",
            "price": ".//div[@class='fbavr price sl-price']/text()",
            "city": "substring-before(.//div[@class='sl-loc']/text(), ',')",
            "street": "substring-after(substring-after(.//div[@class='sl-loc']/text(), ','), ',')",
            'date': ".//div[@class='small-light']/text()"
        }
    },
    '4zida.rs': {
        'start_urls': [{'url': 'https://www.4zida.rs/prodaja-stanova', 'max_pages': 101},
                       {'url': 'https://www.4zida.rs/izdavanje-stanova', 'max_pages': 101},
                       {'url': 'https://www.4zida.rs/prodaja-kuca', 'max_pages': 101},
                       {'url': 'https://www.4zida.rs/izdavanje-kuca', 'max_pages': 52}],
            'ad_selector': "//app-ad-search-preview-compact/div[contains(@class, 'border-2')]",
            'pagination_pattern': '?strana={page_number}',
            'fields': {
                "url": ".//a[@id='internal']/@href",
                "title": ".//div[contains(@class, 'font-medium')]/div[1]/text()",
                "price": ".//span[contains(@class, 'text-xl')]/text()",
                "city": "normalize-space(substring-after(substring-after(.//div[contains(@class, 'font-medium')]/div[2]/text(), ','), ','))",
                "street": "substring-before(.//div[contains(@class, 'font-medium')]/div[2]/text(), ',')",
                "surface": ".//div[contains(@class, 'meta-labels')]/strong[1]/text()",
                'image': ".//picture/source[@srcset][1]/@srcset",
            },
    },
    'sasomange.rs': {
        'start_urls': [{'url': 'https://sasomange.rs/c/stanovi-prodaja', 'max_pages': 870},
                       {'url': 'https://sasomange.rs/c/stanovi-iznajmljivanje', 'max_pages': 200},
                       {'url': 'https://sasomange.rs/c/kuce-prodaja', 'max_pages': 230},
                       {'url': 'https://sasomange.rs/c/kuce-iznajmljivanje', 'max_pages': 20}],
        'ad_selector': "//li[contains(@class, 'product-single-item')]",
        'pagination_pattern': '?currentPage={page_number}',
        'fields': {
            "url": ".//a[@class='product-link']/@href",
            "title": ".//h2[@class='product-title']/text()",
            "price": ".//p[@class='product-price separate']/text()",
            "city": "substring-before(.//div[@class='pin-item']/span/text(), ',')",
            "street": ".//h2[@class='product-title']/text()",
            "surface": ".//ul[@class='highlighted-attributes']/li[1]/span[1]/text()",
            "date": ".//time[@class='pin-item']/span/text()",
            "image": ".//img[@class='product-img']/@src",
        },
    },
    'nadjidom.com': {
        'start_urls': [{'url': 'https://www.nadjidom.com/sr/nekretnine', 'max_pages': 2260}],
        'ad_selector': ".//div[contains(@class, 'estate-loop')]",
        'pagination_pattern': '&offset={offset}',
        'fields': {
            'url': './/a[@class="card-img-top position-relative"]/@href',
            'title': './/a[@class="nav-link stretched-link ad-title"]/text()',
            'price': './/div[@class="fw-bold fs-3 h6 mb-0 w-50 nowrap"]/div[1]/text()',
            'surface': './/ul[@class="parameters mb-2 fs-sm"]/li[@class="param surface"]/text()',
            'city': 'substring-before(.//p[@class="mb-2 fs-sm"]/i/following-sibling::text(), ",")',
            'image': './/img[@class="list-image"]/@src',
            'date': './/span[@class="d-inline-block fs-sm text-muted flex-grow-1"]/text()'
        }
    },
}
