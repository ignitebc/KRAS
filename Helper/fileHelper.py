import sys
import re
import resources.krasConfig as krasConfig
from Definitions import io_paths
import requests
import os

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
        
    datalist = response.json()
    return datalist

def post_download_excel(session: requests.Session, url: str, payload: dict):
    response = session.post(
        url,
        headers={
            **krasConfig.HEADERS,
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "*/*",
        },
        json=payload,
        stream=True,
    )

    content = response.content

    cd = response.headers.get("content-disposition", "")
    filename = None
    m = re.search(r'filename="([^"]+)"', cd)
    if m:
        filename = m.group(1)

    return content, filename


def save_bytes(content, out_path):
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(content)


def outpath_complete_eval_excel(filename):
    os.makedirs(io_paths.OUTPATH_EXCEL_DWNLD, exist_ok=True)
    return os.path.join(io_paths.OUTPATH_EXCEL_DWNLD, filename)