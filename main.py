import krasTasks

# 업종별 
def select_industry_pop_list():
    return krasTasks.select_industry_pop_list()

# 공정 작업, 설명, 설비, 유해인자
def select_selectKrasPrpare():
    return krasTasks.select_selectKrasPrpare()

def select_Risk_Factor():
    return krasTasks.select_Risk_Factor()

if __name__ == "__main__":
    select_industry_pop_list()
    select_selectKrasPrpare()
