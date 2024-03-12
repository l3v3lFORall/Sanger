class tWorker():
    # ThreadWorker模块日志统一格式：
    # 
    def __init__(self) -> None:
        pass
    def getConfig(self) -> None:
        # 调用Loader加载配置文件
        pass
    def CreateTask(self) -> None:
        # Task即一个Module的Manager，也即一个线程
        pass
    def CreateLayer(self) -> None:
        # 每个Layer包含一至多个Task
        pass
    def LayerStart(self) -> None:
        # 按层次启动任务
        pass
    def setOutsider(self) -> None:
        # 运行结果向外部调用提供
        pass

if __name__ == "__main__":
    tw = tWorker()
    tw.getConfig()