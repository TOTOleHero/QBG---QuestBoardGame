#!/usr/bin/python

import log4py
import sys
from os import utime
from time import time

class Log4PyTest:

    def __init__(self):
        self.log4py = log4py.Logger().get_instance(self)

    def run(self):
        self.log4py.error("error")
        self.log4py.warn("warn")
        self.log4py.info("info")
        self.log4py.debug("debug")

    def output(self, message):
        self.log4py.info(message)

mytest = Log4PyTest()

print "\nSettings from log4py.conf\n"
mytest.run()

print "\nNormal level - Long format (written to $HOME/log4py-test.log)"
mytest.log4py.set_target("$HOME/log4py-test.log")
mytest.run()
mytest.log4py.set_target(sys.stdout)

print "\nNormal level - Long format (ansi color)\n"
mytest.log4py.set_use_ansi_codes(log4py.TRUE)
mytest.run()
mytest.log4py.set_use_ansi_codes(log4py.FALSE)

print "\nDebug level - Debug format\n"
mytest.log4py.set_formatstring(log4py.FMT_DEBUG)
mytest.log4py.set_loglevel(log4py.LOGLEVEL_DEBUG)
mytest.run()

print "\nVerbose level - Medium format\n"
mytest.log4py.set_formatstring(log4py.FMT_MEDIUM)
mytest.log4py.set_loglevel(log4py.LOGLEVEL_VERBOSE)
mytest.run()

print "\nVerbose level - User defined format\n"
mytest.log4py.set_formatstring("[ %u (%F) ] %D: %M")
mytest.log4py.set_loglevel(log4py.LOGLEVEL_VERBOSE)
mytest.run()

print "\nNormal, long format - Testing Nested Diagnostic Context\n"
mytest.log4py.set_formatstring(log4py.FMT_LONG)
mytest.log4py.set_loglevel(log4py.LOGLEVEL_VERBOSE)
mytest.log4py.push("ndc1")
mytest.output("Should say \"ndc1\"");
mytest.log4py.push("ndc2")
mytest.output("Should say \"ndc1 ndc2\"");
mytest.log4py.pop()
mytest.output("Should say \"ndc1\"");
mytest.log4py.push("ndc3")
mytest.output("Should say \"ndc1 ndc3\"");
mytest.log4py.clear_ndc();
mytest.output("Should not have any ndc items");

print "\nTesting MySQL target\n"
mytest.log4py.add_target(log4py.TARGET_MYSQL, "localhost", "syslog", "log4py", "mysecretpwd", "logs")
mytest.output("hello world")
mytest.log4py.remove_target(log4py.TARGET_MYSQL)

print "\nTesting Syslog target\n"
mytest.log4py.add_target(log4py.TARGET_SYSLOG)
mytest.run()
mytest.log4py.remove_target(log4py.TARGET_SYSLOG)

print "\nGetting all available targets\n"
print mytest.log4py.get_targets()

print "\nTesting log-file rotation (log4py-rotation.log)\n"
mytest.log4py.set_target("log4py-rotation.log")
mytest.run()
mytest.log4py.set_rotation(log4py.ROTATE_DAILY)
yesterday = time() - 60 * 60 * 24
utime("log4py-rotation.log", (yesterday, yesterday))
mytest.run()
mytest.log4py.set_target(sys.stdout)
