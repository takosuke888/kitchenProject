import subprocess, shlex

def call_browser(args):
    ret = subprocess.call(args)