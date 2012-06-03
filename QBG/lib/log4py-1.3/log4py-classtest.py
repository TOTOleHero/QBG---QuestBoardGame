#!/usr/bin/env python

"""Test class for log4py.

You should get output like this:
--------
20-10-2001 21:19 sharedlog.__init__ [DEBUG]- Shared log instantiated
20-10-2001 21:19 Main.get_instance [DEBUG]- Instantiated
20-10-2001 21:19 Main.Main [INFO]- in main
20-10-2001 21:19 c1.get_instance [DEBUG]- Instantiated
20-10-2001 21:19 c1.__init__ [INFO]- in c1
20-10-2001 21:19 c2.get_instance [DEBUG]- Instantiated
20-10-2001 21:19 c2.__init__ [INFO]- in c2
20-10-2001 21:19 c1.__init__ [INFO]- in c1
--------

Author: Bruce Kroeze <bruce@zefamily.org>
"""

from log4py import Logger, LOGLEVEL_DEBUG

class c1:
    def __init__(self):
        log = Logger().get_instance(self)
        log.info("in c1")

class c2:
    def __init__(self):
        log = Logger().get_instance(self)
        log.info("in c2")

if (__name__ == '__main__'):
    log = Logger("$HOME/log4py.conf").get_instance()
    log.get_root().set_loglevel(LOGLEVEL_DEBUG)
    log.info("in main")

    a = c1()
    b = c2()
    c = c1()
