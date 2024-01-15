# 目录结构
```xml
SANGER
├─conf    # 配置文件目录，使用yaml格式，用于编排插件的工作流程
├─core    # 这个加载插件的核心代码，一些父类和用于管理插件的类
├─log     # 保存运行中的日志
├─modules # 插件应统一将外部模块保存在此，提高便携能力
├─output	# 导出文件的根目录
├─plugin	# 插件本地，目前一个工作流一个目录也就对应一个配置文件；配置文件的名字此目录下的内容无关但建议相同
│  ├─AndroidPlugin # 插件示例1
│  ├─HostPentest # 插件示例2
└─ ├─test # 插件示例3
```
# core的逻辑
最底层三个类：

- 插件基类：`BasePlugin`
- 插件管理器基类：`BaseManager`
- 日志类：`Logger`
## Logger类
最简单的类写在最前面，写Logger类是为了方便在项目中各处统一调试。
使用方法：
```xml
from core import PluginManager
l = PluginManager.getLogger()# 个人推荐将这个变量放在全局中声明

l.d_('debug')
l.i_('info')
l.w_('warning')
l.e_('error')
l.c_('critical')

```
## BasePlugin类
基本的逻辑很简单，就是希望插件的执行过程是`检查运行环境(checkEnv)->由外部传来插件参数(setParam)->运行插件(run)->定制输出（包括屏幕输出和向下一个插件提供的返回值；BaseManager会将向后提供的output返回值转换为Input，交给下一个插件）(output)`  

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1269792/1704792405104-f97aa146-0f16-4d7c-a8d6-268bfa6b8ea3.jpeg)

并且，规定后续编写的自定义插件都应该至少定义一个叫做interface的，继承自BasePlugin类的子类。
## BaseManager类
BasePlugin类定义了单个Plugin的工作流程，BaseManager类则负责控制一个队列的Plugin工作。（目前只支持顺序执行）BaseManager的期望使用顺序是：`加载配置loadConf->加载插件loadPlugin/插件队列loadPluginByList/全部顺序加载loadAll->执行Plugin类的规范流程workByQueue->结束`

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1269792/1704793189998-19ce4ee7-7543-44c7-9af2-bb9904401c76.jpeg)
# 模板
## 配置文件模板
```yaml
插件名1:
  PluginPath: 将被python引用的插件路径，不带py后缀名
  Params: # 指定插件使用到的参数
    target: # 自定义参数
      - /data	# 数组参数
      - /etc
    deviceName: "127.0.0.1:62005" # 自定义字符串参数
  Output: output # 通过字符串，声明插件运行结束后，使用此键值保存运行结果
插件名2:
  PluginPath: plugin.AndroidPlugin.pullfs
  Params:
    target: 
      - /data
      - /etc
    deviceName: "127.0.0.1:62005"
  Output: output
```
## 插件代码模板
```python
from core import PluginCore
from core import PluginManager

l = PluginManager.getLogger()
class interface(PluginCore.BasePlugin):
    def __init__(self):
        super().__init__()
        self.version = "0.0.1"
        self.codename = "AndroidPullFileSystem"	#插件代号，在执行前在命令行显示，是插件的正式名称
        # 例如：[2024-01-15  10:41:26.386] PluginManager.py -> run line:54 [INFO] : Running AndroidPullFileSystem@0.0.1
    def output(self, params=None):
        l.d_("debug信息")
        l.i_(f"提示信息")
        return {params["Output"] : self.outpath}
    def run(self, options=None):
        l.i_("")
        try:
        	something.do()    
        except Exception as e:
            l.exception(e)
        return super().run(options)
```
