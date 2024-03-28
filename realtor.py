#Imports for web scraping and pandas DataFrames
import requests
import pandas as pd
import csv
from sqlalchemy import create_engine, types
import mysql.connector

#Output from a website that converts curl commands to Python from the scraped website
cookies = {
    'split': 'n',
    'split_tcv': '184',
    '__vst': '212e4dad-e496-4f18-9d0c-f76eb880948c',
    '__ssn': '78775c1e-15e4-438b-bde0-bca391c6df68',
    '__ssnstarttime': '1709687542',
    '__bot': 'false',
    'permutive-id': 'd1f441f3-ab6e-43fe-85e8-e7573bcd2490',
    '_pbjs_userid_consent_data': '3524755945110770',
    '__split': '82',
    '_ncg_sp_ses.cc72': '*',
    '_ncg_id_': 'bbbe2d2f-cb9a-4141-a87b-60a03aaa611b',
    'AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg': '1',
    '_scid': '153000c1-07c9-4380-8f00-08ad03bf07f9',
    '__gsas': 'ID=9116eeb810b206d7:T=1709687546:RT=1709687546:S=ALNI_MYo5yFirUKpOwS_KPLGlwc65P5Mhw',
    'ab.storage.userId.7cc9d032-9d6d-44cf-a8f5-d276489af322': '%7B%22g%22%3A%22visitor_212e4dad-e496-4f18-9d0c-f76eb880948c%22%2C%22c%22%3A1709687545840%2C%22l%22%3A1709687545847%7D',
    'ab.storage.deviceId.7cc9d032-9d6d-44cf-a8f5-d276489af322': '%7B%22g%22%3A%22d48ef510-6acd-fbd7-c4e5-faf5de4ca2e0%22%2C%22c%22%3A1709687545850%2C%22l%22%3A1709687545850%7D',
    '_gcl_au': '1.1.488018168.1709687546',
    '_tac': 'true~google|not-available',
    '_ta': 'us~1~89df68bc35032d48c293adce8574aa42',
    '_tas': '50f5gb6m4m9',
    '_fbp': 'fb.1.1709687546721.2076224216',
    '_ncg_domain_id_': 'bbbe2d2f-cb9a-4141-a87b-60a03aaa611b.1.1709687544349.1772759544349',
    'pxcts': '99969642-db56-11ee-92a5-b15120a8cdf3',
    '_pxvid': '99968b0e-db56-11ee-92a5-aad25a76c59f',
    's_ecid': 'MCMID%7C28607576725182706914424593807846780748',
    'G_ENABLED_IDPS': 'google',
    '_tt_enable_cookie': '1',
    '_ttp': 'Egy8UYEixoyfcKTkkCCcuhgPj2U',
    '_ncg_g_id_': 'a81630e7-7e1e-426e-8bb4-e62b08b11c19.3.1697208256.1772759544349',
    'AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '-1124106680%7CMCIDTS%7C19789%7CMCMID%7C28607576725182706914424593807846780748%7CMCAAMLH-1710292344%7C7%7CMCAAMB-1710292344%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1709694749s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0',
    'panoramaId_expiry': '1710292351908',
    '_cc_id': '2e2d581f294362e531fda768a13db0da',
    'panoramaId': '7447647ee6df3d13ede25b2a016ebd9563ce1e76e6789b6447824abef444a8c2',
    '_lr_retry_request': 'true',
    '_lr_env_src_ats': 'false',
    '__qca': 'P0-475909307-1709687544807',
    'AMCVS_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '1',
    'AMCV_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg': '-1124106680%7CMCMID%7C28607576725182706914424593807846780748%7CMCIDTS%7C19789%7CMCOPTOUT-1709694751s%7CNONE%7CvVersion%7C5.2.0',
    '_lr_sampling_rate': '100',
    '_sctr': '1%7C1709614800000',
    '_lr_geo_location_state': 'KY',
    '_lr_geo_location': 'US',
    'ajs_anonymous_id': 'eee38735-ac8c-40aa-804e-d6b772254649',
    '_gid': 'GA1.2.2116191769.1709687554',
    'mdLogger': 'false',
    'kampyle_userid': '9f32-53b3-7bb1-608e-1a08-b816-5732-b589',
    'g_state': '{"i_p":1709694763238,"i_l":1}',
    '_iidt': '0L4V8fSW4fu0drTeYRJuP7+kkyy8zC4u01LD+HwAgSB22ZaS8bOR/LpCv1bl04meUw+Fe0AM68hjfw==',
    '_vid_t': 'J3Bjr8VDCoDUaYIQbx+etPQLnX1GErjbi9hKol6hAU/nj+Vkcyu2wj69YSynCtG4N8aKQ9zLA5CfoA==',
    '__fp': 'PuTWTdaidupm2iqSXGvk',
    'criteria': 'sprefix%3D%252Fnewhomecommunities%26area_type%3Dpostal_code%26city%3DMonticello%26pg%3D1%26state_code%3DKY%26state_id%3DKY%26loc%3DMonticello%252C%2520KY%26locSlug%3D42633%26postal_code%3D42633%26county_fips%3D21231%26county_fips_multi%3D21231-21147',
    '_scid_r': '153000c1-07c9-4380-8f00-08ad03bf07f9',
    '_rdt_uuid': '1709687545577.d61dbe27-970e-43aa-a945-0be9cc708dfa',
    '_ncg_sp_id.cc72': 'bbbe2d2f-cb9a-4141-a87b-60a03aaa611b.1709687544.1.1709687665.1709687544.5f60404d-c0e7-4793-9b75-f46e862c9c92',
    'adcloud': '{%22_les_v%22:%22y%2Crealtor.com%2C1709689471%22}',
    '_ga': 'GA1.2.1191411253.1709687544',
    'ab.storage.sessionId.7cc9d032-9d6d-44cf-a8f5-d276489af322': '%7B%22g%22%3A%22fdbeda76-c559-63ff-0924-fe6355a82f33%22%2C%22e%22%3A1709689486300%2C%22c%22%3A1709687545843%2C%22l%22%3A1709687686300%7D',
    'kampyleUserSession': '1709687698364',
    'kampyleUserSessionsCount': '2',
    'kampyleSessionPageCounter': '1',
    'cto_bundle': 'Z52GOl90eWRhMXB1REIwVGlyNFcxNjVGcHRZY0pscHE4TyUyRmwxJTJCMzMlMkZ4JTJGVkxlbU5UVm9oNzVjVVdmRENYNzRiZ0xwdzVrQXZrMk5lN2dLWDRqSUxsd01HWVdYQkNtM0lnM1l2a29hZFNQcUtPUmlKbXF0UVpqU2xUVU9mSFBvc1ZNYm1Fa1pzT3pOb3pnZHh5aVFnanFwQ2h2dyUzRCUzRA',
    '__gads': 'ID=501b39ce9f14f451:T=1709687546:RT=1709687854:S=ALNI_MbNyXcIvb2KaztstVK-srTLlPxzCw',
    '__gpi': 'UID=00000dcfa15a7693:T=1709687546:RT=1709687854:S=ALNI_MZRfFpOkn83XUqIdyzc4iUFHD1Qfw',
    '__eoi': 'ID=f731b2f62de0627d:T=1709687546:RT=1709687854:S=AA-AfjYjh9HY02A0Nv0x6o9SdkgH',
    '_px3': '96f2b3d264201f470b036495c928de6cd6b033b4c4ee48c249d2e58e914e0f1e:hwihQEmwEPVScOMEYxgECpo/BV/v5L53x87eu//OLCvPfnPV03pTw4wIQ1t2IreLXz0hUzpX9F+akRaLQPhelw==:1000:bcQQwEuAci0MSishJYVjOJ3IMJvHdLYir3YtETBErCBVi25IuoZerPSLLOGQnGWGviHDiOWOs/xYyox81onFBkFj+wtA+fJ+JMG2xnui2TpXgvhxLI2933EzclHvG4l9kzJK6fEKKHEReWe1abggMhe5WbRqmhCaYHBgRk/MZ45ONDqJgdJwK7s8uuIGWtPR9kxpYp33Sr2KtAp664VL1sj+GckFldVTtMx6/nFDYRc=',
    '_ga_MS5EHT6J6V': 'GS1.1.1709687549.1.1.1709688140.60.0.0',
    '_gat': '1',
    '_uetsid': '9ceb8430db5611eeac88fd1839927463|1hjp1qa|2|fju|0|1526',
    '_uetvid': '9cec6530db5611ee8d015de3ef067a3a|8k4ntp|1709688137987|5|1|bat.bing.com/p/insights/c/s',
}

headers = {
    'authority': 'www.realtor.com',
    'accept': 'application/json, text/javascript',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'split=n; split_tcv=184; __vst=212e4dad-e496-4f18-9d0c-f76eb880948c; __ssn=78775c1e-15e4-438b-bde0-bca391c6df68; __ssnstarttime=1709687542; __bot=false; permutive-id=d1f441f3-ab6e-43fe-85e8-e7573bcd2490; _pbjs_userid_consent_data=3524755945110770; __split=82; _ncg_sp_ses.cc72=*; _ncg_id_=bbbe2d2f-cb9a-4141-a87b-60a03aaa611b; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; _scid=153000c1-07c9-4380-8f00-08ad03bf07f9; __gsas=ID=9116eeb810b206d7:T=1709687546:RT=1709687546:S=ALNI_MYo5yFirUKpOwS_KPLGlwc65P5Mhw; ab.storage.userId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22visitor_212e4dad-e496-4f18-9d0c-f76eb880948c%22%2C%22c%22%3A1709687545840%2C%22l%22%3A1709687545847%7D; ab.storage.deviceId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22d48ef510-6acd-fbd7-c4e5-faf5de4ca2e0%22%2C%22c%22%3A1709687545850%2C%22l%22%3A1709687545850%7D; _gcl_au=1.1.488018168.1709687546; _tac=true~google|not-available; _ta=us~1~89df68bc35032d48c293adce8574aa42; _tas=50f5gb6m4m9; _fbp=fb.1.1709687546721.2076224216; _ncg_domain_id_=bbbe2d2f-cb9a-4141-a87b-60a03aaa611b.1.1709687544349.1772759544349; pxcts=99969642-db56-11ee-92a5-b15120a8cdf3; _pxvid=99968b0e-db56-11ee-92a5-aad25a76c59f; s_ecid=MCMID%7C28607576725182706914424593807846780748; G_ENABLED_IDPS=google; _tt_enable_cookie=1; _ttp=Egy8UYEixoyfcKTkkCCcuhgPj2U; _ncg_g_id_=a81630e7-7e1e-426e-8bb4-e62b08b11c19.3.1697208256.1772759544349; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCIDTS%7C19789%7CMCMID%7C28607576725182706914424593807846780748%7CMCAAMLH-1710292344%7C7%7CMCAAMB-1710292344%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1709694749s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; panoramaId_expiry=1710292351908; _cc_id=2e2d581f294362e531fda768a13db0da; panoramaId=7447647ee6df3d13ede25b2a016ebd9563ce1e76e6789b6447824abef444a8c2; _lr_retry_request=true; _lr_env_src_ats=false; __qca=P0-475909307-1709687544807; AMCVS_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=1; AMCV_AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-1124106680%7CMCMID%7C28607576725182706914424593807846780748%7CMCIDTS%7C19789%7CMCOPTOUT-1709694751s%7CNONE%7CvVersion%7C5.2.0; _lr_sampling_rate=100; _sctr=1%7C1709614800000; _lr_geo_location_state=KY; _lr_geo_location=US; ajs_anonymous_id=eee38735-ac8c-40aa-804e-d6b772254649; _gid=GA1.2.2116191769.1709687554; mdLogger=false; kampyle_userid=9f32-53b3-7bb1-608e-1a08-b816-5732-b589; g_state={"i_p":1709694763238,"i_l":1}; _iidt=0L4V8fSW4fu0drTeYRJuP7+kkyy8zC4u01LD+HwAgSB22ZaS8bOR/LpCv1bl04meUw+Fe0AM68hjfw==; _vid_t=J3Bjr8VDCoDUaYIQbx+etPQLnX1GErjbi9hKol6hAU/nj+Vkcyu2wj69YSynCtG4N8aKQ9zLA5CfoA==; __fp=PuTWTdaidupm2iqSXGvk; criteria=sprefix%3D%252Fnewhomecommunities%26area_type%3Dpostal_code%26city%3DMonticello%26pg%3D1%26state_code%3DKY%26state_id%3DKY%26loc%3DMonticello%252C%2520KY%26locSlug%3D42633%26postal_code%3D42633%26county_fips%3D21231%26county_fips_multi%3D21231-21147; _scid_r=153000c1-07c9-4380-8f00-08ad03bf07f9; _rdt_uuid=1709687545577.d61dbe27-970e-43aa-a945-0be9cc708dfa; _ncg_sp_id.cc72=bbbe2d2f-cb9a-4141-a87b-60a03aaa611b.1709687544.1.1709687665.1709687544.5f60404d-c0e7-4793-9b75-f46e862c9c92; adcloud={%22_les_v%22:%22y%2Crealtor.com%2C1709689471%22}; _ga=GA1.2.1191411253.1709687544; ab.storage.sessionId.7cc9d032-9d6d-44cf-a8f5-d276489af322=%7B%22g%22%3A%22fdbeda76-c559-63ff-0924-fe6355a82f33%22%2C%22e%22%3A1709689486300%2C%22c%22%3A1709687545843%2C%22l%22%3A1709687686300%7D; kampyleUserSession=1709687698364; kampyleUserSessionsCount=2; kampyleSessionPageCounter=1; cto_bundle=Z52GOl90eWRhMXB1REIwVGlyNFcxNjVGcHRZY0pscHE4TyUyRmwxJTJCMzMlMkZ4JTJGVkxlbU5UVm9oNzVjVVdmRENYNzRiZ0xwdzVrQXZrMk5lN2dLWDRqSUxsd01HWVdYQkNtM0lnM1l2a29hZFNQcUtPUmlKbXF0UVpqU2xUVU9mSFBvc1ZNYm1Fa1pzT3pOb3pnZHh5aVFnanFwQ2h2dyUzRCUzRA; __gads=ID=501b39ce9f14f451:T=1709687546:RT=1709687854:S=ALNI_MbNyXcIvb2KaztstVK-srTLlPxzCw; __gpi=UID=00000dcfa15a7693:T=1709687546:RT=1709687854:S=ALNI_MZRfFpOkn83XUqIdyzc4iUFHD1Qfw; __eoi=ID=f731b2f62de0627d:T=1709687546:RT=1709687854:S=AA-AfjYjh9HY02A0Nv0x6o9SdkgH; _px3=96f2b3d264201f470b036495c928de6cd6b033b4c4ee48c249d2e58e914e0f1e:hwihQEmwEPVScOMEYxgECpo/BV/v5L53x87eu//OLCvPfnPV03pTw4wIQ1t2IreLXz0hUzpX9F+akRaLQPhelw==:1000:bcQQwEuAci0MSishJYVjOJ3IMJvHdLYir3YtETBErCBVi25IuoZerPSLLOGQnGWGviHDiOWOs/xYyox81onFBkFj+wtA+fJ+JMG2xnui2TpXgvhxLI2933EzclHvG4l9kzJK6fEKKHEReWe1abggMhe5WbRqmhCaYHBgRk/MZ45ONDqJgdJwK7s8uuIGWtPR9kxpYp33Sr2KtAp664VL1sj+GckFldVTtMx6/nFDYRc=; _ga_MS5EHT6J6V=GS1.1.1709687549.1.1.1709688140.60.0.0; _gat=1; _uetsid=9ceb8430db5611eeac88fd1839927463|1hjp1qa|2|fju|0|1526; _uetvid=9cec6530db5611ee8d015de3ef067a3a|8k4ntp|1709688137987|5|1|bat.bing.com/p/insights/c/s',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3ODU4NCIsImFwIjoiMTM4NjEyODM5MCIsImlkIjoiYWQwY2Q2MGZmYjU2YTYzYSIsInRyIjoiMmE4Yjc0NjE1ODJhMmMwOTJmM2NiMzFjODc2MGY3MmYiLCJ0aSI6MTcwOTY4ODE0MzA0NCwidGsiOiIxMDIyNjgxIn19',
    'origin': 'https://www.realtor.com',
    'rdc-ab-test-client': 'rdc-search-for-sale',
    'rdc-ab-tests': 'commute_travel_time_variation:v1',
    'referer': 'https://www.realtor.com/realestateandhomes-search/42633/type-single-family-home/pnd-hide',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-2a8b7461582a2c092f3cb31c8760f72f-ad0cd60ffb56a63a-01',
    'tracestate': '1022681@nr=0-1-378584-1386128390-ad0cd60ffb56a63a----1709688143044',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

params = {
    'client_id': 'rdc-search-for-sale-search',
    'schema': 'vesta',
}

json_data = {
    'query': '\n  query ConsumerSearchQuery(\n    $query: HomeSearchCriteria!\n    $limit: Int\n    $offset: Int\n    $search_promotion: SearchPromotionInput\n    $sort: [SearchAPISort]\n    $sort_type: SearchSortType\n    $client_data: JSON\n    $bucket: SearchAPIBucket\n  ) {\n    home_search: home_search(\n      query: $query\n      sort: $sort\n      limit: $limit\n      offset: $offset\n      sort_type: $sort_type\n      client_data: $client_data\n      bucket: $bucket\n      search_promotion: $search_promotion\n    ) {\n      count\n      total\n      search_promotion {\n        name\n        slots\n        promoted_properties {\n          id\n          from_other_page\n        }\n      }\n      mortgage_params {\n        interest_rate\n      }\n      properties: results {\n        property_id\n        list_price\n        search_promotions {\n          name\n          asset_id\n        }\n        primary_photo(https: true) {\n          href\n        }\n        rent_to_own {\n          right_to_purchase\n          rent\n        }\n        listing_id\n        matterport\n        virtual_tours {\n          href\n          type\n        }\n        status\n        products {\n          products\n          brand_name\n        }\n        source {\n          id\n          type\n          spec_id\n          plan_id\n          agents {\n            office_name\n          }\n        }\n        lead_attributes {\n          show_contact_an_agent\n          opcity_lead_attributes {\n            cashback_enabled\n            flip_the_market_enabled\n          }\n          lead_type\n          ready_connect_mortgage {\n            show_contact_a_lender\n            show_veterans_united\n          }\n        }\n        community {\n          description {\n            name\n          }\n          property_id\n          permalink\n          advertisers {\n            office {\n              hours\n              phones {\n                type\n                number\n                primary\n                trackable\n              }\n            }\n          }\n          promotions {\n            description\n            href\n            headline\n          }\n        }\n        permalink\n        price_reduced_amount\n        description {\n          name\n          beds\n          baths_consolidated\n          sqft\n          lot_sqft\n          baths_max\n          baths_min\n          beds_min\n          beds_max\n          sqft_min\n          sqft_max\n          type\n          sub_type\n          sold_price\n          sold_date\n        }\n        location {\n          street_view_url\n          address {\n            line\n            postal_code\n            state\n            state_code\n            city\n            coordinate {\n              lat\n              lon\n            }\n          }\n          county {\n            name\n            fips_code\n          }\n        }\n        open_houses {\n          start_date\n          end_date\n        }\n        branding {\n          type\n          name\n          photo\n        }\n        flags {\n          is_coming_soon\n          is_new_listing(days: 14)\n          is_price_reduced(days: 30)\n          is_foreclosure\n          is_new_construction\n          is_pending\n          is_contingent\n        }\n        list_date\n        photos(limit: 2, https: true) {\n          href\n        }\n        advertisers {\n          type\n          builder {\n            name\n            href\n            logo\n          }\n        }\n      }\n    }\n  }\n',
    'variables': {
        'geoSupportedSlug': '42633',
        'query': {
            'unique': True,
            'status': [
                'for_sale',
                'ready_to_build',
            ],
            'search_location': {
                'location': '42633, Monticello, KY',
            },
            'type': [
                'single_family',
            ],
            'pending': False,
            'contingent': False,
        },
        'client_data': {
            'device_data': {
                'device_type': 'desktop',
            },
        },
        'limit': 42,
        'offset': 0,
        'sort_type': 'relevant',
        'search_promotion': {
            'name': 'POSTALCODE',
            'slots': [
                5,
                6,
                7,
                8,
            ],
            'promoted_properties': [
                [],
            ],
        },
    },
    'isClient': True,
    'visitor_id': '212e4dad-e496-4f18-9d0c-f76eb880948c',
}

response = requests.post(
    'https://www.realtor.com/api/v1/rdc_search_srp',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

realtor_response = requests.put('https://www.realtor.com/realestateandhomes-search/42633/type-single-family-home/pnd-hide', cookies=cookies, headers=headers, json=json_data)

results_json = response.json()

result_items = results_json['data']['home_search']['properties']

#Arrays for the relevant columns to be made
address = []
price = []
beds = []
baths = []
area = []
propertyType = []
url = []
measurement = []

#For loop to fill each array
for result in result_items:
  address.append(result['location']['address']['line'])
  price.append(result['list_price'])
  beds.append(result['description']['beds'])
  baths.append(result['description']['baths_consolidated'])
  area.append(result['description']['sqft'])
  propertyType.append((result['description']['type']).upper())
  url.append('https://www.realtor.com/realestateandhomes-detail/' + result['permalink'] + '?from=srp-list-card')
  measurement.append("sqft")

#Creating a DataFrame 
realtor_houses_df = pd.DataFrame({'Address':address, 'Price':price, 'Beds':beds, 'Baths':baths, 'Area':area, 'Measurement':measurement, 'Property Type':propertyType, 'URL':url})

#Saving the DataFrame to a .csv
realtor_houses_df.to_csv('realtor_homes.csv', index=False)

#connecting to SQL
host = 'localhost'
user = 'root'
password = ''
database = 'properties'

#creating .csv file
csv_file_path = 'realtor_homes.csv'

#creating/updating the realtor_homes table
table_name = 'realtor_homes'

df = pd.read_csv(csv_file_path)

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

df.to_sql(name=table_name, con=engine,if_exists='replace', index=False)

engine.dispose()

#output upon successful table creation/update
print("realtor_homes has been made/replaced")