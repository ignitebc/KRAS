# 인증값은 계속 변화하기에 바꿔줘야됨 (AUTHORIZATION, COOKIE)
AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxS003NzAzMzYwMUpYMjc2M1RXSiIsIlJPTEUiOlsiIl0sImlhdCI6MTc2NzgzNTQyOSwiZXhwIjoxNzY3ODM3MzI5fQ.KV5GWm4Po8pjwy6yo2DBpbBC6iWNoce0m2wILHBDnfE"

COOKIE = "_ga=GA1.1.837375537.1767769945; WHATAP=z6caj313s8e1fs; _ga_MBS4F60968=GS2.1.s1767770076$o1$g1$t1767770139$j60$l0$h0; lastAnyidComponent=esign-relay; lastAnyidUserSeCd=01; todayIndexPagePopupToDay0=true; SI=0000000001.Tm7%2BmxJvD4SMFmSyIoP1EPsI42Kf4H3XHc%2FXES1lP%2BvXpJQsGjxSx1FJYK8s5R91yrzaCwaBK6OOlArzKY7zZQ%3D%3Dt95BQapT5t3iqLiqxVlFhE2W0rKP8yW19qRFTrMfYPR6YujaSIh0cRuVPRY%2FC657zJ4A95lu4L%2FKQBkCBMqxPbmtrDZedtrbnKGfwNx0tiZk2N9rvYsPvxUgAa6qHJGX6tfVpjwCj%2FZlw8NimpgO4tzjSs7lNWmCzNaIwPw%2B%2B0MtgntOAVXwiypdp32YZthRmmbrL4r6wA6mwfdPDY7%2FX6QuGBPVgQv7cY7xfprSFVR7HbBXEAuNbscm9iDdIvxjK2qWBbYjcIbe8dP7wrYsxgUOjlV6njzW9UVt9pvyM0hyAxkEToY1TsCic%2FIyIubJWV4JACb5eyXovf%2FHxETbZ1BdbsXMRNKrlZbH4pejS%2BNi6E36Qif6JVo8%2FdFsgN3SfGM2JtNjuvuxMBk33uM%2BuhzKXoN%2BeQ4fwFPpo7aNrLBkFLzVSqhyyUnbovX7kkaHOTB7kCxf4CALOcGufPeNA5hG0gqhpYAnv1FaK6qnzj19apJGQrUPrrMLolaB%2FhR9wzy%2BxiMC%2BC6%2FGFn4Y0StAfF2%2F2eah2OgTE4QMhvl0RN2GTouNnb%2FlQNwZW4PcMcY8pxlqv1LNyyxIiapJjicYHRGFDLD5S7WD8Cs29fC7rbuMwUqnJaYnRxrK24OHF3v; portal24_refreshToken=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxS003NzAzMzYwMUpYMjc2M1RXSiIsImlhdCI6MTc2NzgzNTQyOSwiZXhwIjoxNzY3ODQ2MjI5fQ.pk7XYsTmgo2FF7IAoQMpNMzcZCHk99FTDW7nNQcBCdE; _ga_4KTPXTKSMV=GS2.1.s1767835249$o4$g1$t1767835438$j12$l0$h0"

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