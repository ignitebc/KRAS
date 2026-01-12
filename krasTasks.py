import requests
from Definitions import io_paths, category
from Helper import csvHelper, fileHelper
import Service.krasService as krasService

# rsknsEvlNo 추출
def select_rskns_evl_list(session):
    rsknsEvlNo = krasService.get_rskns_evl_list(session)
    return rsknsEvlNo

# 업종별 
def select_industry_pop_list(session):
    industry_list = krasService.get_industry_pop_list(session, search_nm="")
    csvHelper.write_csv(industry_list, io_paths.OUTPATH_INDUSTRY, category.INDUSTRY_COLUMNS, category.INDUSTRY_DIC)
    return industry_list

# testCode : search_nm으로 검색 (산재업종분류-대분류 nm 으로 교체 후 돌릴것) 
def select_single_krasPrpare(session, rsknsEvlNo):
    all_prepareList = []
    industry_list = krasService.get_industry_pop_list(session, search_nm="건설업")
    job_list = krasService.get_prepare_list(session, rsknsEvlNo)

    for item in industry_list:
        for job in job_list:
            job["tpbizLclsfNm"] = item["tpbizLclsfNm"]
            job["tpbizMclsfNm"] = item["tpbizMclsfNm"]
            job["iaTpbizSclsfCdNm"] = item["iaTpbizSclsfCdNm"]
            job["rsknsEvlNo"] = rsknsEvlNo

        all_prepareList += job_list

    csvHelper.write_csv(all_prepareList, io_paths.OUTPATH_PREPARE, category.PREPARE_COLUMNS, category.PREPARE_DIC)
    return all_prepareList

# 공정 작업, 설명, 설비, 유해인자
# def select_krasPrpare():


# 위험발생 상황 및 결과, 법령
def select_risk_factor(session, preaPare_DataList):
    all_risk_factor = []
    seen = set()

    for row in preaPare_DataList:
        iaTpbizJobProcsCd = row.get("iaTpbizJobProcsCd") #payload 값
        rsknsEvlNo = row.get("rsknsEvlNo")          
        rsknsEvlProcsNo = row.get("rsknsEvlProcsNo")

        print(rsknsEvlProcsNo)
        key = (rsknsEvlNo, rsknsEvlProcsNo, iaTpbizJobProcsCd)

        if key in seen:
            continue

        seen.add(key)
        risk_list = krasService.get_risk_factor(session, rsknsEvlNo, rsknsEvlProcsNo, iaTpbizJobProcsCd)

        for item in risk_list:
            item["tpbizLclsfNm"] = row.get("tpbizLclsfNm")
            item["tpbizMclsfNm"] = row.get("tpbizMclsfNm")
            item["iaTpbizSclsfCdNm"] = row.get("iaTpbizSclsfCdNm")
            item["iaTpbizJobProcsSeq"] = row.get("iaTpbizJobProcsSeq")
            item["rsknsEvlJobProcsNm"] = row.get("rsknsEvlJobProcsNm")
            item["iaTpbizJobProcsExpln"] = row.get("iaTpbizJobProcsExpln")
            item["iaTpbizJobProcsMchnExpln"] = row.get("iaTpbizJobProcsMchnExpln")
            item["iaTpbizJobProcsNxsExpln"] = row.get("iaTpbizJobProcsNxsExpln")
            item["rsknsEvlNo"] = rsknsEvlNo
            item["rsknsEvlProcsNo"] = rsknsEvlProcsNo

        all_risk_factor += risk_list

    csvHelper.write_csv(all_risk_factor, io_paths.OUTPATH_RISK_FACTOR, category.RISK_FACTOR_COLUMNS, category.RISK_FACTOR_DIC)
    return all_risk_factor

# 현재의 안전보건조치
# def select_risk_level(session):
    # complete_evaluation_list = krasService.get_complete_evaluation_poplist(session, rsknsEvlNo)

# 위험성평가 완성표
def select_complete_evaluation_poplist(session, rsknsEvlNo):
    complete_evaluation_list = krasService.get_complete_evaluation_poplist(session, rsknsEvlNo)
    csvHelper.write_csv(complete_evaluation_list, io_paths.OUTPATH_COMPLETE_EVALUATION_POPLIST, category.COMPLETE_EVALUATION_POPLIST_COLUMNS, category.COMPLETE_EVALUATION_DIC)
    return complete_evaluation_list

# excel 파일 추출
def select_complete_evaluation_excel(session, rsknsEvlNo, dataList):
    content, filename = krasService.get_download_excel_file(session, rsknsEvlNo, dataList)
    out_path = fileHelper.outpath_complete_eval_excel(f"{filename}.xlsx")
    fileHelper.save_bytes(content, out_path)
    return out_path

def run_complete_evaluation_excel():
    with requests.Session() as session:
        rsknsEvlNo = select_rskns_evl_list(session)
        preaPare_DataList = select_single_krasPrpare(session, rsknsEvlNo)
        risk_factor_dataList = select_risk_factor(session, preaPare_DataList)
        # select_risk_level(session)
        # complete_evaluation_list = select_complete_evaluation_poplist(session, rsknsEvlNo)
        # select_complete_evaluation_excel(session, rsknsEvlNo, complete_evaluation_list)