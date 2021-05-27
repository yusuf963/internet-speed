from speedtest import Speedtest

st = Speedtest()
print('your connection download speed is', st.download()/1000000)
print('your connection upload speed is', st.upload()/1000000)
