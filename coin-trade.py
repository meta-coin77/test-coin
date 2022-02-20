import time
import pyupbit
import datetime

access = "khxk0j7B5stmg4FfcjVIBxBifOANs72Vo9gxlDgt"
secret = "KONmoaU51hldNBO4g714Bpj6fWaDKPq53a1zHV36"

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-SAND")
        end_time = start_time + datetime.timedelta(minutes=3)

        # 9:00 < 현재 < 8:59:50
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-SAND", 0.2)
            current_price = get_current_price("KRW-SAND")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-SAND", krw*0.999)
        else:
            sand = get_balance("SAND")
            if sand > 0.00008:
                upbit.sell_market_order("KRW-SAND", sand)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)