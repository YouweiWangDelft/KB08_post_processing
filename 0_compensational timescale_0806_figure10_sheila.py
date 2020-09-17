# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 21:14:15 2019

@author: youweiwang
"""
import numpy as np
import matplotlib.pyplot as plt
import erosion_time_space_0806 #another python file where the matrix is generated


a = erosion_time_space_0806.erosion   # m by n matrix with row (m) of time, column (n) of location and value (a[m][n]) of depositional rate



def mean_many(window): # this is to make a function of windows for depositional rate at a cross-valley distance of x
    a_new  = []
    a_mean = [] 
    for start in range(0, len(a)-window):
        a_temp = np.mean(a[start:start+window+1],axis=0)
        a_new.append(a_temp)
        
    a_new = np.asarray(a_new)
    return a_new

my_mean = {}  # to make a dictionary, with window as the keyword
my_sigma = []  
for window in range(0,len(a)):
    my_mean[window] = mean_many(window)
    my_sigma.append((np.array(my_mean[window])/0.4-1)**2) #0.4 is my long-term average deposition rate

my_sigma_mean = []
for i in range(len(my_sigma)):
    my_sigma_mean.append(my_sigma[i].mean(axis=1))
    

fig = plt.figure(figsize=(12,8))
ax = plt.subplot(111)
for i in range(len(my_sigma_mean)):
    plt.scatter(np.zeros(len(my_sigma_mean[i]))+i*100,np.sqrt(my_sigma_mean[i]*200),color = 'gray') # all dots
    plt.scatter(i*100,np.mean(np.sqrt(my_sigma_mean[i]*200)),marker = 's', color = 'r', zorder = 2) # mean values
    #plt.errorbar(i*100,np.mean(sqrt(my_sigma_mean[i]*200)),yerr=1*np.std(sqrt(my_sigma_mean[i]*200)),fmt='o',ecolor='gray',color='k',elinewidth=2,capsize=4)
    
    
    plt.plot(i*100,np.mean(np.sqrt(my_sigma_mean[i]*200))+1*np.std(np.sqrt(my_sigma_mean[i]*200)),'-o', color = 'cyan')
    plt.plot(i*100,np.mean(np.sqrt(my_sigma_mean[i]*200))-1*np.std(np.sqrt(my_sigma_mean[i]*200)),'-o', color = 'cyan')
    ax.set_yscale('log')
    ax.set_xscale('log')
    #plt.xticks([10,100],[100,1000])
    plt.axvline(x=2000,linestyle='--',color = 'k',linewidth = 3)
    plt.ylim(0,300)
    plt.xlim(90,40000)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.xlabel('time window (years)',fontsize = 20)
    plt.ylabel(r'$\sigma_{ss}$',fontsize = 25)
    
    #ax = extended(ax, [2000,30000],[np.mean(sqrt(my_sigma_mean[20]*200)),np.mean(sqrt(my_sigma_mean[300]*200))], color="r", lw=2, label="extended")
    plt.plot([2000,30000],[np.mean(np.sqrt(my_sigma_mean[20]*200)),np.mean(np.sqrt(my_sigma_mean[300]*200))],'--', color = 'k',linewidth = 3)
    
    plt.plot([2000,200],[np.mean(np.sqrt(my_sigma_mean[20]*200)),np.mean(np.sqrt(my_sigma_mean[2]*200))],'--', color = 'k',linewidth = 3)

