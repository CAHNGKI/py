import matplotlib.pyplot as plt

fig = plt.figure()

ax1 =fig.add_subplot(2,1,1)
ax2 =fig.add_subplot(2,1,2)

x = range(0,100)
y = [v*v for v in x]
z = [v*v*2 for v in x]

ax1.plot(x,y,'b',z,'r')
ax2.bar(x,z)

plt.show()
