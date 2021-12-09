from pytwitcasting.auth import TwitcastingApplicationBasis
from pytwitcasting.api import API
from config import client_id, client_secret, user_id, search_context, call_time
import winsound
import time
import datetime

dt_log = datetime.datetime.now()
# 配信画面いくつも開いたりアラートいくつも鳴らないようにcall_time分だけタスク待機させる
crnt = int(time.time())
call_timestamp = 60 * call_time

with open('exist.txt', 'r') as f:
    line = f.read()
    diff = int(line)
    # diff = int(f.read)
    call_time = crnt - diff - call_timestamp
    if call_time < 0:
        print("[alert] 12時間以内に配信やってるよ")
        with open('res.log', "a", encoding='utf-8') as f:
            f.write(dt_log.strftime('%Y年%m月%d日%H時%M分%S秒') + " res 2\n")
        exit(2)

with open('sample.wav', 'rb') as f:
    data = f.read()
app_basis = TwitcastingApplicationBasis(client_id=client_id,
                                        client_secret=client_secret)
api = API(application_basis=app_basis)
# デバッグ時に便利。その配信者本当に存在するかどうか？の検索
# d = vars(api.get_user_info(user_id))
# for t in sorted(d.items()):
#     print('{}: {}'.format(t[0], t[1]))

d = api.search_live_movies(search_type='word', context=search_context)
# print(d['movies'])

if len(d['movies']) > 2:
    winsound.PlaySound(data, winsound.SND_MEMORY)
    print("[alert] ツイキャス始まってるよ")
    with open('res.log', "a", encoding='utf-8') as f:
        f.write(dt_log.strftime('%Y年%m月%d日%H時%M分%S秒') + " res 1\n")
    with open('exist.txt', "w", encoding='utf-8') as f:
        f.write(str(crnt))
    exit(1)
with open('res.log', "a", encoding='utf-8') as f:
    f.write(dt_log.strftime('%Y年%m月%d日%H時%M分%S秒') + " res 0\n")
exit(0)
