import platform

os_name = platform.system()

base_url="https://the-internet.herokuapp.com/"
implicit_timeout=10
explicit_timeout=10
if os_name == "Windows":
    chromedriver_path="../driver/windows/chromedriver"
if os_name == "Linux":
    chromedriver_path = "../driver/linux/chromedriver"