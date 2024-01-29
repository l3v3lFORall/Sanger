制作一个满足“可订制“、”ALL-IN-ONE“的自动渗透测试基线工具  
所有工具都以插件的形式加载，按照配置的编排自动运行  
为了统一化渗透过程，方便上手、优化和避免重复工  

- 核心组件
    - [x] 插件输入输出数据处理：每个插件运行结束时向下一个插件的运行选项中增加了：
        1. Input键用来指明交付的运行结果的键名
        2. Output键保存运行结果
    - [ ] 默认的简单工作流程
        - [ ] =>URL=>前端敏感信息=>目录扫描
        - |=>端口扫描=>服务发现
            - [x] loadTarget 多种方式加载目标/目标列表
            - [x] PortScan  端口扫描(namp)(root in linux only)
            - [x] ServiceRecon  端口服务识别(nmap)(root in linux only)
            - [ ] ServiceRecon2 
            - [ ] vulnscan1-xray
            - [ ] vulnscan2-nuclei
            - [ ] vulnscan3-vulmap
        - 车机安卓渗透
            - 基础检查
                - [x] CheckADBTarget 检查adb连接状态
            - 文件系统检查
                - [x] getfslist 获取文件系统目录
                - [x] pullfs    下载文件系统
                - [ ] findconf  搜索配置文件和其中的敏感信息
                - [ ] findsrc   搜索源代码文件、备份文件、压缩文件、shell脚本
                - [ ] getbinlist    搜索可执行文件和共享库
                - [ ] checksec  执行checksec
                - [ ] checkstrip    检查strip和debug符号
                - [ ] findsecret    全盘搜索可疑关键字
                - [ ] checkcron     检查计划任务
            
            
    - [ ] 任务结果可视化
    - [ ] [*]中断继续
    - [ ] [*]跨平台兼容性/docker
    - [x] 使用文档



- [ ] GUI
    - [ ] BS
    - [ ] CS
