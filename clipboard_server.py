from flask import Flask, request, jsonify
import pyperclip
import subprocess

app = Flask(__name__)

# Endpoint to copy content to clipboard
@app.route('/copy', methods=['POST'])
def copy_to_clipboard():
    content = request.form['content']
    print(content)
    process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
    process.communicate(input=content.encode())
    return jsonify({'status': 'success', 'message': 'Content copied to clipboard'}), 200

# Endpoint to get content from clipboard
@app.route('/paste', methods=['GET'])
def paste_from_clipboard():
    content = pyperclip.paste()
    return jsonify({'content': content}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
