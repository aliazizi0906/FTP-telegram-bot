import os

#API ID & API Hash -----> my.telegram.org
api_id = 0000000 
api_hash = 'e28cc5d85c66rr785422fe3bf50e61f'

#Bot Token -----> @BotFather
token = '8569471455:JJkiyA6MmuB570F4t5yVLmi92tWRqQi6rty'

#Session Name -----> optional
session_name = 'FTP_Manager'


#The robot admin (the person who can give orders to the robot.) -----> @myidbot
admins = [1117638015,1117638015,1117638015]

# Chat id to send technical logs
dev = 1117638015

# When a file is sent to the bot, first that file is downloaded from the Telegram repository and stored in the bot's server.
# Here you need to specify its temporary storage path
# For example, I set the bot to save the downloaded file in the current path (the path where config.py file is located).
dl_path = os.path.abspath(os.getcwd()) + '/'


# The upload path where we give FTP access to the bot.
ftp_path = '/public_html/Bot/'

# The files are temporarily downloaded after they are on the bot server. They are uploaded to another host through FTP.
# Here we have to give FTP access to the bot.
ftp_ip = '95.136.117.620'
ftp_username = 'FTP@domain.com'
ftp_password = '12345678'
ftp_domain = 'https://domain.com/Bot/'
