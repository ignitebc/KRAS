import requests
from Definitions import io_paths
from Helper import fileHelper
from resources import krasConfig

# DOCS Env 필요
def get_rskns_evl_list(session):
    payload = {
            "rsknsEvlYr": "2026",
            "rsknsEvlNo": "",
            "rsknsEvlUnfcCustNo": krasConfig.CUSTNO,    
        }

    data = fileHelper.post_json(session, io_paths.INPUT_URL_RSKNSEVLNO, payload)
    payload = data.get("payload")
    dataList = payload.get("dataList")
    rsknsEvlNo = dataList[1]["rsknsEvlNo"] 
    return rsknsEvlNo

def get_industry_pop_list(session, search_nm):
    payload = {
        "searchNm": search_nm
    }
    data = fileHelper.post_json(session, io_paths.INPUT_URL_INDUSTRY_LIST, payload)
    dataList = data["payload"]["dataList"]
    return dataList

def get_prepare_list(session, rsknsEvlNo):
    payload = {
        "rsknsEvlNo" : rsknsEvlNo
    }

    data = fileHelper.post_json(session, io_paths.INPUT_URL_POST_IA_TPBIZ, payload)
    dataList = data["payload"]["dataList"]
    return dataList

def get_risk_factor(session, rsknsEvlNo, rsknsEvlProcsNo, iaTpbizJobProcsCd):
    payload = {
        "rsKnsEvlNo": rsknsEvlNo,
        "rsKnsEvlProcsNo": rsknsEvlProcsNo,
        "iaTpbizJobProcsCd": iaTpbizJobProcsCd,
    }

    data = fileHelper.post_json(session, io_paths.INPUT_URL_SELECT_RISK_FACTOR, payload)
    dataList = data["payload"]["dataList"]
    return dataList

def get_complete_evaluation_poplist(session, rsknsEvlNo,):
    payload = {
        "rsknsEvlNo": rsknsEvlNo,
        "rsknsEvlProcsNo": "",
    }

    data = fileHelper.post_json(session, io_paths.INPUT_URL_COMPLETE_EVALUATION_POPLIST, payload)
    dataList = data["payload"]["dataList"]
    return dataList

def get_download_excel_file(session, rsknsEvlNo, dataList):
    rsknsEvlMthdCd = dataList[0]["rsknsEvlSeCd"]
    rsknsEvlMthdCdNm = dataList[0]["krasMthNm"]
    
    payload = {
        "excelMergeYn": "N",
        "rsknsEvlMthdCd": rsknsEvlMthdCd,
        "rsknsEvlMthdCdNm" : rsknsEvlMthdCdNm,
        "rsknsEvlNo": rsknsEvlNo,
        "rsknsEvlProcsNo": "",
    }

    content, filename = fileHelper.post_download_excel(session, io_paths.INPUT_URL_EXCEL_DWNLD, payload)
    filename = dataList[0]["rsknsEvlTtlNm"]
    return content, filename
    

