from flask import Flask, request
from zeroconf import ServiceInfo, Zeroconf
import socket
import webbrowser
import urllib.parse

app = Flask(__name__)

@app.route('/open')
def open_url():
    raw = request.args.get('url', '')
    url = urllib.parse.unquote(raw)
    if url:
        webbrowser.open(url)
    return "Opened: " + url

if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    zeroconf = Zeroconf()
    service_info = ServiceInfo(
        "_http._tcp.local.",
        "SendToLaptop._http._tcp.local.",
        addresses=[socket.inet_aton(local_ip)],
        port=5000,
        properties={},
        server="sendtolaptop.local."
    )
    zeroconf.register_service(service_info)

    print(f"Service available as http://sendtolaptop.local:5000")

    app.run(host="0.0.0.0", port=5000)
