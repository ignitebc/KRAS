import requests
import krasConfig
import sys

URL_INDUSTRY_LIST = "https://portal.kosha.or.kr/api/portal24/bizC/CRSBA01002/selectIndustryPopList"
URL_POST_IA_TPBIZ = "https://portal.kosha.or.kr/api/portal24/bizC/CRSBA01002/selectPostIaTpbiz"

def post_json(session: requests.Session, url: str, payload: dict):
    response = session.post(
        url,
        headers={
            **krasConfig.HEADERS,
            "Content-Type": "application/json"
        },
        json=payload
    )
    if response.status_code == 401:
        print("401, 인증 토큰 만료")
        sys.exit()

    return response.json()

def get_industry_list(session: requests.Session, search_nm: str, page: int = 5):
    data = post_json(session, URL_INDUSTRY_LIST, {"pageIndex": page, "searchNm": search_nm})
    dataList = data["payload"]["dataList"]
    return dataList

def get_prepare_list(session: requests.Session, id_code: str):
    data = post_json(session, URL_POST_IA_TPBIZ, {"iaTpbizSclsfDtlCd": id_code})
    dataList = ["payload"]["dataList"]
    return dataList
