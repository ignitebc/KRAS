import requests
import uuid
import os
from datetime import datetime
from Core.context import KrasContext
from Core import models
from Service.krasService import KrasService
from Utils.groupby import GroupBy

class KrasPipelineTask(KrasContext):
    def __init__(self):
        super().__init__()
        self.service = KrasService()
        self.groupby = GroupBy()

    # 업종별
    def select_industry_pop_list(self, session):
        industry_list = self.service.get_industry_pop_list(session, search_nm="")
        return industry_list

    # rsknsEvlNo 추출
    def select_rskns_evl_list(self, session):
        rsknsEvlNo = self.service.get_rskns_evl_list(session)
        self.write_log("End select rskns_evl.")
        return rsknsEvlNo

    # testCode : 작업,설명,유해인자의 key / search_nm으로 검색
    def select_single_postiatpbiz(self, session, rsknsEvlNo, industry_data, search_nm):
        filtered = []
        
        for item in industry_data:
            if item.get("tpbizLclsfNm") == search_nm:
                filtered.append(item)

        all_postiatpbiz = []
        for meta in filtered:
            iaTpbizSclsfDtlCd = meta.get("iaTpbizSclsfDtlCd")
            iaTpbizSclsfCd = meta.get("iaTpbizSclsfCd")
            iaTpbizSclsfDtlCdNm = meta.get("iaTpbizSclsfDtlCdNm")

            postiatpbiz_list = self.service.get_postiatpbiz(session, iaTpbizSclsfDtlCd, iaTpbizSclsfCd)

            for postiatpbiz_item in postiatpbiz_list:
                postiatpbiz_item["tpbizLclsfNm"] = meta.get("tpbizLclsfNm")
                postiatpbiz_item["tpbizMclsfNm"] = meta.get("tpbizMclsfNm")
                postiatpbiz_item["iaTpbizSclsfCdNm"] = meta.get("iaTpbizSclsfCdNm")
                postiatpbiz_item["iaTpbizSclsfDtlCd"] = meta.get("iaTpbizSclsfDtlCd")
                postiatpbiz_item["iaTpbizSclsfDtlCdNm"] = iaTpbizSclsfDtlCdNm
                postiatpbiz_item["rsknsEvlNo"] = rsknsEvlNo
            
            all_postiatpbiz += postiatpbiz_list
        
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_dir = os.path.dirname(self.paths.OUTPATH_POST_IA_TPBIZ)
        out_path = os.path.join(base_dir, f"postiatpbiz_{rsknsEvlNo}_{ts}.csv")
        self.write_csv(all_postiatpbiz, out_path, models.POSTIATPBIZ_COLUMNS, models.POSTIATPBIZ_DIC)
        self.write_log("End write postiatpbiz csv.")
        self.write_log("select_single_postiatpbiz complete")
        return all_postiatpbiz

    # 위험발생 상황 및 결과, 법령
    def select_risk_factor(self, session, postiatpbiz_dataList, dtl_cd):
        all_risk_factor = []

        for row in postiatpbiz_dataList:
            iaTpbizJobProcsCd = row.get("iaTpbizJobProcsCd")
            rsknsEvlNo = row.get("rsknsEvlNo")
            rsknsEvlProcsNo = row.get("iaTpbizJobProcsSeq")
            risk_list = self.service.get_risk_factor(session, rsknsEvlNo, rsknsEvlProcsNo, iaTpbizJobProcsCd)

            for idx, risk_item in enumerate(risk_list, start=1):
                risk_item["tpbizLclsfNm"] = row.get("tpbizLclsfNm")
                risk_item["tpbizMclsfNm"] = row.get("tpbizMclsfNm")
                risk_item["iaTpbizSclsfCdNm"] = row.get("iaTpbizSclsfCdNm")
                risk_item["iaTpbizSclsfDtlCdNm"] = row.get("iaTpbizSclsfDtlCdNm")
                risk_item["iaTpbizJobProcsSeq"] = row.get("iaTpbizJobProcsSeq")
                risk_item["rsknsEvlJobProcsNm"] = row.get("rsknsEvlJobProcsNm")
                risk_item["iaTpbizJobProcsExpln"] = row.get("iaTpbizJobProcsExpln")
                risk_item["iaTpbizJobProcsMchnExpln"] = row.get("iaTpbizJobProcsMchnExpln")
                risk_item["iaTpbizJobProcsNxsExpln"] = row.get("iaTpbizJobProcsNxsExpln")
                risk_item["iaTpbizJobProcsCd"] = iaTpbizJobProcsCd
                risk_item["rsknsEvlNxsRiskFctrNo"] = idx

            all_risk_factor += risk_list
        
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = self.outpath_risk_factor_csv(f"risk_factor_{dtl_cd}_{rsknsEvlNo}_{ts}.csv")

        self.write_csv(all_risk_factor, out_path, models.RISK_FACTOR_COLUMNS, models.RISK_FACTOR_DIC)
        self.write_log("End write risk_factor csv.")
        self.write_log("select_risk_factor complete")
        return all_risk_factor

    # 현재의 안전보건조치
    def select_health_measures_poplist(self, session, rsknsEvlNo, grouped_by_risk_factor, dtl_cd):
        all_health_measures = []

        for tab_idx, (group_key, risk_list) in enumerate(grouped_by_risk_factor.items(), start = 1):
            for coulumn_idx, row in enumerate(risk_list, start = 1):
                iaTpbizJobProcsSeq = row.get("iaTpbizJobProcsSeq")
                rsknsEvlNxsRiskFctrNo = row.get("rsknsEvlNxsRiskFctrNo")
                health_list = self.service.get_select_health_measures_poplist(session, rsknsEvlNo, rsknsEvlNxsRiskFctrNo, iaTpbizJobProcsSeq)
                
                if(len(health_list) > 0):
                    data_save = self.service.get_savebtn_health_measures(session, health_list)
                    if data_save is True:
                        self.write_log("get_savebtn_health_measures complete")
                    else:
                        self.none_save()

                for health_item in health_list:
                    health_item["tpbizLclsfNm"] = row.get("tpbizLclsfNm")
                    health_item["tpbizMclsfNm"] = row.get("tpbizMclsfNm")
                    health_item["iaTpbizSclsfCdNm"] = row.get("iaTpbizSclsfCdNm")
                    health_item["iaTpbizSclsfDtlCdNm"] = row.get("iaTpbizSclsfDtlCdNm")
                    health_item["iaTpbizJobProcsSeq"] = row.get("iaTpbizJobProcsSeq")
                    health_item["rsknsEvlJobProcsNm"] = row.get("rsknsEvlJobProcsNm")
                    health_item["iaTpbizJobProcsExpln"] = row.get("iaTpbizJobProcsExpln")
                    health_item["iaTpbizJobProcsMchnExpln"] = row.get("iaTpbizJobProcsMchnExpln")
                    health_item["iaTpbizJobProcsNxsExpln"] = row.get("iaTpbizJobProcsNxsExpln")
                    health_item["riskDtlClsfNm"] = row.get("riskDtlClsfNm")
                    health_item["nxsRiskFctrCn"] = row.get("nxsRiskFctrCn")
                    health_item["sttLprvsTtlNm"] = row.get("sttLprvsTtlNm")
                    health_item["sttLprvsCn"] = row.get("sttLprvsCn")

                all_health_measures += health_list

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = self.outpath_health_measures_csv(f"health_measures_{dtl_cd}_{rsknsEvlNo}_{ts}.csv")

        self.write_csv(all_health_measures, out_path, models.HEALTH_MEASURES_COLUMNS, models.HEALTH_MEASURES_DIC)
        self.write_log("End write health_measures csv.")
        self.write_log("select_health_measures_poplist complete")
        return all_health_measures

    def select_imprvm_after_rsknss(self, session, rsknsEvlNo):
        tab_name_dataList  = []
        imprvm_after_rsknss_dataList = self.service.get_imprvm_after_rsknss(session, rsknsEvlNo)
        
        for row in imprvm_after_rsknss_dataList:
            tabNumber = row.get("iaTpbizJobProcsCd")
            tab_name_dataList.append(tabNumber)

        return tab_name_dataList
    
    # TEST CODE : (필요시 사용)
    def select_risk_after_improvement(self, session, rsknsEvlNo, tab_names):
        for idx, tab_name in enumerate(tab_names, start=1):
            self.service.get_risk_after_improvement(session, tab_name, idx, rsknsEvlNo)
            self.select_complete_evaluation_excel(session, rsknsEvlNo)

    # TEST CODE : 위험성평가 완성표 (필요시 사용 - CSV파일 커스텀 제작용)
    def select_complete_evaluation_poplist(self, session, rsknsEvlNo):
        complete_evaluation_list = self.service.get_complete_evaluation_poplist(session, rsknsEvlNo)
        self.write_csv(complete_evaluation_list, self.paths.OUTPATH_COMPLETE_EVALUATION_POPLIST, models.COMPLETE_EVALUATION_POPLIST_COLUMNS, models.COMPLETE_EVALUATION_DIC)
        return complete_evaluation_list

    # Complete Excel 파일 추출
    def select_complete_evaluation_excel(self, session, rsknsEvlNo, dtl_cd):
        content, filename = self.service.get_download_excel_file(session, rsknsEvlNo)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = self.outpath_complete_eval_excel(f"{dtl_cd}_{ts}.xlsx")
        self.save_bytes(content, out_path)
    
    # Save API Logic
    def save_single_postiatpbiz(self, session, rows, rsknsEvlNo):
        saveList = []

        for idx, row in enumerate(rows, start=1):
            row_uid = str(uuid.uuid4()).upper()
            item = {
                "iaTpbizJobProcsCd": row.get("iaTpbizJobProcsCd"),
                "iaTpbizJobProcsExpln": row.get("iaTpbizJobProcsExpln"),
                "iaTpbizJobProcsMchnExpln": row.get("iaTpbizJobProcsMchnExpln"),
                "iaTpbizJobProcsNxsExpln": row.get("iaTpbizJobProcsNxsExpln"),
                "iaTpbizJobProcsSeq" : idx,
                "iaTpbizSclsfCd" : row.get("iaTpbizSclsfCd"),
                "iaTpbizSclsfDtlCd" : "null",
                "rsknsEvlJobProcsExpln" : row.get("iaTpbizJobProcsExpln"),
                "rsknsEvlJobProcsMchnExpln" : row.get("iaTpbizJobProcsMchnExpln"),
                "rsknsEvlJobProcsNm" : row.get("rsknsEvlJobProcsNm"),
                "rsknsEvlJobProcsNxsExpln" : "null",
                "rsknsEvlNo" : rsknsEvlNo,
                "sortSeqNo" : idx,
                "_$uid": row_uid,
            }

            saveList.append(item)

        data_save = self.service.get_savebtn_single_postiatpbiz(session, saveList, rsknsEvlNo)

        if data_save is True:
            self.write_log("save_single_postiatpbiz complete")
        else:
            self.none_save()

    def save_risk_factor(self, session, rows, rsknsEvlNo):
        for tab_idx, (group_key, risk_list) in enumerate(rows.items(), start=1):
            saveList = []

            for coulumn_idx, risk_row in enumerate(risk_list, start=1):
                row_uid = str(uuid.uuid4()).upper()

                item = {
                    "cmprNow3StepRsknssGradCd": "null",
                    "cmprNow5StepRsknssGradCd": "null",
                    "cmprNowRsknssScore": 0,
                    "dcrsCntrplnCn": "null",
                    "nowOftnScr": 0,
                    "nowRsknsGrd3stepCd": "null",
                    "nowRsknsGrd5stepCd": "null",
                    "nowRsknsScr": 0,
                    "nowStfnScr": 0,
                    "nxsRiskFctrCn": risk_row.get("nxsRiskFctrCn"),
                    "riskDtlClsfCd": risk_row.get("riskDtlClsfCd"),
                    "riskDtlClsfNm": risk_row.get("riskDtlClsfNm"),
                    "rsknsEvlNo": rsknsEvlNo,
                    "rsknsEvlNxsRiskFctrNo": coulumn_idx,
                    "rsknsEvlProcsNo": tab_idx,
                    "sfhlhManagtCn": "null",
                    "sortSeqNo": coulumn_idx,
                    "stdNxsRiskFctrNo": risk_row.get("stdNxsRiskFctrNo"),
                    "sttLprvsNo": risk_row.get("sttLprvsNo"),
                    "sttLprvsTtlNm": risk_row.get("sttLprvsTtlNm"),
                    "sttSeCd": risk_row.get("sttSeCd"),
                    "_$uid": row_uid
                }

                saveList.append(item)

            data_save = self.service.get_savebtn_risk_factor(session, saveList)

            if data_save is True:
                self.write_log(f"save_risk_factor complete ({group_key})")
            else:
                self.none_save()
    
    def run(self, search_nm):
        with requests.Session() as session:
            industry_data = self.select_industry_pop_list(session)
            rsknsEvlNo = self.select_rskns_evl_list(session)
            postiatpbiz_dataList = self.select_single_postiatpbiz(session, rsknsEvlNo, industry_data, search_nm)
            grouped_by_postiatData = self.groupby.group_by_postiatpbiz_dataList(postiatpbiz_dataList)

            print(len(grouped_by_postiatData))
            # grouped_by_postiatData = dict(list(grouped_by_postiatData.items())[500:560]) # TEST CODE : 나눠서 뽑을때 주석해제

            for dtl_cd, rows in grouped_by_postiatData.items():
                self.save_single_postiatpbiz(session, rows, rsknsEvlNo)
                risk_factor_dataList = self.select_risk_factor(session, rows, dtl_cd)
                grouped_by_risk_factor = self.groupby.group_by_riskfactor_dataList(risk_factor_dataList)
                self.save_risk_factor(session, grouped_by_risk_factor, rsknsEvlNo)
                self.select_health_measures_poplist(session, rsknsEvlNo, grouped_by_risk_factor, dtl_cd)
                tab_name= self.select_imprvm_after_rsknss(session, rsknsEvlNo)
                self.select_complete_evaluation_excel(session, rsknsEvlNo, dtl_cd)
                
                # self.select_risk_after_improvement(session, rsknsEvlNo, tab_name)
                # self.select_complete_evaluation_poplist(session, rsknsEvlNo)
                # self.save_health_measures(session, grouped_by_risk_factor, rsknsEvlNo)

