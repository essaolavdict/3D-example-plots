# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: 3D-example-plots
#     language: python
#     name: 3d-example-plots
# ---

# %% [markdown]
# # Notebook for 3D plot visualizations

# %% [markdown]
# #### Import modules:

# %%
# %matplotlib ipympl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# %% [markdown]
# #### Set plot style:

# %%
sns.set_theme(style="white", context="talk")

# %% [markdown]
# #### Generate data:

# %%
u = np.linspace(0, 2 * np.pi, 200)
v = np.linspace(-1, 1, 50)
u, v = np.meshgrid(u, v)

x = (1 + 0.5 * v * np.cos(u / 2)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2)

# %% [markdown]
# #### Plot:

# %%
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(projection="3d")

surf = ax.plot_surface(
    x, y, z,
    cmap=sns.color_palette("magma", as_cmap=True),
    edgecolor="none",
    alpha=0.95
)

ax.set_box_aspect([1, 1, 0.5])
ax.set_axis_off()
ax.view_init(elev=50, azim=10)
ax.set_title('Möbius strip')

plt.show()

# %%
