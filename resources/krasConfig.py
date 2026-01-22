# 인증값은 계속 변화하기에 바꿔줘야됨 (AUTHORIZATION, COOKIE)
AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxS003NzAzMzYwMUpYMjc2M1RXSiIsIlJPTEUiOlsiIl0sImlhdCI6MTc2OTA0MzI0MSwiZXhwIjoxNzY5MDQ1MTQxfQ.tpMjl83X0msADVJuCQzVl_ZoaOGi3u_o6UZ4aEY5uGI"

#위험성평가문서의 값
CUSTNO = "1KM77033601JX2763TWJ"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://portal.kosha.or.kr",
    "Referer": "https://portal.kosha.or.kr/kras/implement/real/prepare",
    "Authorization": AUTHORIZATION,
    # "Cookie": COOKIE,
    "chnlid": "portal24",
}


# COOKIE = "_ga=GA1.1.975349353.1767848381; WHATAP=z683lau3q4o0do; _ga_MBS4F60968=GS2.1.s1767852092$o1$g1$t1767852100$j52$l0$h0; lastAnyidComponent=esign-relay; lastAnyidUserSeCd=01; todayIndexPagePopupToDay1=true; todayIndexPagePopupToDay0=true; _ga_S66869TLEQ=GS2.1.s1768956499$o1$g1$t1768956744$j37$l0$h0; SI=0000000001.dvXmx1LnyKAimsUbkNm8JHAiAW0x22itEfWXKhV26CRnx96Cj%2FiDwYz02OxCSEQgOnYKN8fei%2BPQWP%2F7krxXYQ%3D%3Dt3ESxTnh89tu1xL3BKudKsNMfhHVwu2x%2BIglI9knAqmaPWVmVL%2FkypWTTLAgYeAqWf1nCZPMvmYM948aCGF7D%2Fl9i8ASaTqt8CtFkXVQiIHklgrC%2BmiCV8xIEzakKSQDoOrp008cI05CZy4JNcdto3pdoq%2B4cvX2GHfU%2FJjeJ9MAYXbQ%2BUB0yzr0cfYsVt5yW7w4O7HDzKJu%2By669XsHbgrf%2B24S%2FYXEMYLB47%2FiVntJn4hVZxX8PRfuI0khFDr6rWlsKspGKNSLuWlpkqYHNMPLMR95lEY9awBgnCTmqlCAy4jOKaZGqHyknSuIEP%2BEQWDUrwRaNsZJUi74qiJgi%2BHzzCGjNGg15Awz4zFrPhMcU%2Fp6Mps%2Br%2FCHQmjkBN1zGfUvXmONkeCwDFQvkgWxhh90lg3dxcm6FEKsLvJiSSMeqzAmvs5wqDOMzPPttTAi157TmexV54S5twLYzU3Jkqs5ntYPsznEeDAhV2AUEEhUIRY39IqnPrkkrajHzZnBVUi0qRVHUnWNAyUVLnW9U6yYsngOYih0GQSt3X2KbUsMXH4QFQ9LAJhpUCrRiuisonnSQNajvtqkeeGFO1SaTPjrPRH0HU%2BJ%2FrT1PkfxeQS16VQoZ25H5VEOT4mmwfH%2F; portal24_refreshToken=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxS003NzAzMzYwMUpYMjc2M1RXSiIsImlhdCI6MTc2ODk3MjkxNCwiZXhwIjoxNzY4OTgzNzE0fQ.Mf7TzZmswjZkyDTQVDGH71J5FgQkTYPN7NU8Qk2_eGg; _ga_4KTPXTKSMV=GS2.1.s1768972885$o50$g1$t1768977105$j54$l0$h0"