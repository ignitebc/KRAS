import csv 

class CsvHelper:
    def __init__(self):
        pass

    def write_csv(self, datalist, out_path, csv_columns, value):
        with open(out_path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()

            for item in datalist or []:
                row = {}
                for col_name, json_key in value.items():
                    val = item.get(json_key)
                    row[col_name] = "" if val is None else str(val)
                writer.writerow(row)
