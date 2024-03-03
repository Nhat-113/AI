from kivymd.uix import dialog
from kivymd.uix import button
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.toolbar import MDTopAppBar as MDToolbar
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.factory import Factory

from kivy.uix.scrollview import ScrollView
import os
import pyautogui
import playsound
from kivy.core.window import Window
from win10toast import ToastNotifier
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from time import strftime
from gtts import gTTS
#from youtube_search import YoutubeSearch
from bs4 import BeautifulSoup

path = "C:/Users/ASUS/Documents/AI"

a = ['chào', 'hello', 'hey', 'bạn ơi']
b = ['không khỏe', 'tôi ốm', 'không được khỏe']
c = ['đẹp trai', 'thấy tôi thế nào', 'đẹp gái', 'xinh đẹp']
d = ['bạn là ai', 'tên gì', 'tôi không biết bạn', 'chưa biết bạn', ]
e = ['tôi là ai', 'tôi tên gì', 'tôi tên là gì']
f = ['khỏe không', 'bạn ổn', 'ổn không']
g = ['cảm ơn', 'thanks', 'thank you']
h = ['thôi', 'dừng', 'tạm biệt', 'bye', 'good bye']
name = ''
language = 'vi'
toast = ToastNotifier()
alone = 'Câu này hỏi khó quá đi, Người yêu đâu phải muốn thì có luôn. Kể ra lại thấy thêm buồn, Bận làm trợ lý alone dài dài haha'
like = 'Tôi thích tìm kiếm thông tin và giúp đỡ mọi người. Thê có tính là yêu không'


def current_weather(text):
    # reg_ex = re.search('ở (.+)', text)
    domain = text
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = domain
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day=now.day, month=now.month, year=now.year, hourrise=sunrise.hour, minrise=sunrise.minute,
                                                                           hourset=sunset.hour, minset=sunset.minute,
                                                                           temp=current_temperature, pressure=current_pressure, humidity=current_humidity)
        speak(content)
        return(content)
        time.sleep(20)
    else:
        speak("Không tìm thấy địa chỉ của bạn")


def get_text():
    for i in range(3):
        print('Nói đi')
        text = get_voice()
        if(text):
            return text.lower()
        elif i < 2:
            speak("Tôi không nghe rõ, bạn có thể nói lại không")
    time.sleep(10)
    stop()
    return 0


def talk(name):
    day_time = int(strftime("%H"))
    if day_time < 12:
        hi = "Chào buổi sáng {}. Chúc bạn ngày mới tốt lành!".format(name)
        speak(hi)
    elif day_time < 18:
        hi = "Chào buổi chiều {}".format(name)
        speak(hi)
    else:
        hi = "Chào buổi tối {}".format(name)
        speak(hi)
    time.sleep(5)
    speak("Bạn có khỏe không ?")
    time.sleep(3)
    answer = get_voice()
    if answer:
        if "có" in answer:
            speak("Thật là tốt")
        else:
            speak("Buồn quá, vậy bạn nên nghỉ ngơi cho khỏe đi!")


def get_name():
    speak("Tên bạn là {}".format(name))
    return "Tên bạn là {}".format(name)


def open_application(text):
    if "microsoft edge" in text:
        speak("Mở Microsoft Edge")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.exe')
        time.sleep(3)
        speak("Đã Mở Microsoft Edge")
        time.sleep(3)
        return 'Đã Mở Microsoft Edge'

    elif "google" in text:
        speak("Mở Google Chrome")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome.exe')
        time.sleep(3)
        speak("Đã mở Google Chrome")
        time.sleep(3)
        return 'Đã mở Google Chrome'
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013')
        time.sleep(3)
        speak("Đã mở Microsoft Word")
        time.sleep(3)
        return("Đã mở Microsoft Word")
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile(
            'C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE')
        time.sleep(3)
        speak("Đã mở Microsoft Excel")
        time.sleep(3)
        return 'Đã mở Microsoft Excel'
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
        time.sleep(3)
        return 'Ứng dụng chưa được cài đặt. Bạn hãy thử lại!'


def help():
    time.sleep(3)
    speak("Bạn cần Tôi giúp gì không?")
    time.sleep(3)
    return'Bạn cần Tôi giúp gì không?'


def call_bot(text):
    id = 0
    text = text.lower()
    print(text)
    for s in a:
        if s in text:
            id = 1
            break
    for s in b:
        if s in text:
            id = 2
            break
    for s in c:
        if s in text:
            id = 3
            break
    for s in d:
        if s in text:
            id = 4
            break
    for s in e:
        if s in text:
            id = 5
            break
    for s in f:
        if s in text:
            id = 6
            break
    for s in g:
        if s in text:
            id = 7
            break
    for s in h:
        if s in text:
            id = 8
            break

    print(id)
    if id == 1:
        s = 'Chào bạn '+name + ' tôi có thể giúp gì cho bạn'
        speak(s)
        return s
    elif id == 2:
        s = 'Bạn nghỉ ngơi đi nhé !'
        speak(s)
        return s
    elif id == 3:
        s = 'Bạn luôn là nhất hê hê !'
        speak(s)
        return s
    elif id == 4:
        s = 'Tên tôi là trợ lý VKU'
        speak(s)
        time.sleep(3)
        return s
    elif id == 5:
        s = 'Bạn là ' + name + ' dễ mến'
        speak(s)
        time.sleep(3)
        return s
    elif id == 6:
        s = 'Tôi lúc nào cũng khỏe'
        speak(s)
        time.sleep(3)
        return s
    elif id == 7:
        s = 'Ngại quá, Tôi rất vui khi giúp được bạn'
        speak(s)
        time.sleep(3)
        return s
    elif id == 8:
        s = stop()
        speak(s)
        time.sleep(3)
        return s
    elif "trò chuyện" in text or "nói chuyện" in text:
        return talk(name)
    elif "âm lượng" in text:
        return change_volume(text)
    elif "thời tiết ở" in text:
        return current_weather(text)
    elif "ứng dụng" in text:
        return open_application(text)
    elif "tên tôi" in text or "tôi tên" in text:
        return get_name()
    elif "bạn có người yêu chưa" in text or "người yêu của bạn" in text:
        speak(alone)
        time.sleep(5)
        return alone
    elif "bạn có khỏe không" in text or "khỏe không" in text:
        speak("Tôi luôn luôn khỏe trừ khi mất điện")
        time.sleep(4)
        return 'Tôi luôn luôn khỏe trừ khi mất điện'
    elif "trang web" in text:
        return open_website(text)
        time.sleep(4)
    elif "giá vàng" in text:
        s = gold_price()
        speak(s)
        # toast.show_toast("Giá vàng",s)
        return s
    elif "tìm kiếm" in text:
        return open_website_search(text)
        time.sleep(4)
    elif "hiện tại" in text:
        s = get_time(text)
        # toast.show_toast("Giờ",s)
        return s
    elif "định nghĩa" in text:
        return speak("Bot: haha")
    elif "chơi nhạc" in text:
        return play_song(text)
        time.sleep(4)
    else:
        return query(text)


def search(text):
    url = "https://www.google.com.tr/search?q={}".format(text)
    webbrowser.open(url)
    s = "Không có thông tin, và sau đây là 1 vài kết quả"
    speak(s)
    return s


def open_website_search(text):
    reg_ex = re.search('kiếm (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www.google.com.tr/search?q={}".format(domain)
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False


def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
        return('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
        return("Hôm nay là ngày %d tháng %d năm %d" %
               (now.day, now.month, now.year))
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")


def open_website(text):
    reg_ex = re.search('web (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        return 'Trang web bạn yêu cầu đã được mở.'
    else:
        return False


def stop():
    speak("Hẹn gặp lại bạn nhé")
    return 'Hẹn gặp lại bạn nhé'


def language_voice(text):
    # reg_ex = re.search('tiếng (.+)', text)
    reg_ex = text
    if reg_ex:
        if reg_ex:
            domain = reg_ex
            if 'việt' in domain:
                return 'vi'
            if 'nhật' in domain:
                return 'ja'
            if 'anh' in domain:
                return 'en'
            if 'trung' in domain:
                return 'zh'
            if 'pháp' in domain:
                return 'fr'
            if 'hàn' in domain:
                return 'ko'
            else:
                return 'vi'
    else:
        return 'vi'


def gold_price():
    url = 'https://www.pnj.com.vn/blog/gia-vang/'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    sult = soup.find(id="content-price").find_all("td")
    CLEANR = re.compile('<.*?>')
    a2 = []
    for a in sult:
        c = re.sub(CLEANR, '', str(a))
        c = c.replace(',', '.')
        a2.append(c)
    a1 = 'Giá bán vàng ' + a2[0]+': ' + a2[1] + ' đồng' + '\n'+'Giá mua vàng ' + a2[0]+': ' + a2[2] + \
        ' đồng'+'\n'+'Giá bán vàng ' + \
        a2[3]+': ' + a2[4] + ' đồng'+'\n'+'Giá mua vàng ' + \
        a2[3]+': ' + a2[5] + ' đồng'
    return a1


def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return 0


def Toast(name, text):
    toast.show_toast(name, text)


def play_song(text):
    # reg_ex = re.search('bài (.+)', text)
    speak('Xin mời bạn chọn tên bài hát')
    time.sleep(2)
    domain = get_text()
    mysong = domain
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")
    return 'Bài hát bạn yêu cầu đã được mở'


def speak2(lang, text):
    language_v = language_voice(lang)
    print("Bot: {}".format(text))
    # truyen vao text de doc language
    tts = gTTS(text=text, lang=language_v, slow=False)
    # luu am thanh vao he thong
    tts.save(path+'sound.mp3')
    # play song truyen tu text
    playsound.playsound(path+'sound.mp3', False)
    # xoa song
    os.remove(path+'sound.mp3')


def query(text):
    user_query = text
    URL = "https://www.google.co.in/search?q=" + user_query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    bebe = str(soup)
    if 'class="Y2IQFc"' in bebe:
        sult = soup.find(id='tw-target-text').get_text()
        speak2(user_query, sult)
        return sult
    elif 'class="vk_bk dDoNo FzvWSb"' in bebe:
        sult = soup.find(class_='vk_bk dDoNo FzvWSb').get_text()
        speak(sult)
        time.sleep(6)
        return sult
    elif 'class="Z0LcW"' in bebe:
        sult = soup.find(class_='Z0LcW').get_text()
        speak(sult)
        return sult
    elif 'class="pclqee"' in bebe:
        sult = soup.find(class_='pclqee').get_text()
        speak(sult+'VNĐ')
        return sult+' VNĐ'
    elif 'class="LGOjhe"' in bebe:
        sult = soup.find(class_='LGOjhe').find(class_='hgKElc').get_text()
        speak(sult)
        return sult
    elif 'class="FzvWSb"' in bebe:
        sult = soup.find(class_='FzvWSb').get_text()
        speak(sult)
        return sult
    elif 'class="z7BZJb XSNERd"' in bebe:
        sult = soup.find(class_='qv3Wpe').get_text()
        speak(text + ' là ' + sult)
        return sult
    elif 'class="kno-rdesc"' in bebe:
        sult = soup.find(class_='kno-rdesc').find('span')
        CLEANR = re.compile('<.*?>')
        sult = re.sub(CLEANR, '', str(sult))
        speak(sult)
        return sult
    elif 'class="ayRjaf"' in bebe:
        sult = soup.find(class_='zCubwf').get_text()
        speak(sult)
        return sult
    elif 'class="dDoNo vrBOv vk_bk"' in bebe:
        sult = soup.find(class_='dDoNo vrBOv vk_bk').get_text()
        speak(sult)
        return sult
    elif 'class="hgKElc"' in bebe:
        sult = soup.find(class_='hgKElc').get_text()
        speak(sult)
        return sult
    elif 'class="UQt4rd"' in bebe:
        nhietdo = 'Nhiệt độ: ' + \
            soup.find(class_='q8U8x').get_text() + '°C.'+'\n'
        doam = 'Độ ẩm: ' + soup.find(id='wob_hm').get_text()
        mua = 'Khả năng có mưa: ' + soup.find(id='wob_pp').get_text()+'\n'
        gdp = soup.find(class_='wob_tci')
        wheather = gdp['alt']+'\n'
        nam = wheather + nhietdo + mua + doam
        # toast.show_toast("Thời tiết",nam)
        speak(nam)
        return nam
    elif 'class="gsrt vk_bk FzvWSb YwPhnf"' in bebe:
        sult = soup.find(class_='gsrt vk_bk FzvWSb YwPhnf').get_text()
        speak(sult)
        return sult
    elif 'class="qyEGdc"' in bebe:
        gdp = soup.find_all("table", attrs={"class": "qyEGdc"})
        table1 = gdp[1]
        span = str(table1.find_all('span'))
        span = span.replace(']', '')
        s = span.split(',')
        print()
        all = re.sub(r"[A-Za-z<>/=]", '', s[2])
        die = re.sub(r"[A-Za-z<>/=]", '', s[8])
        all_1 = re.sub(r"[A-Za-z<>/=]", '', s[6])
        die_1 = re.sub(r"[A-Za-z<>/=]", '', s[12])
        all = 'Tổng số người mắc: ' + all + ' : '
        speak(all)
        time.sleep(3)
        if '+' in all_1:
            all_1 = re.sub(r"[+-]", '', all_1)
            all_1 = 'Tăng '+all_1+' ca : '
            speak(all_1)
            time.sleep(3)
        elif '-' in all_1:
            all_1 = re.sub(r"[+-]", '', all_1)
            all_1 = 'Giảm '+all_1+' ca : '
            time.sleep(3)
        die = 'Số người tử vong: ' + die + ' : '
        speak(die)
        time.sleep(4)
        if '+' in die_1:
            die_1 = re.sub(r"[+-]", '', die_1)
            die_1 = 'Tăng '+die_1+' ca '
            speak(die_1)
            time.sleep(3)
        elif 'class-' in die_1:
            die_1 = re.sub(r"[+-]", '', die_1)
            die_1 = 'Giảm '+die_1+' ca '
            speak(die_1)
            time.sleep(3)
        covid = all + '\n' + all_1 + '\n' + die + '\n' + die_1
        # Toast('Covid', covid)
        return covid
    else:
        if len(text) > 0:
            return search(text)


def change_volume(text):
    if 'giảm' in text:
        pyautogui.press('volumedown', presses=3)
    if 'tăng' in text:
        pyautogui.press('volumeup', presses=3)
    if 'tắt' in text:
        pyautogui.press('volumemute', presses=3)
    speak('đã chỉnh')
    return 'Đã chỉnh thành công'


def speak(text):

    print("Bot: {}".format(text))
    # truyen vao text de doc language
    tts = gTTS(text=text, lang=language, slow=False)
    # luu am thanh vao he thong
    tts.save(path+'sound.mp3')
    # play song truyen tu text
    playsound.playsound(path+'sound.mp3',)
    # xoa song
    os.remove(path+'sound.mp3')


class ConverterApp(MDApp):
    def show_data(self, txt):
        dialog = MDDialog(text=txt)
        dialog.open()

    def text(self, text, ):
        self.item = TwoLineListItem(
            text="Bạn",
            secondary_text=self.input.text,
            height=25)
        self.list_view.add_widget(self.item)
        self.scroll.scroll_to(self.item)
        text = self.input.text
        text = text.lower()
        s = call_bot(text)
        if s:
            self.item = TwoLineListItem(
                text='Bot',
                secondary_text=s,)
            self.list_view.add_widget(self.item)
            self.scroll.scroll_to(self.item)
            self.close_button = MDRaisedButton(
                text='Đóng', on_release=self.close_dialog)
            self.dialog = MDDialog(
                title='Kết quả', text=s, buttons=[self.close_button])
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def voice(self, text, ):
        speak('Bạn cần tôi giúp gì nào')
        text = get_text()
        text = text.lower()
        if text:
            self.item = TwoLineListItem(
                text="Bạn",
                secondary_text=text,
                height=25)
            self.list_view.add_widget(self.item)
            self.scroll.scroll_to(self.item)
            s = call_bot(text)
            if s:
                self.item = TwoLineListItem(
                    text='Bot',
                    secondary_text=s,)
                self.list_view.add_widget(self.item)
                self.scroll.scroll_to(self.item)
        else:
            speak('không có dữ liệu')

    def build(self):
        Window.pos_hint = {'center_x': 0, 'center_y': 0}
        self.state = 0  # initial state
        screen = MDScreen()

        # top toolbar
        self.toolbar = MDToolbar(title="Trợ lý ảo")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["play"]]
        # banner

        # list view
        self.scroll = ScrollView(
            pos_hint={"top": 0.9},
            size_hint=(1, 0.65)
        )
        self.list_view = MDList()
        self.scroll.add_widget(self.list_view)
        self.item2 = OneLineListItem(text='Bot: Chào bạn ' + name)
        self.list_view.add_widget(self.item2)
        self.item2 = OneLineListItem(text='Tôi là trợ lý VKU')
        self.list_view.add_widget(self.item2)
        self.item2 = OneLineListItem(
            text='Tôi có thể giúp bạn rất nhiều việc đó')
        self.list_view.add_widget(self.item2)
        self.item2 = OneLineListItem(text='Tôi có thể giúp bạn dịch')
        self.list_view.add_widget(self.item2)
        self.item2 = OneLineListItem(text='Tôi có thể giúp bạn chơi nhạc')
        self.list_view.add_widget(self.item2)
        self.item2 = OneLineListItem(text='Tôi có thể giúp bạn xem thời tiết')
        self.list_view.add_widget(self.item2)
        self.item2 = OneLineListItem(text='Và rất nhiều việc nữa hì hì')
        self.list_view.add_widget(self.item2)
        self.input = MDTextField(
            size_hint=(0.6, 0.4),
            hint_text="Bạn muốn nói gì với tôi",
            mode="rectangle",
            pos_hint={"center_x": 0.35, "center_y": 0.07},
            font_size=15
        )

        # secondary + primary labels
        # "CONVERT" button
        self.voicemic = MDRaisedButton(
            text="Nói",
            font_size=17,
            size_hint=(0.14, None),
            pos_hint={"center_x": 0.9, "center_y": 0.06},
            on_press=self.voice
        )
        self.send = MDRaisedButton(
            text="Gửi",
            font_size=17,
            size_hint=(0.14, None),
            pos_hint={"center_x": 0.75, "center_y": 0.06},
            on_press=self.text
        )
        screen.add_widget(self.scroll)
        screen.add_widget(self.voicemic)
        screen.add_widget(self.send)
        screen.add_widget(self.input)
        screen.add_widget(self.toolbar)

        return screen


if __name__ == '__main__':
    speak('Chào bạn ' + name)
    ConverterApp().run()
