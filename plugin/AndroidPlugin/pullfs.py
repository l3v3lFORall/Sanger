from core import PluginCore
from core import PluginManager

l = PluginManager.getLogger()
class interface(PluginCore.BasePlugin):
    def __init__(self):
        super().__init__()
        self.codename = "AndroidPullFileSystem"
        self.outpath = "./"
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
                    return serialNum
                else:
                    continue
            raise AttributeError("ADB 设备选择异常：检查设备是否存在；是否在配置文件中正确指定")
    def output(self, params=None):
        l.d_("正在按照设置处理插件输出")
        l.i_(f"Pulled Files to {self.outpath}")
        return {params["Output"] : self.outpath}
    def run(self, options=None):
        # TODO 增加处理Input的代码
        # TODO 拆分为检查adb状态的插件CheckADBTarget和拉取文件系统的插件PullFS
        l.i_("""准备导出安卓文件系统""")
        _params = options["Params"]
        _output = options["Output"]
        from pathlib import Path
        import os
        current_path = Path(__file__).resolve().parent
        root_path = current_path.parent.parent

        if not os.path.exists(_output):
            os.makedirs(_output)

        try:
            _targetList = options[options["Input"]] # 接收上一个插件的输出
            cmd_result1 = os.popen("adb devices").read()
            l.d_(cmd_result1)
            if 'List of devices attached\n\n' == cmd_result1: 
                raise AttributeError("ADB连接异常")
            assert(isinstance(_targetList, list))

            deviceName = self.getDevice(cmd_result1, options=_params)
            for _path in _targetList:
                self.outpath = os.path.join(root_path, _output)
                l.i_(f"Pulling {deviceName}'s {_path} to {self.outpath}")
                os.system(f"adb root && adb -s {deviceName} pull {_path} {self.outpath}")
        except Exception as e:
            l.exception(e)
        return super().run(options)