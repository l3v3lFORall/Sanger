from core.PluginCore import BaseManager
from core.PluginCore import BasePlugin
from core.PluginCore import Logger
import os
import importlib


l = Logger()
l.i_("LogFile Saved in: " + l.outputLog2File())
def getLogger():
    return l

class MyManager(BaseManager):
    def __init__(self):
        super().__init__()
    def loadConf(self, path: str):
        super().loadConf(path)
        import yaml
        self.config = yaml.load(
            open(os.path.join("conf", path), "r"),
            Loader=yaml.FullLoader
        )
        l.d_(self.config)
    def loadPlugin(self, codename: str):
        super().loadPlugin(codename)
        _config = self.config[codename]
        self.pqueue[codename] = importlib.import_module(
            _config["PluginPath"]
        )
        l.d_(f"Loaded plugin({codename}): {str(self.pqueue[codename])}")
    def loadPluginByList(self, codelist: list):
        for codename in codelist:
            super().loadPlugin(codename)
            _config = self.config[codename]
            self.pqueue[codename] = importlib.import_module(
                _config["PluginPath"]
            )
            l.d_(f"Loaded plugin({codename}): {str(self.pqueue[codename])}")

    def loadAll(self):
        self.loadPluginByList(list(self.config.keys()))


    def run(self, codename:str):
        __p = self.getPlugin(codename).interface()

        if self.output is not None:
            self.config[codename].update(self.output)
            # 增加上一个插件的输出数据
        __c = self.config[codename]
        l.d_(__c)
        __p.checkEnv()
        __p.setParam(__c["Params"])
        l.i_("Running " + __p.getPluginname()+ "@" +__p.getVersion())
        self.output = __p.run(__c)
        self.output["Input"] = self.config[codename]["Output"]
        # 将上一个插件的输出键值保存为下一个插件的输入键值
    def workbyQueue(self):
        if not hasattr(self, 'pqueue'):
            # 当没指定运行某个单独的插件或插件列表时，默认按顺序执行所有插件
            self.loadAll()
        self.output = {}
        for _cn in self.pqueue.keys():
            self.run(_cn)

if __name__ == "__main__":
    a = MyManager()
    a.loadConf("Plugin.yaml")
    a.loadPlugin("PluginTest")
