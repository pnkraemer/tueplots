
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

## I am still getting 'overfull hbox' errors in my latex code

Even though the figsizes delivered by tueplots match the figure sizes in style files exactly,
sometimes, figures can be a few pt wider than what latex allows.
Visually, this does not make any difference,
but it might lead to 'overfull hbox' raised by, e.g., 'pdflatex'.
This is not tueplots fault, but likely due to the optimisation that matplotlib carries out
as part of constrained_layout=True or tight_layout=True.
Refer to the ![constrained layout documentation](https://matplotlib.org/stable/tutorials/intermediate/constrainedlayout_guide.html)
for more info.

**Solution:**
If you really cannot live with this warning, there are the following possible solutions:
* Instead of `\includegraphics(<plot>)`, use `\includegraphics[width=\textwidth](<plot>)`
  (to fix the final few pt -- the visual difference is zero).
* Set the `rel_width` in the figsizes to, e.g., `rel_width=0.97` and use `\includegraphics(<plot>)` as usual.


## My submission template requires Type 1 fonts

Type 1 fonts are a tricky requirements; for example, because
![Adobe will disable support for authoring with Type 1 fonts in January 2023](https://helpx.adobe.com/fonts/kb/postscript-type-1-fonts-end-of-support.html).
Matplotlib cannot do Type 1 fonts, but uses Type 3 fonts as a default.
There is also no way of making matplotlib use Type 1 fonts.
The only options are Type 3 fonts and Type 42 (/TrueType) fonts.

**Solution:**
If you _need_ Type 1 fonts, using TeX typesetting usually does the trick: E.g., via `bundles.icml2022(usetex=True)`,
or `fonts.icml2022_tex()`.
If the goal, however, is only to avoid type 3 fonts, adding
`plt.rcParams.update({"pdf.fonttype": 42})` to your plotting code will a PDF with `TrueType` fonts.
See ![this issue](https://github.com/pnkraemer/tueplots/issues/77) for more details.
