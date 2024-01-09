from core import PluginManager


a = PluginManager.MyManager()
a.loadConf("HostPentest.yaml")
# a.loadPlugin("loadTarget")
a.workbyQueue()
