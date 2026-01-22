class GroupBy:
    def __init__(self):
        pass

    def group_by_postiatpbiz_dataList(self, postiatpbiz_dataList):
        grouped = {}

        for row in postiatpbiz_dataList:
            key = row.get("iaTpbizSclsfDtlCd")

            if key not in grouped:
                grouped[key] = []

            grouped[key].append(row)

        return grouped

    def group_by_riskfactor_dataList(self, riskfactor_dataList):
        grouped = {}

        for row in riskfactor_dataList:
            key = row.get("iaTpbizJobProcsCd")

            if key not in grouped:
                grouped[key] = []

            grouped[key].append(row)

        return grouped
