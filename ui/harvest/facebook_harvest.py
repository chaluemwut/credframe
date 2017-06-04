from __future__ import print_function
import argparse
import mechanicalsoup
from getpass import getpass


browser = mechanicalsoup.StatefulBrowser()

browser.open("https://www.facebook.com/")
browser.select_form('#login_form')
browser["email"] = 'chaluemwut@hotmail.com'
browser["pass"] = 'Rvpooh123'
resp = browser.submit_selected()

browser.open('https://www.facebook.com/ThairathFan/posts/10155712834602439/')
page = browser.get_current_page()
print(page.soup)