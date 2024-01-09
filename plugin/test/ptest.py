from core import PluginCore
from core import PluginManager

l = PluginManager.getLogger()
class interface(PluginCore.BasePlugin):
    def __init__(self):
        super().__init__()
        self.codename = "测试插件"
    def output(self, params=None):
        l.d_("正在按照设置处理插件输出")
        return super().output(params)
    def run(self, options=None):
        print("测试插件正在运行")
        return super().run()
