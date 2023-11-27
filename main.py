##############################Функція з однією змінною##########################
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar


def f(x):
    return 3*np.sin(x) + 2*np.cos(x)


x_min = round(minimize_scalar(f, bounds=[-2, 2]).x, 2)
f_min = round(f(x_min), 2)

x_values = np.linspace(-2, 2, 100)
f_values = f(x_values)

plt.plot(x_values, f_values, label='$f(x)$')
plt.scatter(x_min, f_min, color='red', label=f'x_min = {x_min}, f(x_min) = {f_min}')
plt.title('$f(x) = 3sinx(x) + 2cos(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
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
# plt.scatter(x_min[0], x_min[1], s=40, c='k', marker='x', label='min', linewidths=2)
# ax2.set_title('Карта ліній рівня (XOZ)')
# ax2.set_xlabel('X')
# ax2.set_ylabel('Z')
# ax2.legend()
# plt.colorbar(contour, ax=ax2)
#
# ax3 = fig.add_subplot(133)
# contour = ax3.contourf(Y, Z, X, cmap='coolwarm', levels=20)
# ax3.scatter(x_min[0], x_min[1], s=40, c='k', marker='x', label='min', linewidths=2)
# ax3.set_title('Карта ліній рівня (YOZ)')
# ax3.set_xlabel('Y')
# ax3.set_ylabel('Z')
# ax3.legend()
# plt.colorbar(contour, ax=ax3)
#
# plt.tight_layout()
# plt.show()
