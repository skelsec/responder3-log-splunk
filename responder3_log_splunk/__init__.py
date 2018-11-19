# Works with Python 3.7
import asyncio
import traceback
import json

from responder3.core.logging.logtask import LoggerExtensionTask
from responder3.core.logging.logger import Logger, r3exception
from responder3.core.logging.log_objects import *
from responder3.core.commons import UniversalEncoder

class splunkHandler(LoggerExtensionTask):
	def init(self):
		try:
			self.retry_timeout = 10
			self.splunk_ip = self.config['splunk_ip']
			self.splunk_port = self.config['splunk_port']
			if 'retry_timeout' in self.config:
				self.retry_timeout = self.config['retry_timeout']

		except Exception as e:
			traceback.print_exc()

	async def setup(self):
		pass

	async def main(self):
		while True:
			try:
				await self.logger.info('Connecting to Splunk')
				reader, writer = await asyncio.open_connection(self.splunk_ip, self.splunk_port)
				await self.logger.info('Connected to Splunk!')
				while not reader.at_eof():
					msg = await self.result_queue.get()
					ul = UnifiedLog.construct(msg)
					try:
						logline = ul.to_json().encode() + b'\r\n'
					except:
						await self.logger.exception()
					else:
						writer.write(logline)
						await writer.drain()


			except Exception as e:
				await self.logger.exception()

			await self.logger.info('Connection lost! Reconnecting in %ss' % self.retry_timeout)
			await asyncio.sleep(self.retry_timeout)

