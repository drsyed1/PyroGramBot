#  Copyright (c) 2019-2020 Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without
#  limitation the rights to use, copy, modify, merge, publish,
#  distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be
#  included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#  OTHER DEALINGS IN THE SOFTWARE.

from .pyrobot import PyroBot

import os
import time
import datetime

import pyrogram

if __name__ == "__main__":
    PyroBot().run()
    
    
user_session_string = os.environ.get("1BVtsOHwBuwqrsinlWxs5au0hdAmI3kcYtpy5BK97xaZda6EDkiEIA90r0bnjM6A6yVjxfBRKDfzkifyOSIccS5MqoiCNPD_3cb1b8Ox4htuyKpOtSZpbtxyO6iM2k73uUMEBzd4f1eu9mqufc1nH2MkMjo_F4XAGTnyNwZ1U876CX9yYTr0sM0bRMCQ9nz8U_00wJwbINrCtTJwhckVqiVEzy7FjmKF2swH5wJw89VgXDGjZ53kC6j2GceYeuMhdXr1xsM557XWjznTWsvVUoKG4MF2jM0XYwOwnfJmqLi5Z3uUUggXnT2OGjvi9wjB-P-dYne5JbYMcxmRP28mq9oP4DDOYmso=")
bots = [i.strip() for i in os.environ.get("@WhiteEyeRenameBot, @WhiteEyeUrlUploaderBot, @WhiteEyeYouTubeBot, @WhiteEyeDeleteAllBot, @WhiteEyeCompressorBot, @Miss_ArantxaBot, @WhiteEyeSubtitleBot, @WhiteEyeLinkToFileBot, @WhiteEyeGDriveBot, @WhiteEyeTelegraphBot, @WhiteEyeForceSubscriberBot, @WhiteEyeUltraTonBot, @WhiteEyeTagRemoverBot").split(' ')]
bot_owner = os.environ.get("@Mr_StarLords")
update_channel = os.environ.get("-1001484903966")
status_message_id = int(os.environ.get("status_message_id"))
api_id = int(os.environ.get("1715074"))
api_hash = os.environ.get("0c8fb6a43409019900aa98f439eceec4")

user_client = pyrogram.Client(
    user_session_string, api_id=api_id, api_hash=api_hash)


def main():
    with user_client:
        while True:
            print("[INFO] starting to check uptime..")
            edit_text = f"@{update_channel} Bot's Uptime Status.(Updated every 15 mins)\n\n"
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                snt = user_client.send_message(bot, '/start')

                time.sleep(15)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    edit_text += f"@{bot} status: `Down`\n\n"
                    user_client.send_message(bot_owner,
                                             f"@{bot} status: `Down`")
                else:
                    print(f"[INFO] all good with @{bot}")
                    edit_text += f"@{bot} status: `Up`\n\n"
                user_client.read_history(bot)

            utc_now = datetime.datetime.utcnow()
            ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)

            edit_text += f"__last checked on \n{str(utc_now)} UTC\n{ist_now} IST__"

            user_client.edit_message_text(update_channel, status_message_id,
                                         edit_text)
            print(f"[INFO] everything done! sleeping for 15 mins...")

            time.sleep(15 * 60)


main()    
