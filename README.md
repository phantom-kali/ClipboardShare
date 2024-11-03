# ClipboardShare

**ClipboardShare** is a simple server-client application designed to facilitate clipboard sharing across devices on the same network. The repository provides an Android app (`ClipboardShare.apk`) to connect to the server, allowing easy clipboard content transfer between Android devices and computers.


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/phantom-kali/ClipboardShare.git
   cd ClipboardShare
   ```

2. **Install Python Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure `xclip` is Installed (Linux Only)**

   For Linux users, install `xclip` to handle clipboard operations:
   
   ```bash
   sudo apt install xclip
   ```

## Usage

1. **Start the Server:**

   Run the Python script to start the server:

   ```bash
   python clipboard_server.py
   ```

   The server will begin broadcasting its presence on the network and will be available on all local IP addresses, which will be displayed in the console.

2. **Connect Using the Android App:**

   Install and open the Android app (`ClipboardShare.apk`) on your device. It will detect the server broadcast and allow you to connect to it.


## Notes

- This server currently only supports text-based clipboard sharing.
- Make sure your firewall settings allow connections on the specified port (`5000` for Flask, `12345` for UDP broadcast).

