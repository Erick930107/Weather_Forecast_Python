# Python嘉義市氣溫爬蟲
這個程式會從 中央氣象署開放資料平台 (CWB OpenData) 抓取未來一週嘉義市的氣溫資料，計算每日早晚的溫差，並利用 Matplotlib 繪製折線圖，讓使用者可以快速了解未來 7 天的氣溫變化
## 功能特色
* 從 CWB API 取得台灣地區未來一週的溫度資料。
* 計算每日早晚溫差，若溫差超過 4°C，會提示「早晚溫差大」。
* 使用 Matplotlib 畫出未來 7 天 早/晚氣溫折線圖。
* X 軸顯示日期與早晚時間點，Y 軸顯示攝氏氣溫。

## 使用技術
* 語言：Python 3

* 套件：
  * requests（取得 API 資料）
  * matplotlib（資料視覺化）
  * time（時間處理）

## 執行方式
1. 安裝需要的套件：
    ~~~bash
    pip install requests matplotlib
    ~~~

2. 執行程式：
    ~~~
    python weather_forecast.py
    ~~~

3. 程式會輸出：
    * 現在時間
    * 每日早晚溫差 (若 ≥4°C 會提示「早晚溫差大」)
    * 未來 7 天早晚氣溫折線圖
