1. data部份我除了收集20170101~20190228外，我自己還有去以下這個網站將2019年3月份的資料手動補齊。
https://www.taipower.com.tw/d006/loadGraph/loadGraph/load_reserve_.html
2. data的部份我只用到 peak_load，train_data則是從20170101到20180630。
3. 因為 peak_load在夏天時會叫冬天高出許多，因此我採用的 model是holtwinters這種model，因為這種model適合用在季節對於 data有較大影響時。
4. 因為清明節連假四天的關係，model預測起來就比正常週休二日的時候還差上許多。
