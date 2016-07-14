## problem 4.7 4.9

>##摘要
行星运动是天文学的重要研究方向。对于太阳系中行星的运动，我们既有解析解，又有数值解，是发展数值计算方法的良好实验室。
本文使用Euler-Cromer方法，对开普勒定律以及行星运动进行了研究。同时回答了4.7,4.9题。

>##背景
具体讨论了双星系统与通常的具有较大质量的恒星与行星体系的轨迹区别和质量相等的两体运动以及讨论质量相等的三体运动轨迹。

>##正文
关于双星系统，并且假定系统在初始状态下，总角动量为零，先后讨论了质量相等与不等的情形，在原有天文单位制列出的运动微分方程的基础，加以一定的修正，具体如下  
![1](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/1.gif)  
![2](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/2.gif)  
![3](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/3.gif)  
![4](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.11/4.gif)  
你可以在这里得到我的[代码](https://github.com/lzx78966/computationalphysics_N2014301020035/blob/master/Chapter4.1/problem4.7.py)。
通过修正后的运动微分方程所绘得的行星运动轨迹为下图所示：  
这是质量相同时两体的轨迹：  
![5](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/5.png)  
这是质量不同时两体的轨迹：  
![6](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/6.png)
上文中我们考虑的都是两体问题，这里我们考虑三体问题。我们知道，三体系统是一个混沌系统，我们预见其运动轨迹将会十分复杂。
令三个质量相等的太阳放在一个我任意选择的三角形的三个顶点，并且总动量为0。我任选了三个三角形做实验。  
你可以在这里得到我的[代码](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/problem4.9.py)。
三颗恒星的运动轨迹为下图：  
![7](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/7.png)  
![8](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/8.png)  
![9](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter4.1/9.png)  
图中的红点为三颗太阳的起始位置，黑点为绘图时它们所处的位置。

>##结论
在两体问题中，由图可知，质量大的恒星的轨道范围小，质量小的行星的轨道范围大。在三体问题中，由图可知，三体的运动很容易陷入混沌状态。三颗恒星的运动是难以预测的。



