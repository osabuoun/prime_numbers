from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse, json, time, ast, random, os
from pprint import pprint
from threading import Thread

class HTTP(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		data = None
		binary = None
		html_file = open('./index.html','r')
		response = html_file.read()
		html_file.close()
		#print(response)
		binary = bytes(json.dumps(response),"utf-8")

		self._set_headers()
		self.wfile.write(binary)

	def do_HEAD(self):
		self._set_headers()
		
	def do_POST(self):
		#pprint(vars(self))
		# Doesn't do anything with posted data
		content_length= None
		data_json = None
		data =None
		filedir = './www/'
		try:
			if (self.path):
				filedir = filedir + self.path 
				if (not os.path.isdir(filedir)):
					os.makedirs(filedir)

			filedir = filedir + '/R_'
			content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
			data = self.rfile.read(int(content_length)).decode('utf-8')
			print('data' + str(data))
			data_json = ast.literal_eval(data)
			print('data_json : ' + str(data_json))
		except Exception as e:
			print("Error in parsing the content_length and packet data")
			raise e
		#data_back = ""

		#if (self.path == ''):

			
		#print('data_json' + str(data))
		html_file = open(filedir + str(data_json['worker_id']) +'.html','a')
		html_file.write("<p>" + str(data_json) + "<p><br>")
		html_file.close()
		data_back = "received"
		print("------------------ Finished ---------------")
		
		self._set_headers()
		self.wfile.write(bytes(str(data_back), "utf-8"))


def start_server(port=8081):
	server_address = ('', port)
	httpd = HTTPServer(server_address, HTTP)
	print('Starting HTTP Server...' + str(port))
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		print("***** Error in HTTP Server *****")
		pass

	httpd.server_close()
	print(time.asctime(), "Experiment Manager Server Stopped - %s:%s" % (server_address, port))

if __name__ == '__main__':
	http_server_thread = Thread(target = start_server, args = ())
	http_server_thread.start()