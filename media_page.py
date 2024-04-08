import requests

cookies = {
    '_yasc': 'Cf3jfKfpQ5ab0zJs9fHba4boHQ7xsUZ7Ho28RHXWufh0D85UfD8tPhMljhBwJr5w1A==',
    'i': '2mBz6+FauH4/HWlvRM8Tb2ptD34p98Fy1KqG6lANY0OrqrzHzUc76teL6TzuGcvrON9vEgba6GxZLrga87NNUfU2Z6o=',
    'yandexuid': '7405758471712580760',
    'yashr': '7810803961712564389',
    'yandex_login': '',
    'mda2_beacon': '1712580760153',
    'no-re-reg-required': '1',
    '_ym_uid': '1712564395564125624',
    '_ym_d': '1712580761',
    'cycada': 'iFdEgyfMJtKwEghDp85YOElFmph8gVTBSCt0akD5C3w=',
    '_ym_isad': '2',
    'tc': '11',
    'my_perpages': '^%^5B^%^5D',
    'mobile': 'no',
    'mda_exp_enabled': '1',
    'result_type': 'full',
    'desktop_session_key': '53e8eb140162a0b34d21762b588963a6b4c068a8d776d3f30d841ad689bc9b8821365dc507b27cf01eb2e6199aab49d1b493d2e12aef2292931c15294ab97857a447023ab33598c617704f41a0b980821a49906c9613084594654b0a5d34936e',
    'desktop_session_key.sig': 'mmQYMG3pfyt8cRSC3DB-qrHJ5eQ',
    'gdpr': '0',
    'PHPSESSID': 'e79ae51d0e4ae04a00061a2c37da1b45',
    'user_country': 'ru',
    'yandex_gid': '51',
    'ya_sess_id': 'noauth:1712580760',
    'sessar': '1.1188.CiDTlot-xKgcIPIXOo8dZPAWjK23tuiaQDztZ8uEm3P0dQ.XG2zZ4hu06RG01RFlM0t7v7XBUNDwXMpidzng4uT78s',
    'ys': 'c_chck.1639545136',
    'sso_status': 'sso.passport.yandex.ru:synchronized',
    '_csrf': 'Ab6ehn9QIA3DeYRHdyCLtuO1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': '_yasc=Cf3jfKfpQ5ab0zJs9fHba4boHQ7xsUZ7Ho28RHXWufh0D85UfD8tPhMljhBwJr5w1A==; i=2mBz6+FauH4/HWlvRM8Tb2ptD34p98Fy1KqG6lANY0OrqrzHzUc76teL6TzuGcvrON9vEgba6GxZLrga87NNUfU2Z6o=; yandexuid=7405758471712580760; yashr=7810803961712564389; yandex_login=; mda2_beacon=1712580760153; no-re-reg-required=1; _ym_uid=1712564395564125624; _ym_d=1712580761; cycada=iFdEgyfMJtKwEghDp85YOElFmph8gVTBSCt0akD5C3w=; _ym_isad=2; tc=11; my_perpages=^%^5B^%^5D; mobile=no; mda_exp_enabled=1; result_type=full; desktop_session_key=53e8eb140162a0b34d21762b588963a6b4c068a8d776d3f30d841ad689bc9b8821365dc507b27cf01eb2e6199aab49d1b493d2e12aef2292931c15294ab97857a447023ab33598c617704f41a0b980821a49906c9613084594654b0a5d34936e; desktop_session_key.sig=mmQYMG3pfyt8cRSC3DB-qrHJ5eQ; gdpr=0; PHPSESSID=e79ae51d0e4ae04a00061a2c37da1b45; user_country=ru; yandex_gid=51; ya_sess_id=noauth:1712580760; sessar=1.1188.CiDTlot-xKgcIPIXOo8dZPAWjK23tuiaQDztZ8uEm3P0dQ.XG2zZ4hu06RG01RFlM0t7v7XBUNDwXMpidzng4uT78s; ys=c_chck.1639545136; sso_status=sso.passport.yandex.ru:synchronized; _csrf=Ab6ehn9QIA3DeYRHdyCLtuO1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
#name  = 5212441
def select(name):
    response = requests.get('https://www.kinopoisk.ru/film/' + str(name), cookies=cookies, headers=headers)

    with open('media_page.html', "w", encoding="utf-8") as f:
        f.write(response.text)
    return response

def write_to_html(name):
    with open('media_page.html', "w", encoding="utf-8") as file:
        file.write(select(name).text)

#write_to_html("404900")