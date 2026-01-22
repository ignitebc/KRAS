from Helper.logHelper import Log
from Helper.sysHelper import SysHelper
from Helper.csvHelper import CsvHelper
from Helper.fileHelper import FileHelper
from Helper.apiHelper import ApiHelper

import Resources.krasConfig as krasConfig
from Paths import io_paths

class KrasContext(Log, SysHelper, CsvHelper, FileHelper, ApiHelper):
    def __init__(self):
        Log.__init__(self)
        SysHelper.__init__(self)
        CsvHelper.__init__(self)
        FileHelper.__init__(self)
        ApiHelper.__init__(self)
        
        self.config = krasConfig
        self.paths = io_paths
