
rm -rf bot1 
mkdir bot1
git clone https://github.com/eternnoir/pyTelegramBotAPI.git
cd pyTelegramBotAPI
python setup.py install
git clone --recursive https://github.com/PassionSasha/bot_lab.git
cd /usr/local/bin/bot1 && git clone --recursive https://github.com/PassionSasha/bot_lab.git
