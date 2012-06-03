Log4Py ReadMe:

Log4Py is a Python logging module similar to log4j. It supports multiple levels
of logging and configurable output (either to stdout/stderr or to files). A
list of available format strings and ouput parameters can be found at the
beginning of log4py.py.

Installation:

    Automatic:
        Using Python's Distutils, you can execute:
        "python setup.py install"

    Manually:
        Either copy log4py.py into your project directory or to your site-packages directory.

Usage:

    from log4py import Logger

    class foo:
        def __init__(self):
	    cat = Logger().get_instance(self)

    Have a look at log4py-test.py and log4py-classtest.py for examples.
    For logging to databases, please have a look at the database/ directory

If you have any comments or questions, don't hesitate to contact me ;-)

Martin 						<Martin.Preishuber@eclipt.at>
