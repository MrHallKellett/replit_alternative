import sqlite3
from config import *

class Database:

	def  __enter__(self):
		self.__connection = sqlite3.connect(DB_FILENAME)
		self.__cursor = self.__connection.cursor()
		return self

	def __exit__(self, type, value, traceback):
		self.__connection.close()

	def execute(self, query, values=None, one_row=False):

			
		if values:
			val_copy = list(values)
			q_debug = query
			while val_copy:
				q_debug = q_debug.replace("?", str(val_copy.pop(0)), 1)
		
			print("PROCESSING QUERY:", q_debug)
			results = self.__cursor.execute(query, values)
		else:
			results = self.__cursor.execute(query)
		self.__connection.commit()
		if one_row:
			result = results.fetchone()
			print("returning", result)
			return result
		else:
			return results.fetchall()
		