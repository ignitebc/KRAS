import json
import requests
import KRASConfig as cf


# 업종별
def select_industry_pop_list():
    url = "https://portal.kosha.or.kr/api/portal24/bizC/CRSBA01002/selectIndustryPopList"

    response = requests.post(
        url,
        headers={**cf.HEADERS, "Content-Type": "application/json"},
        json= {"pageIndex": 1}
    )
    # print("status:", response.status_code)
    # print("content-type:", response.headers.get("content-type"))

    data = response.json()  
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    select_industry_pop_list()


