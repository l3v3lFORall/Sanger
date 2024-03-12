import logging
import colorlog
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

