from speedtest import Speedtest

st = Speedtest()
print('your connection download speed is', st.download())
print('your connection upload speed is', st.upload())
