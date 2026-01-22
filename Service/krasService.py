from Core.context import KrasContext


class KrasService(KrasContext):
    def __init__(self):
        super().__init__()

    # DOCS Env 필요
    def get_rskns_evl_list(self, session):
        payload = {
            "rsknsEvlYr": "2026",
            "rsknsEvlNo": "",
            "rsknsEvlUnfcCustNo": self.config.CUSTNO,
        }

        data = self.post_json(session, self.paths.INPUT_URL_RSKNSEVLNO, payload)
        payload = data.get("payload")
        dataList = payload.get("dataList")
        
        if not dataList:
            self.none_kras_evl()

        rsknsEvlNo = dataList[0]["rsknsEvlNo"]
        return rsknsEvlNo

    def get_industry_pop_list(self, session, search_nm):
        payload = {
            "searchNm": search_nm
        }

        data = self.post_json(session, self.paths.INPUT_URL_INDUSTRY_LIST, payload)
        dataList = data["payload"]["dataList"]
        return dataList

    def get_search_nm(self, industry_data):
        dataList = []
        seen = set()

        for row in industry_data:
            search_nm = row.get("tpbizLclsfNm")
            if search_nm in seen:
                continue
            seen.add(search_nm)
            dataList.append(search_nm)

        return dataList

    def get_postiatpbiz(self, session, iaTpbizSclsfDtlCd, iaTpbizSclsfCd):
        payload = {
            "iaTpbizSclsfDtlCd": iaTpbizSclsfDtlCd
        }

        data = self.post_json(session, self.paths.INPUT_URL_POST_IA_TPBIZ, payload)
        dataList = data["payload"]["dataList"]

        if len(dataList) == 0:
            payload = {
                "iaTpbizSclsfCd": iaTpbizSclsfCd
            }
            
            data = self.post_json(session, self.paths.INPUT_URL_POST_IA_TPBIZ, payload)
            dataList = data["payload"]["dataList"]

        if len(dataList) == 0:
            self.write_log("None Data")

        return dataList

    def get_risk_factor(self, session, rsknsEvlNo, rsknsEvlProcsNo, iaTpbizJobProcsCd):
        payload = {
            "rsKnsEvlNo": rsknsEvlNo,
            "rsKnsEvlProcsNo": rsknsEvlProcsNo,
            "iaTpbizJobProcsCd": iaTpbizJobProcsCd,
        }

        data = self.post_json(session, self.paths.INPUT_URL_RISK_FACTOR, payload)
        dataList = data["payload"]["dataList"]
        return dataList

    def get_select_health_measures_poplist(self, session, rsknsEvlNo, rsknsEvlNxsRiskFctrNo, iaTpbizJobProcsSeq):
        page = ((rsknsEvlNxsRiskFctrNo - 1) // 10) + 1
        payload = {
            "page": page,
            "resultPageTotalCnt": 0,
            "rowsPerPage": 10,
            "rsknsEvlNo": rsknsEvlNo,
            "rsknsEvlNxsRiskFctrNo": rsknsEvlNxsRiskFctrNo,
            "rsknsEvlProcsNo": iaTpbizJobProcsSeq
        }

        data = self.post_json(session, self.paths.INPUT_URL_HEALTH_MEASURES_LIST, payload)
        dataList = data["payload"]["dataList"]
        return dataList

    def get_imprvm_after_rsknss(self, session, rsknsEvlNo):
        payload = {
            "rsknsEvlNo" : rsknsEvlNo
        }
        data = self.post_json(session, self.paths.CHECK_IMPRVM_AFTER_RSKNSS, payload)
        dataLists = data["payload"]["dataList"]
        dataList = dataLists["processList"]
        return dataList

    def get_risk_after_improvement(self, session, tab_name, tab_number, rsknsEvlNo):
        payload = {
            "iaTpbizJobProcsCd": tab_name,
            "rsknsEvlNo": rsknsEvlNo,
            "rsknsEvlProcsNo": tab_number,
        }

        data = self.post_json(session, self.paths.CHECK_RISK_AFTER_IMPROVEMENT, payload)

        if data["result"] == "success":
            return True
        else:
            return False

    def get_complete_evaluation_poplist(self, session, rsknsEvlNo):
        payload = {
            "rsknsEvlNo": rsknsEvlNo,
            "rsknsEvlProcsNo": "",
        }

        data = self.post_json(session, self.paths.INPUT_URL_COMPLETE_EVALUATION_POPLIST, payload)
        dataList = data["payload"]["dataList"]
        return dataList

    def get_download_excel_file(self, session, rsknsEvlNo):
        payload = {
            "excelMergeYn": "N",
            "rsknsEvlMthdCd": "02",
            "rsknsEvlMthdCdNm": "빈도·강도법",
            "rsknsEvlNo": rsknsEvlNo,
            "rsknsEvlProcsNo": "",
        }

        content, filename = self.post_download_excel(session, self.paths.INPUT_URL_EXCEL_DWNLD, payload)
        return content, filename

    def get_savebtn_single_postiatpbiz(self, session, saveList, rsknsEvlNo):
        iaTpbizSclsfCd = saveList[0].get("iaTpbizSclsfCd")

        payload = {
            "iaTpbizSclsfCd": iaTpbizSclsfCd,
            "listDelete": "true",
            "rsknsEvlMthdCd": "02",
            "rsknsEvlNo": rsknsEvlNo,
            "saveList": saveList
        }

        data = self.post_json(session, self.paths.INPUT_SAVEURL_POST_IA_TPBIZ, payload)

        if data["result"] == "success":
            return True
        else:
            return False

    def get_savebtn_risk_factor(self, session, saveList):
        payload = {
            "saveList": saveList
        }

        data = self.post_json(session, self.paths.INPUT_SAVEURL_RISK_FACTOR, payload)

        if data["result"] == "success":
            return True
        else:
            return False

    def get_savebtn_health_measures(self, session, saveList):
        payload = {
            "saveList": saveList
        }
        
        data = self.post_json(session, self.paths.INPUT_SAVEURL_HEALTH_MEASURES_POPLIST, payload)

        if data["result"] == "success":
            return True
        else:
            return False
