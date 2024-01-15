from core import PluginCore
from core import PluginManager

l = PluginManager.getLogger()
class interface(PluginCore.BasePlugin):
    def __init__(self):
        super().__init__()
        self.plugin_output = ''
        self.version = "0.0.1"
        self.codename = "AndroidPullFileSystem"	#插件代号，在执行前在命令行显示，是插件的正式名称
        # 例如：[2024-01-15  10:41:26.386] PluginManager.py -> run line:54 [INFO] : Running AndroidPullFileSystem@0.0.1
    def output(self, params=None):
        l.d_("debug信息")
        l.i_(f"提示信息")
        return {params["Output"] : self.plugin_output}
    def run(self, options=None):
        l.i_("")
        try:
            perivousInput = options[options["Input"]] # 接收上一个插件的输出  
        except Exception as e:
            l.exception(e)
            exit(-1)
        return super().run(options)