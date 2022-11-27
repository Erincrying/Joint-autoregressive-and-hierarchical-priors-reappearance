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


# 重新训练前的选点
# bpp_myself = [0.11311848958333331, 0.1898600260416667, 0.34497409396701384, 0.5446946885850694, 0.796875, 0.9485236273871527]
# psnr_myself = [ 27.9804873104851, 29.69223977516354, 31.70264841162641, 33.75013402805966, 35.55966067123389, 36.489859806079174]

# 重新训练第5、6个码率点
bpp_myself = [0.11311848958333331, 0.1898600260416667, 0.34497409396701384, 0.5446946885850694, 0.7282545301649305]
psnr_myself = [ 27.9804873104851, 29.69223977516354, 31.70264841162641, 33.75013402805966, 35.418804324085045]


# 第一个码率点
bpp_myself_FIR_01 = [0.11311848958333331]
psnr_myself_FIR_01 = [ 27.9804873104851]

bpp_myself_FIR_02 = [0.11440022786458331]
psnr_myself_FIR_02 = [	27.919279305731433]


# 第二个码率点
bpp_myself_SEC_01 = [0.1898600260416667]
psnr_myself_SEC_01 = [29.69223977516354]

# 第三个码率点
bpp_myself_THI_01 = [0.35229153103298616]
psnr_myself_THI_01 = [31.694376047084095]

bpp_myself_THI_02 = [0.34497409396701384]
psnr_myself_THI_02 = [31.70264841162641]

# 第四个码率点
bpp_myself_FOUR_01 = [0.550320095486111]
psnr_myself_FOUR_01 = [33.72843470073433]

bpp_myself_FOUR_02 = [0.5457661946614584]
psnr_myself_FOUR_02 = [33.686422857353115]

bpp_myself_FOUR_03 = [0.5446946885850694]
psnr_myself_FOUR_03 = [33.75013402805966]

# 第五个码率点
bpp_myself_FIVE_01 = [0.7960645887586807]
psnr_myself_FIVE_01 = [35.549931949747794]

bpp_myself_FIVE_02 = [0.822838677300347]
psnr_myself_FIVE_02 = [35.525695706455444]

bpp_myself_FIVE_03 = [0.8254496256510416]
psnr_myself_FIVE_03 = [35.46308217787015]

bpp_myself_FIVE_04 = [0.796875]
psnr_myself_FIVE_04 = [35.55966067123389]

bpp_myself_FIVE_05 = [0.8084072536892362]
psnr_myself_FIVE_05 = [35.47669278465481]

bpp_myself_FIVE_06 = [0.9298875596788195]
psnr_myself_FIVE_06 = [35.61632170735353]

bpp_myself_FIVE_07 = [0.905429416232639]
psnr_myself_FIVE_07 = [35.67110124865172]


bpp_myself_FIVE_08 = [0.8459574381510415]
psnr_myself_FIVE_08 = [35.58530749459595]

bpp_myself_FIVE_09 = [0.9462517632378472]
psnr_myself_FIVE_09 = [35.63010021106881]

bpp_myself_FIVE_10 = [0.829074435763889]
psnr_myself_FIVE_10 = [35.487170549271916]

bpp_myself_FIVE_11 = [0.7282545301649305]
psnr_myself_FIVE_11 = [35.418804324085045]
# 第六个码率点
bpp_myself_SIX_01 = [0.9789598253038193]
psnr_myself_SIX_01 = [36.47576705830845]

bpp_myself_SIX_02 = [0.9485236273871527]
psnr_myself_SIX_02 = [36.489859806079174]

bpp_myself_SIX_03 = [0.9661492241753473]
psnr_myself_SIX_03 = [36.47805391147329]

bpp_myself_SIX_04 = [0.9533962673611112]
psnr_myself_SIX_04 = [36.481174174512624]

bpp_myself_SIX_05 = [0.9954698350694443]
psnr_myself_SIX_05 = [36.439243257400996]

bpp_myself_SIX_06 = [0.9677632649739584]
psnr_myself_SIX_06 = [36.46840360457957]

bpp_myself_SIX_07 = [0.9946933322482637]
psnr_myself_SIX_07 = [36.40668225802234]

bpp_myself_SIX_08 = [0.8879496256510415]
psnr_myself_SIX_08 = [36.348351733617946]

bpp_myself_SIX_09 = [0.9047003851996528]
psnr_myself_SIX_09 = [36.32330645338983]
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
# plt.scatter(bpp_myself_SEC_01, psnr_myself_SEC_01)
# plt.plot(bpp_myself_SEC_01, psnr_myself_SEC_01, label='joint_SEC_01')

# 第三个码率点
# plt.scatter(bpp_myself_THI_01, psnr_myself_THI_01)
# plt.plot(bpp_myself_THI_01, psnr_myself_THI_01, label='joint_THI_01')

# plt.scatter(bpp_myself_THI_02, psnr_myself_THI_02)
# plt.plot(bpp_myself_THI_02, psnr_myself_THI_02, label='joint_THI_02')
# 第四个码率点
# plt.scatter(bpp_myself_FOUR_01, psnr_myself_FOUR_01)
# plt.plot(bpp_myself_FOUR_01, psnr_myself_FOUR_01, label='joint_FOUR_01')

# plt.scatter(bpp_myself_FOUR_02, psnr_myself_FOUR_02)
# plt.plot(bpp_myself_FOUR_02, psnr_myself_FOUR_02, label='joint_FOUR_02')

# plt.scatter(bpp_myself_FOUR_03, psnr_myself_FOUR_03)
# plt.plot(bpp_myself_FOUR_03, psnr_myself_FOUR_03, label='joint_FOUR_03')

# 第五个码率点
# plt.scatter(bpp_myself_FIVE_01, psnr_myself_FIVE_01)
# plt.plot(bpp_myself_FIVE_01, psnr_myself_FIVE_01, label='joint_FIVE_01')

# plt.scatter(bpp_myself_FIVE_02, psnr_myself_FIVE_02)
# plt.plot(bpp_myself_FIVE_02, psnr_myself_FIVE_02, label='joint_FIVE_02')

# plt.scatter(bpp_myself_FIVE_03, psnr_myself_FIVE_03)
# plt.plot(bpp_myself_FIVE_03, psnr_myself_FIVE_03, label='joint_FIVE_03')

# plt.scatter(bpp_myself_FIVE_04, psnr_myself_FIVE_04)
# plt.plot(bpp_myself_FIVE_04, psnr_myself_FIVE_04, label='joint_FIVE_04')

# plt.scatter(bpp_myself_FIVE_05, psnr_myself_FIVE_05)
# plt.plot(bpp_myself_FIVE_05, psnr_myself_FIVE_05, label='joint_FIVE_05')

# plt.scatter(bpp_myself_FIVE_06, psnr_myself_FIVE_06)
# plt.plot(bpp_myself_FIVE_06, psnr_myself_FIVE_06, label='joint_FIVE_06')

# plt.scatter(bpp_myself_FIVE_07, psnr_myself_FIVE_07)
# plt.plot(bpp_myself_FIVE_07, psnr_myself_FIVE_07, label='joint_FIVE_07')

# plt.scatter(bpp_myself_FIVE_08, psnr_myself_FIVE_08)
# plt.plot(bpp_myself_FIVE_08, psnr_myself_FIVE_08, label='joint_FIVE_08')


# plt.scatter(bpp_myself_FIVE_09, psnr_myself_FIVE_09)
# plt.plot(bpp_myself_FIVE_09, psnr_myself_FIVE_09, label='joint_FIVE_09')


# plt.scatter(bpp_myself_FIVE_10, psnr_myself_FIVE_10)
# plt.plot(bpp_myself_FIVE_10, psnr_myself_FIVE_10, label='joint_FIVE_10')

# plt.scatter(bpp_myself_FIVE_11, psnr_myself_FIVE_11)
# plt.plot(bpp_myself_FIVE_11, psnr_myself_FIVE_11, label='joint_FIVE_11')
# 第六个码率点
plt.scatter(bpp_myself_SIX_01, psnr_myself_SIX_01)
plt.plot(bpp_myself_SIX_01, psnr_myself_SIX_01, label='joint_SIX_01')

plt.scatter(bpp_myself_SIX_02, psnr_myself_SIX_02)
plt.plot(bpp_myself_SIX_02, psnr_myself_SIX_02, label='joint_SIX_02')

plt.scatter(bpp_myself_SIX_03, psnr_myself_SIX_03)
plt.plot(bpp_myself_SIX_03, psnr_myself_SIX_03, label='joint_SIX_03')

plt.scatter(bpp_myself_SIX_04, psnr_myself_SIX_04)
plt.plot(bpp_myself_SIX_04, psnr_myself_SIX_04, label='joint_SIX_04')

plt.scatter(bpp_myself_SIX_05, psnr_myself_SIX_05)
plt.plot(bpp_myself_SIX_05, psnr_myself_SIX_05, label='joint_SIX_05')

plt.scatter(bpp_myself_SIX_06, psnr_myself_SIX_06)
plt.plot(bpp_myself_SIX_06, psnr_myself_SIX_06, label='joint_SIX_06')

plt.scatter(bpp_myself_SIX_07, psnr_myself_SIX_07)
plt.plot(bpp_myself_SIX_07, psnr_myself_SIX_07, label='joint_SIX_07')

plt.scatter(bpp_myself_SIX_08, psnr_myself_SIX_08)
plt.plot(bpp_myself_SIX_08, psnr_myself_SIX_08, label='joint_SIX_08')

plt.scatter(bpp_myself_SIX_09, psnr_myself_SIX_09)
plt.plot(bpp_myself_SIX_09, psnr_myself_SIX_09, label='joint_SIX_09')
#添加网格信息
plt.grid(True, linestyle='--', alpha=0.5) #默认是True，风格设置为虚线，alpha为透明度
plt.legend() # 为了能显示label
plt.show()
