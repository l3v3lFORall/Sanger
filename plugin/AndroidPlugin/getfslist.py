from core import PluginCore
from core import PluginManager

l = PluginManager.getLogger()
class interface(PluginCore.BasePlugin):
    def __init__(self):
        super().__init__()
        self.plugin_output = ''
        self.version = "0.0.1"
        self.codename = "GetAndroidFileSystemList"	#插件代号，在执行前在命令行显示，是插件的正式名称
        # 例如：[2024-01-15  10:41:26.386] PluginManager.py -> run line:54 [INFO] : Running AndroidPullFileSystem@0.0.1
    def output(self, params=None):
        l.i_(f"插件输出参数：{params['Output']}:{self.fslist}")
        return {params["Output"] : self.fslist}
    def run(self, options=None):
        l.i_(f"{self.codename}: 过滤安卓filesystem获取需要拉取的目录")
        try:
            _params = options["Params"]
            deviceName = options[options["Input"]] # 接收上一个插件的输出
            import subprocess
            import shlex
            import base64
            shcmd = base64.b64decode('bHMgLWwgLyB8IGVncmVwICdeZCcgfCBhd2sgJ3twcmludCAkOH0nIHwgZ3JlcCAtdiAnZGV2JyB8IGdyZXAgLXYgJ3Byb2MnIHwgZ3JlcCAtdiAnbG9zdCtmb3VuZCc=')
            cmd = shlex.split(r'''adb -s {} shell "{}"'''.format(deviceName, shcmd.decode()))
            l.d_(cmd)
            cmd_result, _error = subprocess.Popen(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            self.fslist = list(filter(None, cmd_result.split('\n')))
            l.d_(cmd_result)


        except Exception as e:
            l.exception(e)
            exit(-1)
        return super().run(options)