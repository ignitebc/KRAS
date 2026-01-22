from krasTasks import KrasPipelineTask

class KRASApplication:
    def __init__(self):
        pass

    # 금융및보험업, 광  업, 제조업, 전기·가스·증기및수도사업, 기타의사업, 운수·창고 및 통신업, 임  업, 어  업, 농  업, 건설업
    def run(self):
        task = KrasPipelineTask()
        task.run("금융및보험업")

def main():
    app = KRASApplication()
    app.run()

if __name__ == "__main__":
    main()
 