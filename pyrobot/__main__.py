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
    
    
user_session_string = "BQCQX5yd3ipFkANBGiquKBfn851U9-i_rl9By2pDVU59RdgBayy8-sX5ape6oPisaQDpZCgBDHQwO1BkbP6IxecUrAOgcWnfNZGt_khgJqTZIsri5X4aYjXJKW0XETfQxMhYV4ZRYfjhE_Nle8jXKnw_pOifsQ9C0HhySsgvcs3Mxrup8fW4i07fxFjCMM2iN24G9xvC90jhUs8Nib7kkdwtid_-7jell2cge_I7CKDhA9W79NJLok755_maoI1GPG2hcWGTb6w3bqr43lHNC6rsM-LR_zmLBW0OkDTrO7xD1DDNtvhsvBAaBZReTI5-m2415F45GF7r6-19oqCkBpDJUbEaEQA"
bots = ["WhiteEyeRenameBot"]
bot_owner = ("@Mr_StarLords")
update_channel = ("@WhiteEyeBotsChat")
status_message_id = ("926856350")
api_id = ("2412622")
api_hash = ("fa25ca6c7d6723ea717eee08e6af6565")

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
