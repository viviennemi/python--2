import requests

def download_weather():
    url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=rdec-key-123-45678-011121314&format=JSON'
    response = requests.get(url)
    if response.status_code == 200:
        print("下載成功")
        weather = response.json()
        return weather
    else:
        print("下載失敗")
        return False
def main():
    #下載json檔
    weather = download_weather()
    if weather != False:
        print("下載完畢")
    else:
        print("應用程式下載失敗")
        return
if __name__ =="__main__":
    main()