from core import PluginCore

class interface(PluginCore.BasePlugin):
    def __init__(self):
        super().__init__()
        self.codename = "测试插件"
    def run(self, options=None):
        print("测试插件正在运行")
        return super().run()