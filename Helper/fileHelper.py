import os

class FileHelper:
    def __init__(self):
        pass

    def save_bytes(self, content, out_path):
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(content)

    def outpath_postiatpbiz_csv(self, filename):
        os.makedirs(self.paths.OUTPATH_CSV_POSTIATPBIZ, exist_ok=True)
        return os.path.join(self.paths.OUTPATH_CSV_POSTIATPBIZ, filename)
    
    def outpath_risk_factor_csv(self, filename):
        os.makedirs(self.paths.OUTPATH_CSV_RISK_FACTOR, exist_ok=True)
        return os.path.join(self.paths.OUTPATH_CSV_RISK_FACTOR, filename)

    def outpath_health_measures_csv(self, filename):
        os.makedirs(self.paths.OUTPATH_CSV_HEALTH_MEASURES, exist_ok=True)
        return os.path.join(self.paths.OUTPATH_CSV_HEALTH_MEASURES, filename)

    def outpath_complete_eval_excel(self, filename):
        os.makedirs(self.paths.OUTPATH_EXCEL_DWNLD, exist_ok=True)
        return os.path.join(self.paths.OUTPATH_EXCEL_DWNLD, filename)

