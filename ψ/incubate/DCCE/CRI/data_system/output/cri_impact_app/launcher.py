import streamlit.web.cli as stcli
import os, sys
import webbrowser
from threading import Timer

def resolve_path(path):
    base_path = getattr(sys, '_MEIPASS', os.getcwd())
    return os.path.join(base_path, path)

def open_browser():
    """ Explicitly open the browser to the streamlit port """
    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    # Point to the bundled app.py
    app_path = resolve_path("app.py")
    
    # Schedule the browser to open after 3 seconds
    Timer(3.0, open_browser).start()
    
    # Bootstrap Streamlit
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--global.developmentMode=false",
        "--server.port=8501",
        "--server.headless=true"
    ]
    sys.exit(stcli.main())
