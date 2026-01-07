

# 인증값은 계속 변화하기에 바꿔줘야됨 (AUTHORIZATION, COOKIE)
AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxS003NzAzMzYwMUpYMjc2M1RXSiIsIlJPTEUiOlsiIl0sImlhdCI6MTc2Nzc2Njk4OCwiZXhwIjoxNzY3NzY4ODg4fQ.V8TM1Uj6s2QIulD4sXnr3yrFpICjlhS-40Gueiz56J8"

COOKIE = "_ga=GA1.1.488229315.1767765772; WHATAP=z1498mmsp7u9np; lastAnyidComponent=esign-relay; lastAnyidUserSeCd=01; SI=0000000001.cQga%2FEHfWBqep36n2tZ80glIunWUw9tH2Mg1lIO3qKGuqkj6LEY7vpzMudfIdXw5DbnQSVR9%2BUVn1LAfHcnyTw%3D%3Dn1Z14L3oEGMnMQur3X1aiovK%2FjWur15bjag6g8vzmjVAd8dmv8W%2FuWDD7lRlD6yHQEWA23x5aAPhij70JqjQmhvYpkv50dQEbus89TJriqD%2FwzVxl%2F2oD%2F6JnugLZaCRD4wiUEn4tkFUCjkSvsixcA1QXmfs1nH774SqZzrokxUYsAlIFM9J1miX%2FcyvH9G3JHSDleuiDtYTNxWikntTsKokCx6SbbZR19LtMC32HaopAXw24803A0IHNnxKRmHIbhQxggFsr2elYsDjNo9NzCkpcP2EWzOnCQKmsTdRseYdxkasgdYjRvF%2F9%2BWb97bfaphPFV%2BH8D5xypVne62hEGePiCHk5CJSEPKv6cFFggWlsT1cLH4J5X7BdlOB%2Bu4YsiANDqdLcu3DnJorH39dWzvse8WgnjYbiJlqkmFWOiqpACwrFfRu9K2ADa5J%2FMyC14k58VzJKPCfxOmhS12d4CiaX9gVsAA%2BDcsK5BsM2E8%2BY7yZuwxVhaOMV3oOSM%2FeyK60n15Ht24N8ikcmlZ6urpaBw4hknzmI3idqIhEflCSyd%2FEiOtygcgK5s8aaHmQINzOLqGoaaByAxHEilXkmLZgpmZW8vuyqKWC8fW%2BWbM0IX6U4sIwTxt5HZo0xrxK; portal24_refreshToken=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxS003NzAzMzYwMUpYMjc2M1RXSiIsImlhdCI6MTc2Nzc2NTkxNiwiZXhwIjoxNzY3Nzc2NzE2fQ.F-XPnhPYhtF7L_apUPLmm-1E5KBCnUO8U_5omXgI7Vo; _ga_4KTPXTKSMV=GS2.1.s1767765771$o1$g1$t1767766992$j54$l0$h0"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://portal.kosha.or.kr",
    "Referer": "https://portal.kosha.or.kr/kras/implement/real/prepare",
    "Authorization": AUTHORIZATION,
    "Cookie": COOKIE,
    "chnlid": "portal24",
}