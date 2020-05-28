# PY_youtube_downloader_2020
    The code is pretty ugly but it's because there's a lot of random advertisements on yt downloaders website.
    So in order to handle the advertisement I had a lot of ugly try instruction.
    It's ugly BUT everything work ;)

    Things you need to use it :
        Youtube existing playlist.
        Firefox.
        Selenium (and geckodriver).

    Youtube :
        Build a publique/not referenced playlist add some musique or find an existing playlist.
        Change the 'self.url' variable in the download.py file with your playlist link.

    Firefox :
        Linux :
            sudo apt-get Firefox or sudo dnf install Firefox
        Mac :
            brew install homebrew/cask/firefox

    Selenium
        Linux :
            pip install selenium or pip3 install selenium or
            pip install selenium --user or pip3 install selenium --user
        Mac :
            brew install selenium-server-standalone or sudo easy_install selenium

    Geckodriver
        Download manually here : https://github.com/mozilla/geckodriver/releases
        Extract it in a folder (personnaly I put it in the selenium dir in /.../python/library/...):
            tar -xvzf geckodriver*
            remember where you extract it for the path
        Export in path (bashrc/zshrc/...):
            export PATH=$PATH:/path-to-geckodriver/


    I made it for my sister so I hope you will enjoy it.