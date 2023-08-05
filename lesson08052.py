import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

t = np.arange(0.,1.0,0.05)
#display(t)
##print(t)
st.write(t)
#t1 = 2 * np.pi * t
#display(t1)
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
#display(y1)
#display(y2)
##print(y1)
##print(y2)
st.write(y1)
st.write(y2)
figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
st.write(figure1)
##plt.show()
#要安裝pip install streamlit才能秀在網頁上
#streamlit run 程式名稱才會跑程式
#ctrl+C就是執行中斷顯示