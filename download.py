#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common import keys
import time
import random

class Bot:
    def __init__(self):
        self.url = "LINK OF YOUR PLAYLIST" # self.url = "https://www..."
        self.downloader_url = "https://mp3-youtube.download/en/fast-youtube-converter"
        self.prefix = "https://youtu.be/"
        self.page = webdriver.Firefox()
        self.page.get(self.url)
        self.final_link = []

    def sleeping(self, sleep):
        for i in range(sleep):
            time.sleep(1)
            print("Sleeping " + str(i + 1) + " / " + str(sleep) + " seconds\n")

    def get_link(self):
        to_download = []
        suffix = []

        hrefs = self.page.find_elements_by_tag_name('a')
        song_hrefs = [elem.get_attribute('href') for elem in hrefs]
        song_hrefs = [href for href in song_hrefs]
        for song_href in song_hrefs :
            try:
                if "watch" in song_href and "index" in song_href and song_href not in to_download:
                    to_download.append(song_href)
            except Exception as e:
                pass
        suffix = [i.replace("https://www.youtube.com/watch?v=", self.prefix) for i in to_download]
        to_download = [i.replace("https://www.youtube.com/watch?v=", "") for i in suffix]
        suffix.clear()
        for link in to_download:
            save, trash, trash1 = link.partition("&")
            self.final_link.append(save)

    def close_pub(self):
        try:
            buton = self.page.find_element_by_id("LabsIFrameCloseButton")
            buton.click()
        except Exception as e:
            pass

    def downloading(self, link, deep):
        try:
            self.page.get(self.downloader_url)
            btn = self.page.find_element_by_class_name('input-group')
            self.close_pub()
            btn.click()
            self.close_pub()
            btn = self.page.find_element_by_class_name('form-control')
            self.close_pub()
            btn.click()
            self.sleeping(random.randrange(15, 30))
            self.close_pub()
            btn.send_keys(link)
            self.close_pub()
            btn.send_keys(keys.Keys.RETURN)
            self.sleeping(random.randrange(30, 60))
            self.close_pub()
            try:
                btn = self.page.find_element_by_class_name('btn')
                self.close_pub()
                btn.click()
            except Exception as e:
                if deep == False:
                    self.downloading(link, True)
            self.sleeping(random.randrange(60, 120))
            self.close_pub()
            btn = self.page.find_element_by_class_name('btn')
            self.close_pub()
            btn.click()
        except Exception as e:
            pass

def main():
    bot = Bot()

    bot.sleeping(random.randrange(5, 30))
    bot.get_link()
    for link in bot.final_link:
        bot.downloading(link, False)
    bot.sleeping(random.randrange(60, 120))
    bot.page.close()
    print("END")

main()