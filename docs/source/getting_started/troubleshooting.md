
# Troubleshooting

## My version of matplotlib cannot find font XYZ?!

Some of the fonts that `tueplot` provides (e.g., `Times` or `Roboto`) needs to be installed on your machine before matplotlib can find it.
This means that you need to find a `.ttf` file online (e.g., `Roboto` family is available at Google fonts: https://fonts.google.com/specimen/Roboto),
download it, and install it. For Ubuntu, this means opening the file (with your font manager) and clicking `install`.
There are probably many other ways to do this.
Once the font is installed, delete your matplotlib cache (usually: `rm ~/.cache/matplotlib -rf`) and restart your notebook (not just the kernel).
See also https://stackoverflow.com/questions/42097053/matplotlib-cannot-find-basic-fonts/42841531.

## My fonts are not displayed as expected  with `plt.rc_context()`

In our experience, changing fonts works more reliably with `plt.rcParams.update()` than with `plt.rc_context()`.
If someone knows why, please let us know. :)
