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
    "No.": "iaTpbizJobProcsSeq",
    "공정(작업)": "rsknsEvlJobProcsNm",
    "공정(작업)설명": "iaTpbizJobProcsExpln",
    "설비": "iaTpbizJobProcsMchnExpln",
    "유해인자": "iaTpbizJobProcsNxsExpln",
}

INDUSTRY_COLUMNS = list(INDUSTRY_DIC.keys())
PREPARE_COLUMNS = list(PREPARE_DIC.keys())