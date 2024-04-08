# берем первый фильм/сериал
import requests

cookies = {
    '_yasc': 'K4TVg6Nk80fGPGENhuncKjeP9EOAWfeUjM4JDi/GMT/IzVE82sz7FHvvIolmNavS7Q==',
    'i': 'BF6i6xJcysKhJWwAUVdExtrST7IS+F8VhJal816kDSuxUQUsaelHRVVEhAJST0k/dXFnAmT63xkyFL3v+IZpkYqYG2U=',
    'yandexuid': '1329765431712564390',
    'yashr': '7810803961712564389',
    'ya_sess_id': 'noauth:1712564390',
    'sessar': '1.1188.CiCUOx9xujWiTBep8strQBsvNQiazOqqeepAX-rJPAGVQw.hENZ3Am82aFzO86kqmmaXZQJiN6EyNvPj6lcFRkJClE',
    'yandex_login': '',
    'ys': 'c_chck.1015831780',
    'mda2_beacon': '1712564390964',
    'sso_status': 'sso.passport.yandex.ru:synchronized_no_beacon',
    'no-re-reg-required': '1',
    'desktop_session_key': 'f3f5e2e632403686aea5b62f4bc841b8eb2ea38242aaef1412d529bd219688454de60fb0ecaf3f466df20e915dbc0aebbc3184491a9e296e068d6b7a4317bf504359502a000ad87669a6a3fed12ff3534760f5c32ec064b2e82b05261a8d310b',
    'desktop_session_key.sig': 'Otrf79eEtq7_UFYAW8t0jm00EcE',
    'gdpr': '0',
    '_ym_uid': '1712564395564125624',
    '_ym_d': '1712565590',
    'cycada': 'NbzPKJyvY+R7U1K9gDofaklFmph8gVTBSCt0akD5C3w=',
    '_ym_isad': '2',
    'PHPSESSID': 'a82d2d1756873d7bd56dadd14fea56fe',
    'user_country': 'ru',
    'yandex_gid': '51',
    'tc': '11',
    'my_perpages': '^%^5B^%^5D',
    '_csrf_csrf_token': 'JeHmtsValmzXDleWSkd3jbg5bjduk7k0vRqwmRWTKGs',
    'mobile': 'no',
    'mda_exp_enabled': '1',
    'yandex_plus_metrika_cookie': 'true',
    '_ym_visorc': 'b',
    'user-geo-region-id': '51',
    'user-geo-country-id': '2',
    '_csrf': 's0NXkj7pIqspRsCmRMR30IP-',
    'sgst': 'searchRequest-^%^D1^%^82^%^D0^%^BE^%^D0^%^BF^%^D0^%^B8',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.kinopoisk.ru/film/1050961/',
    # 'Cookie': '_yasc=K4TVg6Nk80fGPGENhuncKjeP9EOAWfeUjM4JDi/GMT/IzVE82sz7FHvvIolmNavS7Q==; i=BF6i6xJcysKhJWwAUVdExtrST7IS+F8VhJal816kDSuxUQUsaelHRVVEhAJST0k/dXFnAmT63xkyFL3v+IZpkYqYG2U=; yandexuid=1329765431712564390; yashr=7810803961712564389; ya_sess_id=noauth:1712564390; sessar=1.1188.CiCUOx9xujWiTBep8strQBsvNQiazOqqeepAX-rJPAGVQw.hENZ3Am82aFzO86kqmmaXZQJiN6EyNvPj6lcFRkJClE; yandex_login=; ys=c_chck.1015831780; mda2_beacon=1712564390964; sso_status=sso.passport.yandex.ru:synchronized_no_beacon; no-re-reg-required=1; desktop_session_key=f3f5e2e632403686aea5b62f4bc841b8eb2ea38242aaef1412d529bd219688454de60fb0ecaf3f466df20e915dbc0aebbc3184491a9e296e068d6b7a4317bf504359502a000ad87669a6a3fed12ff3534760f5c32ec064b2e82b05261a8d310b; desktop_session_key.sig=Otrf79eEtq7_UFYAW8t0jm00EcE; gdpr=0; _ym_uid=1712564395564125624; _ym_d=1712565590; cycada=NbzPKJyvY+R7U1K9gDofaklFmph8gVTBSCt0akD5C3w=; _ym_isad=2; PHPSESSID=a82d2d1756873d7bd56dadd14fea56fe; user_country=ru; yandex_gid=51; tc=11; my_perpages=^%^5B^%^5D; _csrf_csrf_token=JeHmtsValmzXDleWSkd3jbg5bjduk7k0vRqwmRWTKGs; mobile=no; mda_exp_enabled=1; yandex_plus_metrika_cookie=true; _ym_visorc=b; user-geo-region-id=51; user-geo-country-id=2; _csrf=s0NXkj7pIqspRsCmRMR30IP-; sgst=searchRequest-^%^D1^%^82^%^D0^%^BE^%^D0^%^BF^%^D0^%^B8',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
def select(name):
    response = requests.get(
        #'https://www.kinopoisk.ru/index.php?kp_query=^%^D1^%^82^%^D0^%^BE^%^D0^%^BF^%^D0^%^B8',
        #'https://www.kinopoisk.ru/index.php?kp_query=топи',
        'https://www.kinopoisk.ru/index.php?kp_query=' + str(name),
        cookies=cookies,
        headers=headers,
    )
    return response

def write_to_html(name):
    with open('search_media.html', "w", encoding="utf-8") as file:
        file.write(select(name).text)

