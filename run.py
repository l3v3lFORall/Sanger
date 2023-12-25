from core import PluginManager


a = PluginManager.MyManager()
a.loadConf("Plugin.yaml")
a.loadPlugin("PluginTest")
a.loadPlugin("PluginTest2")
a.workbyQueue()