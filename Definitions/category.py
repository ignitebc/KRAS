# 업종(산재업종분류)
INDUSTRY_DIC = {
    "번호": "iaTpbizSclsfCd",
    "산재업종분류-대분류": "tpbizLclsfNm",
    "산재업종분류-중분류": "tpbizMclsfNm",
    "산재업종분류-소분류": "iaTpbizSclsfCdNm",
    "산재업종분류-세부코드": "iaTpbizSclsfDtlCd",
    "산재업종분류 - 세부작업": "iaTpbizSclsfDtlCdNm",
    "표준산업분류-대분류": "stdIndutyLclasNm",
    "표준산업분류-중분류": "stdIndutyMlsfcNm",
    "표준산업분류-소분류": "stdIndutyNm",
    "키값": "srchKywdNm",
}

# 공정(작업), 설명, 유해인자
PREPARE_DIC = {
    "산재업종분류-대분류": "tpbizLclsfNm",
    "산재업종분류-중분류": "tpbizMclsfNm",
    "산재업종분류-소분류": "iaTpbizSclsfCdNm",
    "No(StepNo.)": "iaTpbizJobProcsSeq",
    "공정(작업)": "rsknsEvlJobProcsNm",
    "공정(작업)설명": "iaTpbizJobProcsExpln",
    "설비": "iaTpbizJobProcsMchnExpln",
    "유해인자": "iaTpbizJobProcsNxsExpln",
    "EvlProcsNo" : "rsknsEvlProcsNo",
    "ProcsCd" : "iaTpbizJobProcsCd"
}

# 위험발생 상황 및 결과, 법령
RISK_FACTOR_DIC = {
    "산재업종분류-대분류": "tpbizLclsfNm",
    "산재업종분류-중분류": "tpbizMclsfNm",
    "산재업종분류-소분류": "iaTpbizSclsfCdNm",
    "No.": "iaTpbizJobProcsSeq",
    "공정(작업)": "rsknsEvlJobProcsNm",
    "공정(작업)설명": "iaTpbizJobProcsExpln",
    "설비": "iaTpbizJobProcsMchnExpln",
    "유해인자": "iaTpbizJobProcsNxsExpln",
    "위험발생 상황 및 결과" : "nxsRiskFctrCn",
    "관련근거(법령)" : "sttLprvsTtlNm"
}

# 위험성평가 완성표 (selectCompleteEvaluationPopList 결과)
COMPLETE_EVALUATION_DIC = {
    "파일번호": "rsknsEvlNo",
    "평가년도": "rsknsEvlYr",
    "평가명": "rsknsEvlTtlNm",
    "평가구분": "krasSeCmmnNm",
    "평가방법": "rsknsEvlMthdCdNm",
    "평가기준": "krasStdrCmmnNm",

    "공정번호": "rsknsEvlProcsNo",
    "공정(작업)": "rsknsEvlJobProcsNm",
    "공정(작업)설명": "rsknsEvlJobProcsExpln",
    "설비/기계": "rsknsEvlJobProcsMchnExpln",
    "유해인자/취급물질": "rsknsEvlJobProcsNxsExpln",

    "위험요인번호": "rsknsEvlNxsRiskFctrNo",
    "위험요인(상황/결과)": "nxsRiskFctrCn",
    "세부분류": "riskDtlClsfNm",

    "관련법령(제목)": "sttLprvsTtlNm",
    "관련법령(번호)": "sttLprvsNo",

    "현재-빈도": "nowOftnScr",
    "현재-강도": "nowStfnScr",
    "현재-위험성": "nowRsknsScr",

    "현재조치": "sfhlhManagtCn",
    "감소대책": "dcrsCmsrsCn",

    "최종평가일": "lastEvlDate",
    "최종수정일": "evlLastMdfcnYmd",
}

# # 위험성평가 결과표
# COMPLETEEVALUATIONPOPLIST_DIC = {
#     "rsknsEvlNo": 216324,
#     "bplcMngNo": null,
#     "bizStrtNo": null,
#     "rsknsEvlUnfcCustNo": "1KM77033601JX2763TWJ",
#     "rsknsEvlYr": "2026",                  # 년도
#     "rsknsEvlTtlNm": "위험성평가 test",     # 위험성평가명
#     "rsknsEvlSeCd": "02",
#     "krasSeCmmnNm": "정기평가",             # 평가 구분
#     "rsknsEvlMthdCd": "02",
#     "krasMthNm": "빈도·강도법",             # 평가 방법
#     "rsknsEvlAtcflNo": null,
#     "rsknsEvlCrtrCd": "01",
#     "krasStdrCmmnNm": "3x3",                # 평가 기준명 (3x3)
#     "iaTpbizSclsfCd": "C00010",             # 산재업종분류-소분류 코드
#     "agrdeMinScr": 1,                       # 위험성 수준
#     "agrdeMaxScr": 3,
#     "bgrdeMinScr": 4,
#     "bgrdeMaxScr": 6,
#     "cgrdeMinScr": 7,
#     "cgrdeMaxScr": 9,
#     "dgrdeMinScr": null,
#     "dgrdeMaxScr": null,
#     "egrdeMinScr": null,
#     "egrdeMaxScr": null,
#     "fgrdeMinScr": null,
#     "fgrdeMaxScr": null,
#     "agrdeRsknsEvlImpvMthdCd": "01",
#     "aGradImprvmMthCmmnNm": "현재상태유지",
#     "bgrdeRsknsEvlImpvMthdCd": "02",
#     "bGradImprvmMthCmmnNm": "개선",
#     "cgrdeRsknsEvlImpvMthdCd": "03",
#     "cGradImprvmMthCmmnNm": "즉시개선",
#     "dgrdeRsknsEvlImpvMthdCd": "00",
#     "dGradImprvmMthCmmnNm": "미선택",
#     "egrdeRsknsEvlImpvMthdCd": "00",
#     "eGradImprvmMthCmmnNm": "미선택",
#     "fgrdeRsknsEvlImpvMthdCd": "00",
#     "fGradImprvmMthCmmnNm": "미선택",
#     "evlLastMdfcnYmd": "20260109",
#     "evlCmptnYn": "N",
#     "evlCmptnYmd": null,
#     "bldEvlCrtrMm": null,
#     "bldPrnmntProcsExpln": null,
#     "evlCrtrYmd": null,
#     "rsknsEvlProcsCnt": 0,
#     "rsknsEvlRsltShrnYn": "N",
#     "frstRegDt": "2026-01-07",
#     "lastMdfcnDt": "2026-01-07",
#     "rsknsEvlProcsNo": 1,
#     "공정(작업)" : "rsknsEvlJobProcsNm",        #공정(작업)
#     "rsknsEvlJobProcsExpln": "레미콘 운반트럭에 콘크리트 운반",
#     "rsknsEvlJobProcsMchnExpln": "레미콘 운반트럭, 펌프카",
#     "rsknsEvlJobProcsNxsExpln": "콘크리트",
#     "rsknsEvlNxsRiskFctrNo": 1,
#     "riskDtlClsfCd": "0.0",
#     "riskDtlClsfNm": "기타",
#     "stdNxsRiskFctrNo": 14543,
#     "위험발생 상황 및 결과" : "nxsRiskFctrCn",  #위험발생 상황 및 결과
#     "sttSeCd": "S0004",
#     "sttLprvsNo": "38",
#     "sttLprvsTtlNm": "산업안전보건기준에 관한 규칙 제 38조(사전조사 및 작업계획서의 작성 등)",
#     "nowOftnScr": 1,
#     "nowStfnScr": 1,
#     "nowRsknsScr": 1,
#     "nowRsknssGradCd": null,
#     "sortSeqNo": 1,
#     "sfhlhManagtCn": null,
#     "dcrsCmsrsCn": null,
#     "impvPrnmntYmd": null,
#     "impvCmptnYmd": null,
#     "impvPicNm": null,
#     "impvOftnScr": null,
#     "impvStfnScr": null,
#     "impvRsknsScr": null,
#     "imprvmRsknssGradCd": null,
#     "lastEvlDate": "2026-01-09"
# }

INDUSTRY_COLUMNS = list(INDUSTRY_DIC.keys())
PREPARE_COLUMNS = list(PREPARE_DIC.keys())
RISK_FACTOR_COLUMNS = list(RISK_FACTOR_DIC.keys())
COMPLETE_EVALUATION_POPLIST_COLUMNS = list(COMPLETE_EVALUATION_DIC.keys())