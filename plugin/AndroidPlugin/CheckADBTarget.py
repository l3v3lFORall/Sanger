from core import PluginCore
from core import PluginManager

l = PluginManager.getLogger()
class interface(PluginCore.BasePlugin):
    def __init__(self):
        super().__init__()
        self.plugin_output = ''
        self.version = "0.0.1"
        self.codename = "CheckADBTarget"	#插件代号，在执行前在命令行显示，是插件的正式名称
        # 例如：[2024-01-15  10:41:26.386] PluginManager.py -> run line:54 [INFO] : Running AndroidPullFileSystem@0.0.1
    def getDevice(self, cmd, options=None):
        data = list(filter(None, cmd.split('\n')))[1:]
        if len(data) == 1:
            # 只有一个设备
            return str(data[0].split('\t')[0])
        elif "deviceName" in options.keys and options["deviceName"] != "":
            # 只连接指定设备
            return options["deviceName"]
        else:
            # 用户手动选择设别
            for _d in data:
                serialNum, _ = _d.split('\t')
                if input("Use This Device[Y/N]:").lower() == 'y': 
                    # TODO 检查正确性
                    return serialNum
                else:
                    continue
            raise AttributeError("ADB 设备选择异常：检查设备是否存在；是否在配置文件中正确指定")
    def output(self, params=None):
        l.i_(f"插件输出参数：{params['Output']}: {self.deviceName}")
        return {params["Output"] : self.deviceName}
    def run(self, options=None):
        l.i_(f"{self.codename}: 检查adb设备")
        try:
            _params = options["Params"]
            import os
            cmd_result1 = os.popen("adb devices").read()
            l.d_(cmd_result1)
            if 'List of devices attached\n\n' == cmd_result1: 
                raise AttributeError("ADB连接异常")  
            self.deviceName = self.getDevice(cmd_result1, options=_params)
        except Exception as e:
            l.exception(e)
        return super().run(options)