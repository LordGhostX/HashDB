#HashDB
#Author - LordGhostX

from event_logger import event_log
from writer import write
from reader import load
from finder import find
from cloner import clone
from deleter import delete

def banner():
	print("""#
#   ██╗ ██╗  █████╗ ███████╗██╗  ██╗      ██████╗ ██████╗ 
#  ████████╗██╔══██╗██╔════╝██║  ██║      ██╔══██╗██╔══██╗
#  ╚██╔═██╔╝███████║███████╗███████║█████╗██║  ██║██████╔╝
#  ████████╗██╔══██║╚════██║██╔══██║╚════╝██║  ██║██╔══██╗
#  ╚██╔═██╔╝██║  ██║███████║██║  ██║      ██████╔╝██████╔╝
#   ╚═╝ ╚═╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═════╝ 
#""")
		
version = "HashDB v0.0.3"

event_log("HashDB Successfully Connected!", 0)