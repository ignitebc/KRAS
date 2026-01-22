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
POSTIATPBIZ_DIC = {
    "산재업종분류-대분류": "tpbizLclsfNm",
    "산재업종분류-중분류": "tpbizMclsfNm",
    "산재업종분류-소분류": "iaTpbizSclsfCdNm",
    "산재업종분류 - 세부작업": "iaTpbizSclsfDtlCdNm",
    "공정(작업)": "rsknsEvlJobProcsNm",
    "공정(작업)설명": "iaTpbizJobProcsExpln",
    "설비" : "iaTpbizJobProcsMchnExpln",
    "유해인자" : "iaTpbizJobProcsNxsExpln",
    "rsknsEvlNo": "rsknsEvlNo",
    "iaTpbizJobProcsSeq" : "iaTpbizJobProcsSeq",
    "iaTpbizJobProcsCd" : "iaTpbizJobProcsCd",
    "iaTpbizSclsfDtlCd" : "iaTpbizSclsfDtlCd"
}

# 위험발생 상황 및 결과, 법령
RISK_FACTOR_DIC = {
    "산재업종분류-대분류": "tpbizLclsfNm",
    "산재업종분류-중분류": "tpbizMclsfNm",
    "산재업종분류-소분류": "iaTpbizSclsfCdNm",
    "산재업종분류 - 세부작업": "iaTpbizSclsfDtlCdNm",
    "No.": "iaTpbizJobProcsSeq",
    "공정(작업)": "rsknsEvlJobProcsNm",
    "공정(작업)설명": "iaTpbizJobProcsExpln",
    "설비": "iaTpbizJobProcsMchnExpln",
    "유해인자": "iaTpbizJobProcsNxsExpln",
    "위험분류" : "riskDtlClsfNm",
    "위험발생 상황 및 결과" : "nxsRiskFctrCn",
    "관련근거(법령)" : "sttLprvsTtlNm",
    "세부 법적근거" : "sttLprvsCn",
    "rsknsEvlNxsRiskFctrNo" : "rsknsEvlNxsRiskFctrNo",
    "위험분류코드" : "riskDtlClsfCd"
}

# 안전보건조치 (조치사항)
HEALTH_MEASURES_DIC = {
    "산재업종분류-대분류": "tpbizLclsfNm",
    "산재업종분류-중분류": "tpbizMclsfNm",
    "산재업종분류-소분류": "iaTpbizSclsfCdNm",
    "산재업종분류 - 세부작업": "iaTpbizSclsfDtlCdNm",
    "No.": "iaTpbizJobProcsSeq",
    "공정(작업)": "rsknsEvlJobProcsNm",
    "공정(작업)설명": "iaTpbizJobProcsExpln",
    "설비": "iaTpbizJobProcsMchnExpln",
    "유해인자": "iaTpbizJobProcsNxsExpln",
    "위험분류" : "riskDtlClsfNm",
    "위험발생 상황 및 결과" : "nxsRiskFctrCn",
    "관련근거(법령)" : "sttLprvsTtlNm",
    "세부 법적근거" : "sttLprvsCn",
    "표준 위험성평가 모델의 법규상 안전보건조치(참고용)" : "sftyHlthcActnCnRefer",
    "현재의 안전보건조치" : "sftyHlthcActnCn",
    # "rsknsEvlNo" : "rsknsEvlNo",
    # "rsknsEvlProcsNo" : "rsknsEvlProcsNo",
    # "rsknsEvlSftyHlthcActnNo" : "rsknsEvlSftyHlthcActnNo",
    # "stdNxsRiskFctrNo" : "stdNxsRiskFctrNo",
    # "stdSftyHlthcActnNo" : "stdSftyHlthcActnNo",
    # "ceck" : "ceck"
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

INDUSTRY_COLUMNS = list(INDUSTRY_DIC.keys())
POSTIATPBIZ_COLUMNS = list(POSTIATPBIZ_DIC.keys())
RISK_FACTOR_COLUMNS = list(RISK_FACTOR_DIC.keys())
HEALTH_MEASURES_COLUMNS = list(HEALTH_MEASURES_DIC.keys())
COMPLETE_EVALUATION_POPLIST_COLUMNS = list(COMPLETE_EVALUATION_DIC.keys())