import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#沒有value的時候無法互動但是會顯示
value = st.slider("三角函式",min_value=0,max_valuse=10)
t = np.arange(0.,value,0.05)
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
st.write(figure1)

#要安裝pip install streamlit才能秀在網頁上
#streamlit run 程式名稱才會跑程式
#ctrl+C就是執行中斷顯示