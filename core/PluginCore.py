import logging
import colorlog
class BasePlugin:
    def __init__(self):
        self.version = "0.0.1"
        self.codename = "baby"
        self.params = {}
        pass
    def getVersion(self):
        return self.version
    def getPluginname(self):
        '''
        返回插件名/代号/github地址等信息
        '''
        return self.codename
    def setParam(self, params=None):
        '''
        设置插件所需参数的接口
        '''
        self.params = {}
        pass
    def checkEnv(self):
        '''
        检查插件运行所需环境的接口
        '''
        pass
    def run(self, options=None):
        return self.output(options)

    def output(self, params=None):
        pass

class BaseManager:
    def __init__(self):
        pass
    def loadConf(self, path:str):
        '''
        加载插件相关的配置文件
        '''
        self.config = {}
    def loadPlugin(self, codename:str):
        if hasattr(self, 'pqueue') :
            self.pqueue[codename] = ''
        else:
            self.pqueue = {
                codename : ''
                }
    def getPlugin(self, codename:str):
        return self.pqueue[codename]
    
    def loadPluginByList(self, codelist:list):
        '''
        多线程地同时加载codelist中指定的插件列表
        '''
        self.pqueue = {
            'a': '',
            'b': ''
        }
    def loadAll(self):
        pass
    def getPluginByList(self, codelist:list):
        '''
        按列表返回插件列表
        '''
        plist = []
        for _cn in codelist:
            plist.append(
                self.pqueue.get(_cn, "Plugin Not Found")
            )
        return plist
    
    def cleanPlugin(self):
        pass

    def unloadPlugin(self, codename:str):
        pass
    def reloadPlugin(self, codename:str):
        pass



class Logger:
    def __init__(self, loglevel="DEBUG"):

        self.log_colors_config = {
            'DEBUG': 'white',  # cyan white
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
        import time
        self.logname = f'Sanger_logger_{int(round(time.time()/100))}.log'
        self.logger = logging.getLogger(self.logname)
        self.loglevel = self._getLogLevel(loglevel)
        # 输出到控制台
        self.console_handler = logging.StreamHandler()
        self.logger.setLevel(self.loglevel)
        self.console_handler.setLevel(self.loglevel)
        console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=self.log_colors_config
        )
        self.console_handler.setFormatter(console_formatter)
        self.logger.addHandler(self.console_handler)
        self.console_handler.close()
    def _getLogLevel(self, loglevel):
        loglevel = str(loglevel)
        if loglevel[0].lower() == "d":
            return logging.DEBUG
        elif loglevel[0].lower() == "i":
            return logging.DEBUG
        elif loglevel[0].lower() == "w":
            return logging.DEBUG
        elif loglevel[0].lower() == "e":
            return logging.DEBUG
        elif loglevel[0].lower() == "c":
            return logging.DEBUG
        else:
            raise Exception("日志记录等级不存在或无法识别")
        

    def outputLog2File(self, filename=None):
        import os
        if not os.path.exists('log'):
            os.mkdir("log")
        if filename is None:
            filename = self.logname
        from logging.handlers import RotatingFileHandler
        self.file_handler = RotatingFileHandler(
            filename=os.path.join('log', filename),
            mode='a',
            encoding='utf8',
            maxBytes=5 * 1024 * 1024
            )
        self.file_handler.setLevel(self.loglevel)
        # 日志输出格式
        file_formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S'
        )
        self.file_handler.setFormatter(file_formatter)
        self.logger.addHandler(self.file_handler)
        self.file_handler.close()
        return 'log/'+self.logname

    def d_(self, msg):
        msg = str(msg)
        return self.logger.debug(msg, stacklevel=2) # stacklevel=2 使日志在正确的位置提示
    def i_(self, msg):
        msg = str(msg)
        return self.logger.info(msg, stacklevel=2)
    def w_(self, msg):
        msg = str(msg)
        return self.logger.warning(msg, stacklevel=2)
    def e_(self, msg):
        msg = str(msg)
        return self.logger.error(msg, stacklevel=2)
    def c_(self, msg):
        msg = str(msg)
        return self.logger.critical(msg, stacklevel=2)
    def exception(self, e):
        return logging.exception(e)


class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

# 单例模式
@Singleton
class DBBackend():
    _conn = None

    _DBPath = None
    def __init__(self, dbpath="Sanger.db"):
        # 检查数据库，如果已经存在_conn则返回_conn，如果没有建立_conn，则按照dbpath新建sqlite连接，保存并返回_conn。
        if self._conn == None:
            import os
            if not os.path.exists('log'):
                os.mkdir("log")
            import sqlite3
            self._conn = sqlite3.connect(dbpath)
        else:
            pass
        self.checkDB()
        self._cur = self._conn.cursor()
        return self._conn
    def checkDB(self):
        # 检查数据库的基本结构，如果是新数据库，则初始化数据库
        pass

    def _s(self, sql):
        # select query
        '''
        res = cur.execute("SELECT name FROM sqlite_master")
        res.fetchone()
        res.fetchall()
        '''
        pass
    def _bs(self, data, sql):
        # batch select query
        '''
        data = [
            ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
            ("Monty Python's The Meaning of Life", 1983, 7.5),
            ("Monty Python's Life of Brian", 1979, 8.0),
        ]
        cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
        con.commit()  # Remember to commit the transaction after executing INSERT.
        '''
        pass

    def _i(self, sql):
        # insert query
        '''
        The INSERT statement need commit
        con.commit()
        '''
        pass
    def _d(self, sql):
        # delete query
        # conn.commit()
        pass
    def _u(self, sql):
        # update query
        # conn.commit()
        pass



if __name__ == '__main__':
    l = Logger()
    l.outputLog2File()
    l.d_('test')
    l.i_('aa')
    l.w_('debug')
    l.e_('debug')
    l.c_('debug')
