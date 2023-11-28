##############################Функція з однією змінною##########################
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, differential_evolution, Bounds


def f(x):
    return np.sin(x) * np.cos(0.5 * x)


x_local_min = round(minimize_scalar(f, bounds=[0, 5]).x, 2)
f_local_min = round(f(x_local_min), 2)
x_local_max = round(-minimize_scalar(f, bounds=[0, 5]).x, 2)
f_local_max = round(f(x_local_max), 2)

x_global_min = round(differential_evolution(f, bounds=[(-10, 10)]).x[0], 2)
f_global_min = round(f(x_global_min), 2)
x_global_max = round(-minimize_scalar(f, bounds=[-10, 10]).x, 2)
f_global_max = round(f(x_global_max), 2)

x_values = np.linspace(-10, 10, 1000)
f_values = f(x_values)

plt.plot(x_values, f_values, label='$f(x)$')
plt.scatter(x_local_min, f_local_min, color='red', label=f'x_local_min = {x_local_min}, f(x_local_min) = {f_local_min}', marker='o')
plt.scatter(x_global_min, f_global_min, color='black', label=f'x_global_min = {x_global_min}, f(x_global_min) = {f_global_min}', marker='x')
plt.scatter(x_local_max, f_local_max, color='green', label=f'x_local_max = {x_local_max}, f(x_local_max) = {f_local_max}', marker='o')
plt.scatter(x_global_max, f_global_max, color='purple', label=f'x_global_max = {x_global_max}, f(x_global_max) = {f_global_max}', marker='x')
plt.title('$f(x) = sin(x) * cos(0.5x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()



############################Функція з двома змінними###############################
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.optimize import minimize
#
#
# def f(x_y):
#     x = x_y[0]
#     y = x_y[1]
#     return np.sin(x) * np.cos(y)
#
#
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(x, y)
# Z = f([X, Y])
# x_min = minimize(f, (-5, -5), method="Nelder-Mead").x
# z_min = f(x_min)
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection="3d")
# ax.plot_surface(X, Y, Z, edgecolor='grey', lw=0.5, rstride=8, cstride=8,
#                 alpha=0.8, cmap="coolwarm")
# ax.scatter(x_min[0], x_min[1], z_min, s=50, c='k', marker="o")
# p1 = ax.contour(X, Y, Z, zdir='z', offset=-8, cmap='coolwarm')
# p1 = ax.contour(X, Y, Z, zdir='x', offset=-3, cmap='coolwarm')
# p1 = ax.contour(X, Y, Z, zdir='y', offset=6, cmap='coolwarm')
# ax.set(xlim=(-5, 5), ylim=(-5, 5), zlim=(-1.5, 1.5), xlabel='X', ylabel='Y', zlabel='Z')
# plt.title("$Z = sin(x) * cos(y)$")
# plt.show()
#
#
# fig = plt.figure()
# ax1 = fig.add_subplot(131)
# contour = ax1.contourf(X, Y, Z, cmap='coolwarm', levels=20)
# ax1.scatter(x_min[0], x_min[1], s=40, c='k', marker='x', label='min', linewidths=2)
# ax1.set_title('Карта ліній рівня (XOY)')
# ax1.set_xlabel('X')
# ax1.set_ylabel('Y')
# ax1.legend()
# plt.colorbar(contour, ax=ax1)
#
# ax2 = fig.add_subplot(132)
# contour = ax2.contourf(X, Z, Y, cmap='coolwarm', levels=20)
# plt.scatter(x_min[0], z_min, s=40, c='k', marker='x', label='min', linewidths=2)
# ax2.set_title('Карта ліній рівня (XOZ)')
# ax2.set_xlabel('X')
# ax2.set_ylabel('Z')
# ax2.legend()
# plt.colorbar(contour, ax=ax2)
#
# ax3 = fig.add_subplot(133)
# contour = ax3.contourf(Y, Z, X, cmap='coolwarm', levels=20)
# ax3.scatter(x_min[1], z_min, s=40, c='k', marker='x', label='min', linewidths=2)
# ax3.set_title('Карта ліній рівня (YOZ)')
# ax3.set_xlabel('Y')
# ax3.set_ylabel('Z')
# ax3.legend()
# plt.colorbar(contour, ax=ax3)
#
# plt.tight_layout()
# plt.show()
