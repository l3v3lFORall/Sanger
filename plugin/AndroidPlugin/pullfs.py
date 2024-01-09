from core import PluginCore
from core import PluginManager

l = PluginManager.getLogger()
class interface(PluginCore.BasePlugin):
    def __init__(self):
        super().__init__()
        self.codename = "AndroidPullFileSystem"
        self.outpath = "./"
    def getDevice(self, options=None):
        # TODO 获取已连接的安卓设备信息，如果只有一个就自动获取，如果有多个就按照options['deviceName']获取，如果没指定deviceName就从命令行要求输入
        pass
    def output(self, params=None):
        l.d_("正在按照设置处理插件输出")
        return {params["Output"] : self.outpath}
    def run(self, options=None):
        l.i_("""准备导出安卓文件系统""")
        _params = options["Params"]
        _output = options["Output"]
        import os
        try:
            cmd_result1 = os.popen("adb devices").read()
            l.d_(cmd_result1)
            if 'List of devices attached\n\n' == cmd_result1: 
                raise AttributeError("ADB连接异常")
            assert(isinstance(_params["target"], list))
            assert(isinstance(_output, list) and len(_output) == 1)
            deviceName = self.getDevice(_params)
            for _path in _params["target"]:
                # TODO 测试正确性
                self.outpath = {os.path.join(_output[0], _path)}
                l.i_(f"Pulling {deviceName}'s {_path} to {self.outpath}")
                os.system(f"adb pull -s {deviceName} {_path} {self.outpath}")
        except Exception as e:
            l.e_(f"{e}，退出插件！")
        return super().run(options)