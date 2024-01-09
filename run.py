from core import PluginManager


a = PluginManager.MyManager()
a.loadConf("Android.yaml")
a.loadPlugin("AndroidPentest2")
a.workbyQueue()
