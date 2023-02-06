import subprocess, shlex

def call_browser(url):
    cmd = 'chromium-browser ' + url + ' --kiosk --incognito'
    args = shlex.split(cmd)
    ret = subprocess.call(args)
