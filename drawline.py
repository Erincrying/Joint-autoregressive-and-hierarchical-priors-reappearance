import matplotlib.pyplot as plt

bpp_result = [
      0.071997, 
      0.153354,
      0.264381,
      0.428511,
      0.635404,
      0.904279,
      1.258828,
      1.982050,
      2.992778
    ]
psnr_result = [
      26.804116,
      28.880747,
      30.927089,
      33.028649,
      34.998064,
      37.053312,
      39.120817,
      42.165220,
      45.074915
    ]


bpp_myself = [0.11311848958333331, 0.1898600260416667]
psnr_myself = [ 27.9804873104851, 29.69223977516354]

# 第一个码率点
bpp_myself_FIR_01 = [0.11311848958333331]
psnr_myself_FIR_01 = [ 27.9804873104851]

bpp_myself_FIR_02 = [0.11440022786458331]
psnr_myself_FIR_02 = [	27.919279305731433]


# 第二个码率点
bpp_myself_SEC_01 = [0.1898600260416667]
psnr_myself_SEC_01 = [29.69223977516354]

# 添加横纵坐标与标题
plt.xlabel('bit rate [bit/px]')
plt.ylabel('PSNR[db]')
plt.title('rate–distortion')

# 原文psnr
plt.scatter(bpp_result, psnr_result)
plt.plot(bpp_result, psnr_result, label='original')

# 自己的psnr
plt.scatter(bpp_myself, psnr_myself)
plt.plot(bpp_myself, psnr_myself, label='myself')
# plt.plot(bpp_myself, psnr_myself, color='g', linestyle='-.', label = 'myself')


# 第一个码率点
# plt.scatter(bpp_myself_FIR_01, psnr_myself_FIR_01)
# plt.plot(bpp_myself_FIR_01, psnr_myself_FIR_01, label='joint_FIR_01')

# plt.scatter(bpp_myself_FIR_02, psnr_myself_FIR_02)
# plt.plot(bpp_myself_FIR_02, psnr_myself_FIR_02, label='joint_FIR_02')

# 第二个码率点
plt.scatter(bpp_myself_SEC_01, psnr_myself_SEC_01)
plt.plot(bpp_myself_SEC_01, psnr_myself_SEC_01, label='joint_SEC_01')
#添加网格信息
plt.grid(True, linestyle='--', alpha=0.5) #默认是True，风格设置为虚线，alpha为透明度
plt.legend() # 为了能显示label
plt.show()
