import json
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_json_data(self):
        with open('list_json.json','r') as json_file:
            return json.load(json_file)

    def __save_json_data(self, json_data):
        with open('list_json.json', 'w') as json_file:
            return json.dumps(json_data, json_file)

    def do_POST(self):
        c_len = int(self.headers.get('Content-Length'))
        client_data = self.rfile.read(c_len)
        client_data = client_data.decode()

        json_data = self.__get_json_data()
        json_data.append(client_data)
        self.__save_json_data()

        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(f'{self.json_data}', "utf-8"))


    def do_GET(self):

        json_content = json.dumps("Hello, World wide web")

        print(json_content)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")