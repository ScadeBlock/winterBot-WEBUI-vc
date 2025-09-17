# PROTOCOL = "http://"
# PROTOCOL = "https://"
# SERVER_IP = "bplans0.onrender.com"
from os.path import exists
from psutil import cpu_percent,virtual_memory
with open("data.txt","r") as f:
    m = f.read().split("\n")
    PROTOCOL = m[0]
    SERVER_IP = m[1]
del m
from datetime import datetime,timedelta
from random import randint,choice
from time import sleep,time
from requests import get,post
from re import search
from threading import Thread
from hashlib import md5
from time import time as T
import secrets
def human_readable_size(size_bytes: float, decimal_places: int = 2) -> str:
    """
    Convert a size in bytes into a human-readable string 
    with the most appropriate unit (KB, MB, GB, TB...).

    Args:
        size_bytes (float): The size in bytes.
        decimal_places (int): Number of decimal places for formatting.

    Returns:
        str: Human-readable size string.
    """
    if size_bytes < 0:
        raise ValueError("Size must be non-negative")
    if size_bytes == 0:
        return "0 B"

    units = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024
        i += 1
    return f"{size_bytes:.{decimal_places}f} {units[i]}"
def multi_thread(func):
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args)
        thread.start()
        return thread
    return wrapper
listd = []
getlink = False
total = succedd = failed = 0
class Signature:
    def __init__(self, params: str, data: str, cookies: str) -> None:

        self.params = params
        self.data = data
        self.cookies = cookies

    def hash(self, data: str) -> str:
        return str(md5(data.encode()).hexdigest())

    def calc_gorgon(self) -> str:
        gorgon = self.hash(self.params)
        if self.data:
            gorgon += self.hash(self.data)
        else:
            gorgon += str("0"*32)
        if self.cookies:
            gorgon += self.hash(self.cookies)
        else:
            gorgon += str("0"*32)
        gorgon += str("0"*32)
        return gorgon

    def get_value(self):
        gorgon = self.calc_gorgon()

        return self.encrypt(gorgon)

    def encrypt(self, data: str):
        unix = int(T())
        len = 0x14
        key = [
            0xDF,
            0x77,
            0xB9,
            0x40,
            0xB9,
            0x9B,
            0x84,
            0x83,
            0xD1,
            0xB9,
            0xCB,
            0xD1,
            0xF7,
            0xC2,
            0xB9,
            0x85,
            0xC3,
            0xD0,
            0xFB,
            0xC3,
        ]

        param_list = []

        for i in range(0, 12, 4):
            temp = data[8 * i : 8 * (i + 1)]
            for j in range(4):
                H = int(temp[j * 2 : (j + 1) * 2], 16)
                param_list.append(H)

        param_list.extend([0x0, 0x6, 0xB, 0x1C])

        H = int(hex(unix), 16)

        param_list.append((H & 0xFF000000) >> 24)
        param_list.append((H & 0x00FF0000) >> 16)
        param_list.append((H & 0x0000FF00) >> 8)
        param_list.append((H & 0x000000FF) >> 0)

        eor_result_list = []

        for A, B in zip(param_list, key):
            eor_result_list.append(A ^ B)

        for i in range(len):

            C = self.reverse(eor_result_list[i])
            D = eor_result_list[(i + 1) % len]
            E = C ^ D

            F = self.rbit(E)
            H = ((F ^ 0xFFFFFFFF) ^ len) & 0xFF
            eor_result_list[i] = H

        result = ""
        for param in eor_result_list:
            result += self.hex_string(param)

        return {"X-Gorgon": ("840280416000" + result), "X-Khronos": str(unix)}

    def rbit(self, num):
        result = ""
        tmp_string = bin(num)[2:]

        while len(tmp_string) < 8:
            tmp_string = "0" + tmp_string

        for i in range(0, 8):
            result = result + tmp_string[7 - i]

        return int(result, 2)

    def hex_string(self, num):
        tmp_string = hex(num)[2:]

        if len(tmp_string) < 2:
            tmp_string = "0" + tmp_string

        return tmp_string

    def reverse(self, num):
        tmp_string = self.hex_string(num)

        return int(tmp_string[1:] + tmp_string[:1], 16)

class Kaffeine():
    def __init__(self,app):
        self.count = 0
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36' }
        
        if SERVER_IP:
            self.HOSTLINK = PROTOCOL + SERVER_IP
            self.kaffeine_reply(self.HOSTLINK)
        else:
            self.HOSTLINK = None
        @app.route("/kaffeine_port") 
        async def KP(request):
            print("[KAFFEINE] Received")
            return response.text("KAFFEINE V2.99 . OK")

    @multi_thread
    def kaffeine_reply_fnc(self):
        if self.HOSTLINK:HOSTLINK = self.HOSTLINK
        print("[KAFFFEINE] Send to",HOSTLINK + "/kaffeine_port")
        get(HOSTLINK + "/kaffeine_port")
    @multi_thread
    def kaffeine_reply(self,HOSTLINK):
        if self.HOSTLINK:
            HOSTLINK = self.HOSTLINK
            print("Received HOSTLINK manually")
        print("Kaffeine: Started")
        while True:
            # sleep(2)
            print(HOSTLINK)
            if not HOSTLINK == None:
                sleep(8 * 60 - 15)
                print("[Kaffeine]: Trigger")
                self.kaffeine_reply_fnc()
            else:
                print("[Kaffeine]: Waiting for HOSTLINK")
            sleep(15)
    # This


def uview(maxthread,link,silent=False):
    global getlink
    # Mode 1: Show request
    # Mode 2: Show total



    # link = Write.Input("Link Video Tiktok -> ", Colors.red_to_purple, interval=0.0025)
    # Lấy ID video từ link
    headers_id = {
        'Connection': 'close',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                    ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Accept': 'text/html'
    }
    try:
        page = get(link, headers=headers_id, timeout=10).text
        match = search(r'"video":\{"id":"(\d+)"', page)
        if match:
            video_id = match.group(1)
            getlink = True
            # print(f'[+] Lấy ID Video thành công: {video_id}')
            # Write.Print(f"[Winter] Lấy video ID thành công\n", Colors.blue_to_green, interval=0.005)
            # Write.Print(f"[Winter] Ngày : {now().strftime('%d/%m/%Y')}\n", Colors.blue_to_green, interval=0.005)

        else:
            getlink = False
            # print('[-] Không tìm thấy ID Video')
            # Write.Print(f"[Winter] Lấy ID video thất bại\nLưu ý: Chỉ có thể buff cho những video đã đăng tải được > 3 phút", Colors.red_to_purple, interval=0.005)
            exit(1)
    except Exception as e:
        # Write.Print(f"[Winter] Xảy ra lỗi khi lấy ID Video : [EXC002]\n", Colors.blue_to_green, interval=0.005)
        # Write.Print(f"{e}\n", Colors.red_to_purple,interval=0)
        exit(1)


    # Hàm gửi view liên tục
    def selec_proxy():
        with open('proxy.txt', 'r', encoding='utf8') as f:
            proxy_lines = f.readlines()
            if proxy_lines:
                proxy_line = choice(proxy_lines).strip()
                proxy_parts = proxy_line.replace('us 30ng |', '').split(":")
                if len(proxy_parts) < 4:
                    prxy = None
                else:
                    prxy = {
                        "http": f"http://{proxy_parts[2].strip()}:{proxy_parts[3].strip()}@{proxy_parts[0].strip()}:{proxy_parts[1].strip()}",
                        "https": f"http://{proxy_parts[2].strip()}:{proxy_parts[3].strip()}@{proxy_parts[0].strip()}:{proxy_parts[1].strip()}",
                    }
            else:
                prxy = None
            return prxy
    def handle_response(resp: dict):
        # Lấy key đầu tiên
        first_key = next(iter(resp), None)
        # Chỉ xử lý khi key đầu là 'status_code' và giá trị của nó == 0
        if first_key == 'status_code' and resp.get('status_code') == 0:
            extra = resp.get('extra', {})
            log_pb = resp.get('log_pb', {})
            if 'now' in extra and 'impr_id' in log_pb:
                return True
        else:
            return False
    def send_view():
        if not silent:
            global failed,total,succedd
        url_view = 'https://api16-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region=VN'
        sig = Signature(params='', data='', cookies='').get_value()
        while True:
            random_hex = secrets.token_hex(16)
            headers_view = {
                'Host': 'api16-core-c-alisg.tiktokv.com',
                'Content-Length': '138',
                'Sdk-Version': '2',
                'Passport-Sdk-Version': '5.12.1',
                'X-Tt-Token': f'01{random_hex}0263ef2c096122cc1a97dec9cd12a6c75d81d3994668adfbb3ffca278855dd15c8056ad18161b26379bbf95d25d1f065abd5dd3a812f149ca11cf57e4b85ebac39d - 1.0.0',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'TikTok 37.0.4 rv:174014 (iPhone; iOS 14.2; ar_SA@calendar=gregorian) Cronet',
                'X-Ss-Stub': '727D102356930EE8C1F61B112F038D96',
                'X-Tt-Store-Idc': 'alisg',
                'X-Tt-Store-Region': 'sa',
                'X-Ss-Dp': '1233',
                'X-Tt-Trace-Id': '00-33c8a619105fd09f13b65546057d04d1-33c8a619105fd09f-01',
                'Accept-Encoding': 'gzip, deflate',
                'X-Khronos': sig['X-Khronos'],
                'X-Gorgon': sig['X-Gorgon'],
                'X-Common-Params-V2': (
                    "pass-region=1&pass-route=1"
                    "&language=ar"
                    "&version_code=17.4.0"
                    "&app_name=musical_ly"
                    "&vid=0F62BF08-8AD6-4A4D-A870-C098F5538A97"
                    "&app_version=17.4.0"
                    "&carrier_region=VN"
                    "&channel=App%20Store"
                    "&mcc_mnc=45201"
                    "&device_id=6904193135771207173"
                    "&tz_offset=25200"
                    "&account_region=VN"
                    "&sys_region=VN"
                    "&aid=1233"
                    "&residence=VN"
                    "&screen_width=1125"
                    "&uoo=1"
                    "&openudid=c0c519b4e8148dec69410df9354e6035aa155095"
                    "&os_api=18"
                    "&os_version=14.2"
                    "&app_language=ar"
                    "&tz_name=Asia%2FHo_Chi_Minh"
                    "&current_region=VN"
                    "&device_platform=iphone"
                    "&build_number=174014"
                    "&device_type=iPhone14,6"
                    "&iid=6958149070179878658"
                    "&idfa=00000000-0000-0000-0000-000000000000"
                    "&locale=ar"
                    "&cdid=D1D404AE-ABDF-4973-983C-CC723EA69906"
                    "&content_language="
                ),
            }
            cookie_view = {'sessionid': random_hex}
            start = datetime(2020, 1, 1, 0, 0, 0)
            end = datetime(2024, 12, 31, 23, 59, 59)
            delta_seconds = int((end - start).total_seconds())
            random_offset = randint(0, delta_seconds)
            random_dt = start + timedelta(seconds=random_offset)
            data = {
                'action_time': int(time()),
                'aweme_type': 0,
                'first_install_time': int(random_dt.timestamp()),
                'item_id': video_id,
                'play_delta': 1,
                'tab_type': 4
            }
            try:
                if not silent:
                    total += 1
                r = post(url_view, data=data, headers=headers_view, cookies=cookie_view, timeout=10)
                # print(r.json())
                sig = Signature(params='ac=WIFI&op_region=VN', data=str(data), cookies=str(cookie_view)).get_value()
                if not silent:
                    if handle_response(r.json()):
                        succedd += 1
                        m = True
                    else:
                        failed += 1
                        m = False
                    if m:
                        listd.append(datetime.now().strftime('%H:%M:%S'))
            except Exception:
                if not silent:
                    failed += 1
                continue

    threads = []
    for i in range(maxthread):
        t = Thread(target=send_view)
        t.daemon = True
        t.start()
        threads.append(t)
from sanic import Sanic, response
app = Sanic(__name__)
GLOBAL = {"silent":False,"link":None}
@app.route("/")
async def index(request):
    global getlink
    if not getlink:
        return response.text("Not running")
    else:
        if GLOBAL["link"] and GLOBAL["silent"]:
            # https://www.tiktok.com/@wdhoang11/video/7549724084234472712
            idv = GLOBAL['link'].split("video/")
            return response.text(f"Check on https://tokcount.com/live-video-view-counter?id={idv[1]}")
        else:
            cx = '\n'.join(listd)
            return response.text(f"Total : {total} ; Succedd : {succedd} ; Failed : {failed}\n--------\n{cx}")
@app.route("/clear")
async def clear(request):
    global listd
    listd = []
    return response.text("Cleared")
@app.route("/monitor")
async def monitor(request):
    vmd = virtual_memory()
    cpu = cpu_percent()
    ram = vmd.percent
    return response.text(f"CPU : {cpu}%\nRAM : {ram}% , meaning {human_readable_size(vmd.total * ram / 100)} / {human_readable_size(vmd.total)} RAM")

@app.route("/run")  
async def run(request):
    global getlink
    url = request.args.get("url")
    max_thread = int(request.args.get("max_thread"))
    silent = (request.args.get("silent"))
    if silent in ["True","true","1"]:
        silent = True
    else:
        silent = False
    if not url : return "No url"
    if getlink == False:
        GLOBAL["silent"] = silent
        tms = Thread(target=uview,args=(max_thread,url,silent))
        tms.start()
        GLOBAL["link"] = url
        return response.text("Starting on "+url)
    else:
        return response.text("Already running on "+GLOBAL["link"]+f" ,mode : {GLOBAL['silent']}")

Kaffeine(app)
if exists("autorun.txt"):
    with open("autorun.txt","r") as f:
        d = f.read().splitlines()
        url = d[0]
        max_thread = int(d[1])
        silent = True if d[2] in ["True","true","1"] else False
        tms = Thread(target=uview,args=(max_thread,url,silent))
        tms.start()
        GLOBAL["link"] = url
        GLOBAL["silent"] = silent
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
