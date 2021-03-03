import matplotlib.pyplot as plt
views=[23,43,54,65,76,86]
fviews=[43,56,74,45,65,32]
xviews=[34,64,65,76,43,21]
x=[1,2,3,4,5,6]
""""
plt.plot(days,views,label='utube views',color='r',marker='h',markerfacecolor='g',ls='--',lw='5',mec='k',mew='5')  #mentioning name to aa data line  plt.scatter()
plt.plot(days,fviews,label='facebook views',color='b',marker='h',markerfacecolor='g',ls='--',lw='5',mec='k',mew='5')
plt.plot(days,xviews,label='twitter views',color='k',marker='h',markerfacecolor='g',ls='--',lw='5',mec='k',mew='5')"""
plt.bar([a-0.10 for a in x],views,label='utube views',width=0.10)  #mentioning name to aa data line  plt.scatter()
plt.bar([a+0.10 for a in x],fviews,label='facebook views',width=0.1)
plt.bar([a+0.20 for a in x],xviews,label='twitter views',width=0.1)

plt.xlabel('day.no.')                               #mentioning name  on x,y axis
plt.ylabel('views')
plt.legend()                                        #calling ,we can set position as legend(loc='upper right')
plt.grid(True,lw='3')
plt.show()                                      #for limits in axis as plt.xlim(),ylim()