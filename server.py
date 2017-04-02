import paho.mqtt.publish as publish
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		print(self.path)
		try:
			if self.path is "/":
				# Response headers
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				# Response contents
				with open('index.html', 'rb') as home_page:
					self.wfile.write(home_page.read())
				return

			elif self.path.endswith("/motor/on"):
				# Action
				publish.single("/MOTOR", "ON", 0, False, "192.168.56.198", "1883")

				# Response headers
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				# Response content
				with open('on.html', 'rb') as on_page:
					self.wfile.write(on_page.read())
				return

			elif self.path.endswith("/motor/off"):
				# Action : Stop Motor
				publish.single("/MOTOR", "OFF", 0, False, "192.168.56.198", "1883")

				# Response headers
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				# Response content
				with open('off.html', 'rb') as off_page:
					self.wfile.write(off_page.read())

				return
		except IOError:
			self.send_error(404, "File not found %s" % self.path)
def main():
	try:
		ip = "192.168.56.198"
		port = 8080
		server = HTTPServer((ip, port), webserverHandler)
		print("Server started on port %s" % (port))
		server.serve_forever()
	except KeyboardInterrupt:
		print("Server stopped!")
		server.socket.close()

if __name__ == '__main__':
	main()
