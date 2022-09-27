#!/usr/bin/env python3

import argparse
import sys
import webbrowser
from urllib.request import urlopen

parser = argparse.ArgumentParser(description='Open a jnu.edu.cn URL with WeChat authentication.')
parser.add_argument('url', help='URL to open in the default browser')
args = parser.parse_args()

with urlopen(args.url) as f:
    for line in f:
        if b'verifyID' in line:
            verifyID = line.decode().split('%3D')[-1].split('&')[0].split('"')[0]
            print(line)
            webbrowser.open(f'https://weixinfwh.jnu.edu.cn/wechat_auth/wechat/wechatClientAsync?verifyID={verifyID}')
            sys.exit(0)

sys.stderr.write('No verifyID found in the response. Fall back to the origin URL.\n')
webbrowser.open(args.url)