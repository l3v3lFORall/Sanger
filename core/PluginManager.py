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

    def run(self, codename:str):
        __p = self.getPlugin(codename).interface()
        __c = self.config[codename]
        __p.checkEnv()
        __p.setParam(__c["Params"])
        __p.run()
        l.i_("Running " + __p.getPluginname()+ "@" +__p.getVersion())
    
    def workbyQueue(self):
        for _cn in self.pqueue.keys():
            self.run(_cn)

if __name__ == "__main__":
    a = MyManager()
    a.loadConf("Plugin.yaml")
    a.loadPlugin("PluginTest")