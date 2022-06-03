# import schedule
# from time import sleep

#01 定期実行する関数を準備
# def task():
#     print("タスク実行中")

# 円債import
import mufg_J
import sbi_J

# 外債import
import smbc
import rakuten
import mufg
import hs

# 円債加工
import mufg_J_p
import SBI_J_p

# 外債加工
import SMBC_p
import rakuten_p
import MUFG_p
import hs_p

#出力
import p_data_all_j
import p_data_all

#02 スケジュール登録
# schedule.every().days.at("11:18").do(task)


# #03 イベント実行
# while True:
#     schedule.run_pending()
#     sleep(1)