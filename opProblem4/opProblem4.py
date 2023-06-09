import matplotlib.pyplot as plt
import cvxpy as cp
import numpy as np

a=[0.5, -0.5, 0.2, -0.7, 0.6, -0.2, 0.7, -0.5, 0.8, -0.4]
l=[40, 20, 40, 40, 20, 40, 30, 40, 30, 60]
Preq=np.arange(a[0],a[0]*(l[0]+0.5),a[0])

for i in range(1, len(l)):
    Preq=np.r_[ Preq, np.arange(Preq[-1]+a[i],Preq[-1]+a[i]*(l[i]+0.5),a[i]) ]

T = sum(l)

Peng_max = 20.0
Pmg_min = -6.0
Pmg_max = 6.0
Ebatt_max = 100.0
eta = 0.1
gamma = 0.1

#-------------------------Task 1--------------------------#
#------------------------Variables------------------------#
#Energy in battery
E = cp.Variable(T+1,nonneg=True)

#Power absorbed by friction break
Pbr = cp.Variable(T,nonneg=True)

#Power generated by combustion engine
Peng = cp.Variable(T,nonneg=True)

#Power generated/absorbed by motor/generator
Pmg =cp.Variable(T)

#-----------------------Constraints-----------------------#
constraints=[Pmg_min <= Pmg,
             Pmg <= Pmg_max,
             Peng <= Peng_max,
             E <= Ebatt_max,
             E[0]==E[T],
             Preq == Peng + Pmg - Pbr,
             E[1:] <= E[:-1] - Pmg - eta*cp.abs(Pmg)]

"""
WHY IS  IT EQUIVALENT?

We have relaxed the last constraint by removing ">=" and keeping "<=".
We keep the inequality that prevents the creation of power,
but we remove the one that prevents the destruction of power in the motor/generator.
Destroying power is not good for fuel efficiency, so we expect that it won't happen.
It can only happen when energy is abundant, but we can fix it by moving all that
energy destruction from the motor/generator to the friction break. Since Pbr is
unbounded from above, it can handle any excess power.
"""


#------------------------Objective------------------------#
objective = cp.Minimize(cp.sum(Peng)+gamma*cp.sum_squares(Peng))


#-------------------------Task 2--------------------------#
#------------------------Solution-------------------------#
prob = cp.Problem(objective, constraints)
solution1 = prob.solve()
print("Objective1:",solution1)
E1=np.copy(E.value)
Pmg1=np.copy(Pmg.value)
Pbr1=np.copy(Pbr.value)
Peng1=np.copy(Peng.value)

#--------------------------Plot---------------------------#
fig, ax = plt.subplots(2)

ax[0].plot(Preq,label="Preq")
ax[0].plot(Pmg.value,c=0,label="Pmg")
ax[0].plot(Peng.value,label="Peng")
ax[0].plot(Pbr.value,label="Pbr")
ax[1].plot(E.value,label="E")

ax[0].set_title("Power vs Time")
ax[0].set_ylabel("Power")
ax[0].set_xlabel("Time")

ax[1].set_title("Energy vs Time")
ax[1].set_ylabel("Energy Stored in Battery")
ax[1].set_xlabel("Time")

ax[0].legend()
ax[1].legend()

plt.show()



#-------------------------Task 3--------------------------#
#-------------Comparison with Battery-less Car------------#

Ebatt_max = 0.0
constraints2=[Pmg_min <= Pmg,
             Pmg <= Pmg_max,
             Peng <= Peng_max,
             E <= Ebatt_max,
             E[0]==E[T],
             Preq == Peng + Pmg - Pbr,
             E[1:] <= E[:-1] - Pmg - eta*cp.abs(Pmg)]


prob2 = cp.Problem(objective, constraints2)
solution2 = prob2.solve()
E2=np.copy(E.value)
Pmg2=np.copy(Pmg.value)
Pbr2=np.copy(Pbr.value)
Peng2=np.copy(Peng.value)
print("Objective2:",solution2)
change_in_power_consumption = solution2 - solution1
print("Difference in objective caused by battery",change_in_power_consumption)

#-----------------Plot Car with no Battery----------------#  

fig, ax = plt.subplots()
ax.plot(Preq,label="Preq")
ax.plot(Pmg2,label="Pmg")
ax.plot(Peng2,label="Peng")
ax.plot(Pbr2,label="Pbr")
ax.set_title("Power in Car with No Battery")
ax.set_ylabel("Power")
ax.set_xlabel("Time")

ax.legend()
plt.show()


#-------------------------Task 4--------------------------#
#---------------------Glitch Handling---------------------#

epsilon=0.0001
objective2 = cp.Minimize(cp.sum(Peng)+gamma*cp.sum_squares(Peng)+epsilon*cp.sum((cp.maximum(0,-Pmg))))
prob3 = cp.Problem(objective2, constraints)
solution3 = prob3.solve()
print("Epsilon:",epsilon)
print("Objective3:",solution3)
print("Difference in objective caused by changing the objective:", solution3-solution1)
#When epsilon is chosen to be 0.0001 the increase in the power consumption is 0.0264





    


