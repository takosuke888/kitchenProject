import subprocess, shlex

def call_browser(args):
    some = 0
    ret = subprocess.call(args)