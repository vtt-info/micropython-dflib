from machine import ADC, Pin


class PT100:
  
  pt100_list = [100, 100.39, 100.78, 101.17, 101.56, 101.95, 102.34, 102.73, 103.12, 103.51
    , 103.9, 104.29, 104.68, 105.07, 105.46, 105.85, 106.24, 106.63, 107.02, 107.4
    , 107.79, 108.18, 108.57, 108.96, 109.35, 109.73, 110.12, 110.51, 110.9, 111.29
    , 111.67, 112.06, 112.45, 112.83, 113.22, 113.61, 114, 114.38, 114.77, 115.15
    , 115.54, 115.93, 116.31, 116.7, 117.08, 117.47, 117.86, 118.24, 118.63, 119.01
    , 119.4, 119.78, 120.17, 120.55, 120.94, 121.32, 121.71, 122.09, 122.47, 122.86
    , 123.24, 123.63, 124.01, 124.39, 124.78, 125.16, 125.54, 125.93, 126.31, 126.69
    , 127.08, 127.46, 127.84, 128.22, 128.61, 128.99, 129.37, 129.75, 130.13, 130.52
    , 130.9, 131.28, 131.66, 132.04, 132.42, 132.8, 133.18, 133.57, 133.95, 134.33
    , 134.71, 135.09, 135.47, 135.85, 136.23, 136.61, 136.99, 137.37, 137.75, 138.13
    , 138.51, 138.88, 139.26, 139.64, 140.02, 140.4, 140.78, 141.16, 141.54, 141.91
    , 142.29, 142.67, 143.05, 143.43, 143.8, 144.18, 144.56, 144.94, 145.31, 145.69
    , 146.07, 146.44, 146.82, 147.2, 147.57, 147.95, 148.33, 148.7, 149.08, 149.46
    , 149.83, 150.21, 150.58, 150.96, 151.33, 151.71, 152.08, 152.46, 152.83, 153.21
    , 153.58, 153.96, 154.33, 154.71, 155.08, 155.46, 155.83, 156.2, 156.58, 156.95
    , 157.33, 157.7, 158.07, 158.45, 158.82, 159.19, 159.56, 159.94, 160.31, 160.68
    , 161.05, 161.43, 161.8, 162.17, 162.54, 162.91, 163.29, 163.66, 164.03, 164.4
    , 164.77, 165.14, 165.51, 165.89, 166.26, 166.63, 167, 167.37, 167.74, 168.11
    , 168.48, 168.85, 169.22, 169.59, 169.96, 170.33, 170.7, 171.07, 171.43, 171.8
    , 172.17, 172.54, 172.91, 173.28, 173.65, 174.02, 174.38, 174.75, 175.12, 175.49
    , 175.86, 176.22, 176.59, 176.96, 177.33, 177.69, 178.06, 178.43, 178.79, 179.16
    , 179.53, 179.89, 180.26, 180.63, 180.99, 181.36, 181.72, 182.09, 182.46, 182.82
    , 183.19, 183.55, 183.92, 184.28, 184.65, 185.01, 185.38, 185.74, 186.11, 186.47
    , 186.84, 187.2, 187.56, 187.93, 188.29, 188.66, 189.02, 189.38, 189.75, 190.11
    , 190.47, 190.84, 191.2, 191.56, 191.92, 192.29, 192.65, 193.01, 193.37, 193.74
    , 194.1, 194.46, 194.82, 195.18, 195.55, 195.91, 196.27, 196.63, 196.99, 197.35
    , 197.71, 198.07, 198.43, 198.79, 199.15, 199.51, 199.87, 200.23, 200.59, 200.95
    , 201.31, 201.67, 202.03, 202.39, 202.75, 203.11, 203.47, 203.83, 204.19, 204.55
    , 204.9, 205.26, 205.62, 205.98, 206.34, 206.7, 207.05, 207.41, 207.77, 208.13
    , 208.48, 208.84, 209.2, 209.56, 209.91, 210.27, 210.63, 210.98, 211.34, 211.7
    , 212.05, 212.41, 212.76, 213.12, 213.48, 213.83, 214.19, 214.54, 214.9, 215.25
    , 215.61, 215.96, 216.32, 216.67, 217.03, 217.38, 217.74, 218.09, 218.44, 218.8
    , 219.15, 219.51, 219.86, 220.21, 220.57, 220.92, 221.27, 221.63, 221.98, 222.33
    , 222.68, 223.04, 223.39, 223.74, 224.09, 224.45, 224.8, 225.15, 225.5, 225.85
    , 226.21, 226.56, 226.91, 227.26, 227.61, 227.96, 228.31, 228.66, 229.02, 229.37
    , 229.72, 230.07, 230.42, 230.77, 231.12, 231.47, 231.82, 232.17, 232.52, 232.87
    , 233.21, 233.56, 233.91, 234.26, 234.61, 234.96, 235.31, 235.66, 236, 236.35
    , 236.7, 237.05, 237.4, 237.74, 238.09, 238.44, 238.79, 239.13, 239.48, 239.83
    , 240.18, 240.52, 240.87, 241.22, 241.56, 241.91, 242.26, 242.6, 242.95, 243.29
    , 243.64, 243.99, 244.33, 244.68, 245.02, 245.37, 245.71, 246.06, 246.4, 246.75]
  
  def __init__(self, pin):
    self.pin = ADC(Pin(pin))
    self.voltageRef = 3.3

  def comp(self, pt, i):
    if (pt - self.pt100_list[i]) > (self.pt100_list[i + 1] - self.pt100_list[i] / 2):
      return i + 1
    else:
      return i

  def read(self):
    voltage = self.pin.read()
    voltage = voltage * self.voltageRef / 4096
    res = (1800 * voltage + 220.9 * 18) / (2.209 * 18 - voltage)
    front = 0
    end = 398
    mid = (front + end) // 2
    while ((front < end) and (res < self.pt100_list[mid] or  res > self.pt100_list[mid+1])):
      if self.pt100_list[mid] < res:
        if self.pt100_list[mid + 1] < res:
          front = mid + 1
        else:
          mid = self.comp(res, mid)
          return mid
      if self.pt100_list[mid] > res:
        if self.pt100_list[mid - 1] > res:
          end = mid - 1
        else:
          mid = self.comp(res, mid - 1)
          return mid
      mid = front + (end - front) // 2
    return mid

