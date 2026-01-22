import sys

class SysHelper:
    def __init__(self):
        pass

    def none_kras_evl(self):
        self.write_log("None Kras_Evl_File.")
        print("None Kras_Evl_File.")
        sys.exit()

    def none_token(self):
        self.write_log("None Token.")
        print("None Token")
        sys.exit()
    
    def none_save(self):
        self.write_log("Save fail")
        print("Save fail")
        sys.exit()
