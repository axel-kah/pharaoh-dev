# source: https://matplotlib.org/stable/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py


import matplotlib.pyplot as plt
import numpy as np

from pharaoh.assetlib.api import metadata_context

# Fixing random seed for reproducibility
np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))  # white noise 1
nse2 = np.random.randn(len(t))  # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(2, 1)
fig: plt.Figure
axs: list[plt.Axes]
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel("time")
axs[0].set_ylabel("s1 and s2")
axs[0].grid(True)

cxy, f = axs[1].cohere(s1, s2, NFFT=256, Fs=1.0 / dt)
axs[1].set_ylabel("coherence")

fig.tight_layout()

with metadata_context(label="MPL"):
    fig.savefig(
        "co he-rence  1.png",  # try with whitespace in path, see https://github.com/Infineon/pharaoh-dev/issues/32
    )
    fig.savefig("coherence2.svg")
plt.show()
