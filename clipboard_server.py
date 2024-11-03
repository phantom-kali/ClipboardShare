from flask import Flask, request, jsonify
import socket
import netifaces
import threading
import time
import pyperclip
import subprocess

app = Flask(__name__)

def get_local_ips():
    """Get all local IP addresses of the machine."""
    ips = []
    interfaces = netifaces.interfaces()
    
    for interface in interfaces:
        addrs = netifaces.ifaddresses(interface)
        # Get IPv4 addresses
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                ip = addr['addr']
                # Filter out localhost
                if not ip.startswith('127.'):
                    ips.append(ip)
    return ips

@app.route('/info')
def get_info():
    """Endpoint that returns server information."""
    hostname = socket.gethostname()
    ips = get_local_ips()
    return jsonify({
        'hostname': hostname,
        'ips': ips
    })

@app.route('/copy', methods=['POST'])
def copy_to_clipboard():
    """Endpoint to copy content to clipboard"""
    content = request.form['content']
    print(f"Received content to copy: {content}")
    
    try:
        process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
        process.communicate(input=content.encode())
        return jsonify({
            'status': 'success',
            'message': 'Content copied to clipboard'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to copy to clipboard: {str(e)}'
        }), 500

@app.route('/paste', methods=['GET'])
def paste_from_clipboard():
    """Endpoint to get content from clipboard"""
    try:
        content = pyperclip.paste()
        return jsonify({
            'status': 'success',
            'content': content
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to paste from clipboard: {str(e)}'
        }), 500

def broadcast_presence():
    """Broadcast UDP packets to announce server presence."""
    BROADCAST_PORT = 12345
    MESSAGE = b"CLIPBOARD_SERVER"
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    while True:
        try:
            sock.sendto(MESSAGE, ('<broadcast>', BROADCAST_PORT))
            time.sleep(1)  # Broadcast every second
        except Exception as e:
            print(f"Broadcast error: {e}")

if __name__ == '__main__':
    # Start broadcasting in a separate thread
    broadcast_thread = threading.Thread(target=broadcast_presence, daemon=True)
    broadcast_thread.start()
    
    print("Starting clipboard sharing server...")
    print("Available on these IPs:", get_local_ips())
    
    # Run Flask server
    app.run(host='0.0.0.0', port=5000)