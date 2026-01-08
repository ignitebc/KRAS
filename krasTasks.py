import requests
import Helper.csvHelper as csvHelper
from Definitions import output_path, category
import Service.krasService as krasService

def select_industry_pop_list():
    with requests.Session() as session:
        industry_list = krasService.get_industry_list(session, search_nm="건설업", page=100)

    csvHelper.write_csv(industry_list, output_path.OUTPATH_INDUSTRY, category.INDUSTRY_COLUMNS, category.INDUSTRY_DIC)
    return industry_list

def select_selectKrasPrpare():
    all_prepareList = []

    with requests.Session() as session:
        # testCode : search_nm으로 검색 (산재업종분류-대분류 nm 으로 교체 후 돌릴것)
        industry_list = krasService.get_industry_list(session, search_nm="건설업", page=100)

        for it in industry_list:
            id_code = it["iaTpbizSclsfDtlCd"]
            job_list = krasService.get_prepare_list(session, id_code = id_code)
            
            for job in job_list:
                job["tpbizLclsfNm"] = it["tpbizLclsfNm"]
                job["tpbizMclsfNm"] = it["tpbizMclsfNm"]
                job["iaTpbizSclsfCdNm"] = it["iaTpbizSclsfCdNm"]

            all_prepareList += job_list
            
    csvHelper.write_csv(all_prepareList, output_path.OUTPATH_PREPARE, category.PREPARE_COLUMNS, category.PREPARE_DIC)
    return all_prepareList

def select_Risk_Factor():
    print("")