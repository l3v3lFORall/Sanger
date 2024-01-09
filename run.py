from core import PluginManager


a = PluginManager.MyManager()
a.loadConf("Android.yaml")
# a.loadPlugin("loadTarget")
a.workbyQueue()
