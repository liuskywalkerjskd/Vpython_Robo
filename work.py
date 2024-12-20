from vpython import *
import numpy as np

# 创建显示窗口
scene = canvas(title="Simulation", width=600, height=600, center=vector(0, 0, 0),
               background=color.white)
scene.up = vector(0, 0, 1)
scene.forward = vector(-1, 0, 0)
scene.range = 1.2

# 创建坐标轴箭头
arrowX0 = arrow(pos=vector(0, 0, 0), axis=vector(0.1, 0, 0),
                shaftwidth=0.01, color=color.red)
arrowY0 = arrow(pos=vector(0, 0, 0), axis=vector(0, 0.1, 0),
                shaftwidth=0.01, color=color.green)
arrowZ0 = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 0.1),
                shaftwidth=0.01, color=color.blue)

L1 = 0.450
L2 = 0.350 / 2
L3 = 0.280
L4 = 0.390
L5 = 0.315
L6 = 0.094 / 2
L7 = 0.210 / 2
L8 = 0.255
L9 = 0.230
L10 = 0.068

arrowX11 = arrow(pos=vector(0, 0, L1), axis=vector(0.1, 0, 0),
                 shaftwidth=0.01, color=color.red)
arrowY11 = arrow(pos=vector(0, 0, L1), axis=vector(0, 0.1, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ11 = arrow(pos=vector(0, 0, L1), axis=vector(0, 0, 0.1),
                 shaftwidth=0.01, color=color.blue)

Link0 = cylinder(pos=arrowX11.pos, axis=vector(0, 0, 0.1),
                 length=L3 / 2, radius=0.01, color=color.yellow)
ball = sphere(pos=vector(0, 0, L1 + L3 / 2), radius=0.05, color=color.red)

arrowX1 = arrow(pos=vector(0, 0, L1 - L5), axis=vector(0.1, 0, 0),
                shaftwidth=0.01, color=color.red)
arrowY1 = arrow(pos=vector(0, 0, L1 - L5), axis=vector(0, 0.1, 0),
                shaftwidth=0.01, color=color.green)
arrowZ1 = arrow(pos=vector(0, 0, L1 - L5), axis=vector(0, 0, 0.1),
                shaftwidth=0.01, color=color.blue)

rod1 = cylinder(pos=arrowX1.pos, axis=arrowZ1.axis,
                length=0.05, radius=0.02, color=color.cyan)
Link1 = cylinder(pos=arrowX1.pos, axis=vector(0, 0, 0.1),
                 length=L5, radius=0.01, color=color.yellow)
Link1_1 = cylinder(pos=arrowX1.pos, axis=vector(0, 0.1, 0),
                   length=L6, radius=0.01, color=color.yellow)
Link1_2 = cylinder(pos=arrowX1.pos, axis=vector(0, -0.1, 0),
                   length=L6, radius=0.01, color=color.yellow)

arrowX12 = arrow(pos=vector(0, -L2, L1), axis=vector(0, 0, -0.1),
                 shaftwidth=0.01, color=color.red)
arrowY12 = arrow(pos=vector(0, -L2, L1), axis=vector(0.1, 0, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ12 = arrow(pos=vector(0, -L2, L1), axis=vector(0, -0.1, 0),
                 shaftwidth=0.01, color=color.blue)

rod12 = cylinder(pos=arrowX12.pos - 0.5 * arrowZ12.axis, axis=-arrowZ12.axis,
                 length=0.05, radius=0.02, color=color.cyan)
rod22 = cylinder(pos=arrowX12.pos - 2.5 * arrowZ12.axis, axis=-arrowZ12.axis,
                 length=0.05, radius=0.02, color=color.cyan)
Link2 = cylinder(pos=arrowX12.pos, axis=-arrowZ12.axis,
                 length=2 * L2, radius=0.01, color=color.yellow)

arrowX13 = arrow(pos=vector(0, -L2, L1), axis=vector(0, 0, -0.1),
                 shaftwidth=0.01, color=color.red)
arrowY13 = arrow(pos=vector(0, -L2, L1), axis=vector(0, -0.1, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ13 = arrow(pos=vector(0, -L2, L1), axis=vector(-0.1, 0, 0),
                 shaftwidth=0.01, color=color.blue)

rod13_1 = cylinder(pos=arrowX13.pos, axis=arrowZ13.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod13_2 = cylinder(pos=arrowX13.pos, axis=arrowZ13.axis,
                   length=-0.05, radius=0.02, color=color.cyan)
rod23_1 = cylinder(pos=vector(0, L2, L1), axis=arrowZ13.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod23_2 = cylinder(pos=vector(0, L2, L1), axis=arrowZ13.axis,
                   length=-0.05, radius=0.02, color=color.cyan)
Link3_1 = cylinder(pos=arrowX13.pos, axis=vector(0, 0, -0.1),
                   length=L3, radius=0.01, color=color.yellow)
Link3_2 = cylinder(pos=vector(0, L2, L1), axis=vector(0, 0, -0.1),
                   length=L3, radius=0.01, color=color.yellow)

arrowX14 = arrow(pos=vector(0, -L2, L1 - L3), axis=vector(0.1, 0, 0),
                 shaftwidth=0.01, color=color.red)
arrowY14 = arrow(pos=vector(0, -L2, L1 - L3), axis=vector(0, -0.1, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ14 = arrow(pos=vector(0, -L2, L1 - L3), axis=vector(0, 0, -0.1),
                 shaftwidth=0.01, color=color.blue)

rod14 = cylinder(pos=arrowX14.pos, axis=-arrowZ14.axis,
                 length=0.05, radius=0.02, color=color.cyan)
rod24 = cylinder(pos=vector(0, L2, L1 - L3), axis=-arrowZ14.axis,
                 length=0.05, radius=0.02, color=color.cyan)

arrowX15 = arrow(pos=vector(0, -L2, L1 - L3), axis=vector(0, 0, -0.1),
                 shaftwidth=0.01, color=color.red)
arrowY15 = arrow(pos=vector(0, -L2, L1 - L3), axis=vector(0.1, 0, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ15 = arrow(pos=vector(0, -L2, L1 - L3), axis=vector(0, -0.1, 0),
                 shaftwidth=0.01, color=color.blue)

rod15_1 = cylinder(pos=arrowX15.pos, axis=arrowZ15.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod15_2 = cylinder(pos=arrowX15.pos, axis=arrowZ15.axis,
                   length=-0.05, radius=0.02, color=color.cyan)
rod25_1 = cylinder(pos=vector(0, L2, L1 - L3), axis=arrowZ15.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod25_2 = cylinder(pos=vector(0, L2, L1 - L3), axis=arrowZ15.axis,
                   length=-0.05, radius=0.02, color=color.cyan)

Link4_1 = cylinder(pos=arrowX15.pos, axis=vector(0, 0, -0.1),
                   length=L4, radius=0.01, color=color.red)  # red link
Link4_2 = cylinder(pos=vector(0, L2, L1 - L3), axis=vector(0, 0, -0.1),
                   length=L4, radius=0.01, color=color.yellow)

arrowX16 = arrow(pos=vector(0, -L6, L1 - L5), axis=vector(0.1, 0, 0),
                 shaftwidth=0.01, color=color.red)
arrowY16 = arrow(pos=vector(0, -L6, L1 - L5), axis=vector(0, 0.1, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ16 = arrow(pos=vector(0, -L6, L1 - L5), axis=vector(0, 0, 0.1),
                 shaftwidth=0.01, color=color.blue)
rod16 = cylinder(pos=arrowX16.pos, axis=-arrowZ16.axis,
                 length=0.05, radius=0.02, color=color.cyan)
rod26 = cylinder(pos=vector(0, L6, L1 - L5), axis=-arrowZ16.axis,
                 length=0.05, radius=0.02, color=color.cyan)
Link5_1 = cylinder(pos=vector(0, -L6, L1 - L5), axis=vector(0, 0, -0.1),
                   length=L1 - L5, radius=0.01, color=color.yellow)
Link5_2 = cylinder(pos=vector(0, L6, L1 - L5), axis=vector(0, 0, -0.1),
                   length=L1 - L5, radius=0.01, color=color.yellow)
Link5_3 = cylinder(pos=vector(0, -L6, 0), axis=vector(0, -0.1, 0),
                   length=L7 - L6, radius=0.01, color=color.yellow)
Link5_4 = cylinder(pos=vector(0, L6, 0), axis=vector(0, 0.1, 0),
                   length=L7 - L6, radius=0.01, color=color.yellow)

arrowX17 = arrow(pos=vector(0, -L7, 0), axis=vector(0, 0, -0.1),
                 shaftwidth=0.01, color=color.red)
arrowY17 = arrow(pos=vector(0, -L7, 0), axis=vector(0.1, 0, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ17 = arrow(pos=vector(0, -L7, 0), axis=vector(0, -0.1, 0),
                 shaftwidth=0.01, color=color.blue)
rod17 = cylinder(pos=arrowX17.pos, axis=-arrowZ17.axis,
                 length=0.05, radius=0.02, color=color.cyan)
rod27 = cylinder(pos=vector(0, L7, 0), axis=arrowZ17.axis,
                 length=0.05, radius=0.02, color=color.cyan)

arrowX18 = arrow(pos=vector(0, -L7, 0), axis=vector(0, 0, -0.1),
                 shaftwidth=0.01, color=color.red)
arrowY18 = arrow(pos=vector(0, -L7, 0), axis=vector(0, -0.1, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ18 = arrow(pos=vector(0, -L7, 0), axis=vector(-0.1, 0, 0),
                 shaftwidth=0.01, color=color.blue)
rod18_1 = cylinder(pos=arrowX18.pos, axis=arrowZ18.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod18_2 = cylinder(pos=arrowX18.pos, axis=arrowZ18.axis,
                   length=-0.05, radius=0.02, color=color.cyan)
rod28_1 = cylinder(pos=vector(0, L7, 0), axis=arrowZ18.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod28_2 = cylinder(pos=vector(0, L7, 0), axis=arrowZ18.axis,
                   length=-0.05, radius=0.02, color=color.cyan)
Link6_1 = cylinder(pos=vector(0, -L7, 0), axis=vector(0, 0, -0.1),
                   length=L8 + L9 + L10, radius=0.01, color=color.yellow)
Link6_2 = cylinder(pos=vector(0, L7, 0), axis=vector(0, 0, -0.1),
                   length=L8 + L9 + L10, radius=0.01, color=color.yellow)

arrowX19 = arrow(pos=vector(0, -L7, -L8), axis=vector(0, 0, -0.1),
                 shaftwidth=0.01, color=color.red)
arrowY19 = arrow(pos=vector(0, -L7, -L8), axis=vector(0.1, 0, 0),
                 shaftwidth=0.01, color=color.green)
arrowZ19 = arrow(pos=vector(0, -L7, -L8), axis=vector(0, -0.1, 0),
                 shaftwidth=0.01, color=color.blue)
rod19_1 = cylinder(pos=arrowX19.pos, axis=-arrowZ19.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod19_2 = cylinder(pos=arrowX19.pos, axis=arrowZ19.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod29_1 = cylinder(pos=vector(0, L7, -L8), axis=-arrowZ19.axis,
                   length=0.05, radius=0.02, color=color.cyan)
rod29_2 = cylinder(pos=vector(0, L7, -L8), axis=arrowZ19.axis,
                   length=0.05, radius=0.02, color=color.cyan)

arrowX110 = arrow(pos=vector(0, -L7, -L8 - L9), axis=vector(0, 0, -0.1),
                  shaftwidth=0.01, color=color.red)
arrowY110 = arrow(pos=vector(0, -L7, -L8 - L9), axis=vector(0, -0.1, 0),
                  shaftwidth=0.01, color=color.green)
arrowZ110 = arrow(pos=vector(0, -L7, -L8 - L9), axis=vector(-0.1, 0, 0),
                  shaftwidth=0.01, color=color.blue)
rod110_1 = cylinder(pos=arrowX110.pos, axis=arrowZ110.axis,
                    length=0.05, radius=0.02, color=color.cyan)
rod110_2 = cylinder(pos=arrowX110.pos, axis=arrowZ110.axis,
                    length=-0.05, radius=0.02, color=color.cyan)
rod210_1 = cylinder(pos=vector(0, L7, -L8 - L9), axis=arrowZ110.axis,
                    length=0.05, radius=0.02, color=color.cyan)
rod210_2 = cylinder(pos=vector(0, L7, -L8 - L9), axis=arrowZ110.axis,
                    length=-0.05, radius=0.02, color=color.cyan)

arrowX111 = arrow(pos=vector(0, -L7, -L8 - L9), axis=vector(0, 0, -0.1),
                  shaftwidth=0.01, color=color.red)
arrowY111 = arrow(pos=vector(0, -L7, -L8 - L9), axis=vector(0.1, 0, 0),
                  shaftwidth=0.01, color=color.green)
arrowZ111 = arrow(pos=vector(0, -L7, -L8 - L9), axis=vector(0, -0.1, 0),
                  shaftwidth=0.01, color=color.blue)
rod111_1 = cylinder(pos=arrowX111.pos, axis=-arrowZ111.axis,
                    length=0.05, radius=0.02, color=color.cyan)
rod111_2 = cylinder(pos=arrowX111.pos, axis=arrowZ111.axis,
                    length=0.05, radius=0.02, color=color.cyan)
rod211_1 = cylinder(pos=vector(0, L7, -L8 - L9), axis=-arrowZ111.axis,
                    length=0.05, radius=0.02, color=color.cyan)
rod211_2 = cylinder(pos=vector(0, L7, -L8 - L9), axis=arrowZ111.axis,
                    length=0.05, radius=0.02, color=color.cyan)

box1 = box(pos=vector(0, -L7, -L8 - L9 - L10), axis=vector(0, 0, -1),
           length=0.01, height=0.1, width=0.13, color=color.blue)
box2 = box(pos=vector(0, L7, -L8 - L9 - L10), axis=vector(0, 0, -1),
           length=0.01, height=0.1, width=0.13, color=color.blue)
ball = sphere(make_trail=True, trail_type="points", interval=100,
              retain=500, radius=0.01, color=color.red)

q11 = 0
q13 = 0
q14 = 0
dt = -0.01
t = 0

while True:
    rate(200)  # 控制循环更新频率

    t += dt  # 更新时间
    x = 0.3 + 0.1 * np.sin(t)
    z = 0.1 * np.cos(t)
    
    a = np.arctan((L1 - z) / x)
    p = np.sqrt((L1 - z) ** 2 + x ** 2)
    q12 = np.arcsin((p ** 2 + L3 ** 2 - L4 ** 2) / (2 * p * L3)) - a
    q15 = np.arccos(-(np.cos(q12) * (z - L1) - x * np.sin(q12) + L3) / L4)
    
    # 更新各个变换矩阵
    T11_00 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, L1], [0, 0, 0, 1]])
    Rz_q11 = np.array([[np.cos(q11), -np.sin(q11), 0, 0], [np.sin(q11), np.cos(q11), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    T11_0 = np.dot(T11_00, Rz_q11)
    
    T12_110 = np.array([[0, 1, 0, 0], [0, 0, -1, -L2], [-1, 0, 0, 0], [0, 0, 0, 1]])
    Rz_q12 = np.array([[np.cos(q12), -np.sin(q12), 0, 0], [np.sin(q12), np.cos(q12), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    T12_11 = np.dot(T12_110, Rz_q12)
    
    T13_120 = np.array([[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    Rz_q13 = np.array([[np.cos(q13), -np.sin(q13), 0, 0], [np.sin(q13), np.cos(q13), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    T13_12 = np.dot(T13_120, Rz_q13)
    
    T14_130 = np.array([[0, 0, 1, L3], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]])
    Rz_q14 = np.array([[np.cos(q14), -np.sin(q14), 0, 0], [np.sin(q14), np.cos(q14), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    T14_13 = np.dot(T14_130, Rz_q14)
    
    T15_140 = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]])
    Rz_q15 = np.array([[np.cos(q15), -np.sin(q15), 0, 0], [np.sin(q15), np.cos(q15), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    T15_14 = np.dot(T15_140, Rz_q15)
    
    T16_15 = np.array([[1, 0, 0, L4], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    # 计算最终变换矩阵
    T12_0 = np.dot(T11_0, T12_11)
    T13_0 = np.dot(T12_0, T13_12)
    T14_0 = np.dot(T13_0, T14_13)
    T15_0 = np.dot(T14_0, T15_14)
    T16_0 = np.dot(T15_0, T16_15)
    
    # 更新箭头的位置和方向
    arrowX11.pos = vector(*T11_0[0:3, 3])
    arrowY11.pos = vector(*T11_0[0:3, 3])
    arrowZ11.pos = vector(*T11_0[0:3, 3])
    arrowX11.axis = vector(*T11_0[0:3, 0]) * 0.1
    arrowY11.axis = vector(*T11_0[0:3, 1]) * 0.1
    arrowZ11.axis = vector(*T11_0[0:3, 2]) * 0.1
    
    arrowX12.pos = vector(*T12_0[0:3, 3])
    arrowY12.pos = vector(*T12_0[0:3, 3])
    arrowZ12.pos = vector(*T12_0[0:3, 3])
    arrowX12.axis = vector(*T12_0[0:3, 0]) * 0.1
    arrowY12.axis = vector(*T12_0[0:3, 1]) * 0.1
    arrowZ12.axis = vector(*T12_0[0:3, 2]) * 0.1
    
    arrowX13.pos = vector(*T13_0[0:3, 3])
    arrowY13.pos = vector(*T13_0[0:3, 3])
    arrowZ13.pos = vector(*T13_0[0:3, 3])
    arrowX13.axis = vector(*T13_0[0:3, 0]) * 0.1
    arrowY13.axis = vector(*T13_0[0:3, 1]) * 0.1
    arrowZ13.axis = vector(*T13_0[0:3, 2]) * 0.1
    
    arrowX14.pos = vector(*T14_0[0:3, 3])
    arrowY14.pos = vector(*T14_0[0:3, 3])
    arrowZ14.pos = vector(*T14_0[0:3, 3])
    arrowX14.axis = vector(*T14_0[0:3, 0]) * 0.1
    arrowY14.axis = vector(*T14_0[0:3, 1]) * 0.1
    arrowZ14.axis = vector(*T14_0[0:3, 2]) * 0.1
    
    arrowX15.pos = vector(*T15_0[0:3, 3])
    arrowY15.pos = vector(*T15_0[0:3, 3])
    arrowZ15.pos = vector(*T15_0[0:3, 3])
    arrowX15.axis = vector(*T15_0[0:3, 0]) * 0.1
    arrowY15.axis = vector(*T15_0[0:3, 1]) * 0.1
    arrowZ15.axis = vector(*T15_0[0:3, 2]) * 0.1
    
    # 更新连接物
    Link3_1.pos = arrowX12.pos
    Link3_1.axis = arrowX12.axis
    Link3_1.length = L3
    
    Link4_1.pos = arrowX15.pos
    Link4_1.axis = arrowX15.axis
    Link4_1.length = L4
    
    # 更新杆的位置和方向
    rod14.pos = arrowX14.pos
    rod14.axis = arrowZ14.axis
    rod14.length = 0.05
    
    rod15_1.pos = arrowX15.pos
    rod15_1.axis = -arrowZ15.axis
    rod15_1.length = 0.05
    
    rod15_2.pos = arrowX15.pos
    rod15_2.axis = -arrowZ15.axis
    rod15_2.length = -0.05
    
    # 更新球的位置
    ball.pos = vector(*T16_0[0:3, 3])
