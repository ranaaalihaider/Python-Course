import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

class WebView(QMainWindow):
    def __init__(self, url):
        super().__init__()

        # Initialize the web engine settings
        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        # Create a QtWebEngineView widget
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl(url))

        # Set the web view as the central widget
        self.setCentralWidget(self.web_view)

        # Set the window properties
        self.setWindowTitle("AI CHAT")  # Modify the title here
        self.setGeometry(100, 100, 800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    url_to_open = "https://chat.openai.com/"  # Replace with the URL of the website you want to display
    app_window = WebView(url_to_open)
    app_window.show()
    sys.exit(app.exec_())
