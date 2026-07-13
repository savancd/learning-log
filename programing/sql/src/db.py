# import library
import sqlite3
from pathlib import Path

# the path where will file be created
# it's gonna create a file inside root parent dir
DB_PATH = Path(__file__).resolve().parent.parent / "job_intel.db"


# in this step database should be open from the path that is previusly created - DB_PATH
def connection():
	# it should be stored in variable and the path should be called
	conn = sqlite3.connect(DB_PATH)
	# send the sql
	# PRAGMA is database settigns
	
