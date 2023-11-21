with open("cal", "rb") as f:
     data = f.read()
     with open("cal_out", "wb") as e:
         e.write(data[len(data)//2:])
         e.write(data[:len(data)//2])
         e.close()
