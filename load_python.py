#
# Hints from
# http://www.python-forum.de/viewtopic.php?f=25&t=31940
#

from ctypes import cdll
import os
from shutil import copyfile
from tempfile import NamedTemporaryFile

class Session(object):

	def __init__(self):
		self.create_private_dll_handle()

	def load_dll(self, path):
		print "load_dll with %s" % (path)
		a = cdll.LoadLibrary(path)
		return a

	def create_private_dll_handle(self):
		self.private_path = self.create_private_dll_name()
		self.create_private_dll()
		self.handle = self.load_dll(self.private_path)

	def create_private_dll_name(self):
		self.path = self.get_cddl()
		namedTempFile = NamedTemporaryFile(prefix='libfoo_', suffix='.so')
		private_path = namedTempFile.name

		return private_path

	def create_private_dll(self):
		print "copy %s to %s" % (self.path, self.private_path)
		copyfile(self.path, self.private_path)

	def get_cddl(self):
		path = os.path.dirname(__file__)
		path = os.path.abspath(path)
		path = os.path.join(path, 'cdll', 'libfoo.so')

		return path


def main():
	a = Session()
	b = Session()

	print a.handle
	print b.handle

if __name__ == '__main__':
	main()
