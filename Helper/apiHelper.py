import re

class ApiHelper:
    def __init__(self):
        pass

    def post_json(self, session, url, payload):
        response = session.post(
            url,
            headers={
                **self.config.HEADERS,
                "Content-Type": "application/json"
            },
            json=payload
        )

        if response.status_code == 401:
            self.none_token()

        datalist = response.json()
        return datalist

    def post_download_excel(self, session, url, payload):
        response = session.post(
            url,
            headers={
                **self.config.HEADERS,
                "Content-Type": "application/json;charset=UTF-8",
                "Accept": "*/*",
            },
            json=payload,
            stream=True,
        )

        content = response.content
        content_disposition = response.headers.get("content-disposition", "")
        filename = None
        filename_member = re.search(r'filename="([^"]+)"', content_disposition)
        if filename_member:
            filename = filename_member.group(1)

        return content, filename
