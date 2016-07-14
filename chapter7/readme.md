## problem 7.3

>##摘要
本文中我们考虑这样一类系统，其中随机性占据重要位置。这些系统一般含有较大数目的“自由度”，在这种系统中，尽管理论上每个粒子的运动可以由力学定律决定，但是这会带来天文数字的微分方程，难以实际求解。为此，我们使用概率论来描述这个系统，使得原系统和这个随机系统在某些我们感兴趣的宏观性质上一致。通过探究这个随机系统，我们可以了解真实系统的情况。

>##背景
本章重点讨论了随机系统，随机系统不同于我们通常所研究的系统，他拥有非常多的自由度，通常不能运用以往的像是描述抛体运动的微分方程组这类的模型来描述，而且在某个时间点上，随机系统出现的结果并不确定，而是概率事件，所以我们可以用统计模型去研究随机系统。

>##正文
一维方向上的随机运动，以原点为起点，每个步长是确定的，但是向左向右在某一个时间点确实不确定的，但是在没有其他外力的条件下，向左向右的概率相等，这可以视作扩散运动的一维描述。  
你可以在这里得到[代码1](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter7/exercise15/problem7.3.1.py)。  
这是x关于步数的分布图像：  
![1](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter7/exercise15/1.png)  
你可以在这里得到[代码2](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter7/exercise15/problem7.3.2.py)。
离原点距离平方随步数的变化关系图像为：  
![2](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter7/exercise15/2.png)  
由图可知，此时的x的平方的平均值与步数近似为线性关系，此过程也是“类扩散的”。
接下来将程序稍作修改，让向右行走的概率为0.75，向左为0.25，固定步长为1.你可以在这里得到[代码3](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter7/exercise15/problem7.3.3.py)和[代码4](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter7/exercise15/problem7.3.4.py)，观察两种平均值随步长的变化关系图像为：  
![3](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter7/exercise15/3.png)  
![4](https://github.com/zhangzhihan/computationalphysics_N2014301020035/blob/master/Chapter7/exercise15/4.png)  
由于左右概率不同，可见x的平均值随步数线性增大，其平方的平均与步数成二次关系。

>##结论
从上述图示，不难发现，如果改变了相应的统计规律，粒子的运动会以一个大趋势向某一个方向运动，尽管偶尔会有涨落，但是趋势是确定的，而从与时间t的关系来看，后来的关系已经大幅偏离原来的拟合结果，故在此种情况下，该运动不在具有扩散的特征。

