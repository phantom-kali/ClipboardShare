from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
import requests

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "Clipboard Share"

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)

        MDTextField:
            id: ip_input
            hint_text: "Enter Server IP"

        MDTextField:
            id: clipboard_input
            hint_text: "Enter text to share"

        MDRaisedButton:
            text: "Send to Server"
            on_release: app.send_to_server()

        MDRaisedButton:
            text: "Paste from Server"
            on_release: app.paste_from_server()

        MDTextField:
            id: clipboard_output
            hint_text: "Clipboard content will appear here"
            readonly: True
'''

class ClipboardShareApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def send_to_server(self):
        ip_input = self.root.ids.ip_input
        clipboard_input = self.root.ids.clipboard_input

        server_ip = ip_input.text
        text = clipboard_input.text

        try:
            response = requests.post(f"http://{server_ip}:5000/copy", data={"content": text})
            if response.status_code == 200:
                self.show_alert("Success", "Content sent to server")
        except Exception as e:
            self.show_alert("Error", f"Failed to send content: {e}")

    def paste_from_server(self):
        ip_input = self.root.ids.ip_input
        clipboard_output = self.root.ids.clipboard_output

        server_ip = ip_input.text

        try:
            response = requests.get(f"http://{server_ip}:5000/paste")
            if response.status_code == 200:
                content = response.json().get("content")
                clipboard_output.text = content
                self.show_alert("Success", "Content pasted from server")
        except Exception as e:
            self.show_alert("Error", f"Failed to paste content: {e}")

    def show_alert(self, title, message):
        dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()

ClipboardShareApp().run()
