# FAQ: Frequently asked questions

## My version of matplotlib cannot find font XYZ

Some fonts that Tueplots uses (e.g., `Times` or `Roboto`) must be installed on your machine before matplotlib can find them.
This installation means that you need to find a `.ttf` file online (e.g., the `Roboto` family is available at Google fonts: [link-to-roboto](https://fonts.google.com/specimen/Roboto),
download it, and install it. For Ubuntu, this means opening the file (with your font manager) and clicking `install`.
There are many other ways to do this, for example, one way would be to install Microsoft's TrueType Core fonts (known as `mscorefonts`).
Once a set of fonts has been installed, delete your matplotlib cache (usually: `rm ~/.cache/matplotlib -rf`) and restart your notebook (not just the kernel).
See also [this question on Stack Overflow](https://stackoverflow.com/questions/42097053/matplotlib-cannot-find-basic-fonts/42841531).

On a related note: if you want to use the Latex version of the fonts/bundles, your system must include the required tex packages.
Typically, this means installing either `texlive-fonts-extra` or `texlive-fonts-recommended`.
See [this Stack Overflow discussion](https://stackoverflow.com/questions/55746749/latex-equations-do-not-render-in-google-colaboratory-when-using-matplotlib)
for information.
Some users have encountered this Latex compatibility problem when using Tueplots with a Google Colab notebook.

If font compatibility is an issue, one workaround would be to set matplotlib up that it uses only a set of 14 core fonts; [here](https://matplotlib.org/stable/users/explain/text/fonts.html#core-fonts) is a link to the matplotlib documentation.


## My fonts are not displayed as expected  with `plt.rc_context()`

In our experience, changing fonts works more reliably with `plt.rcParams.update()` than with `plt.rc_context()`.
If someone knows why, please let us know. :)

## I am still getting 'overfull hbox' errors in my latex code

Even though the figure sizes delivered by Tueplots match the figure sizes in style files as closely as possible,
sometimes, figures can be a few points wider than what latex allows.
Visually, this does not make any difference, but it might lead to an 'overfull hbox' raised by, e.g., 'pdflatex'.
This overfull hbox is not Tueplots' fault but more due to how matplotlib draws figures:
- The figure dimensions are optimised differently, depending on whether a user selects constrained_layout=True or tight_layout=True (or neither).
  Refer to the <a href=https://matplotlib.org/stable/tutorials/intermediate/constrainedlayout_guide.html>constrained layout documentation</a> for more info.

- Sometimes, rounding errors in the division by dpi or an ignored linewidth may lead to marginally inaccurate figure sizes.
  See [Issue #129](https://github.com/pnkraemer/tueplots/issues/129) for context and more explanation.


**Solution:**
If you want to avoid this warning by any means, here are some solutions:
* Instead of `\includegraphics(<plot>)`, use `\includegraphics[width=\textwidth](<plot>)`. This argument fixes the final few pixels; the visual difference is non-existent.
* Set the `rel_width` in the figsizes to, e.g., `rel_width=0.97` and use `\includegraphics(<plot>)` as usual.
* Set the `savefig.bbox` argument to `tight`, as in:
```python
with mpl.rc_context({'savefig.bbox': 'standard'}):
    plt.savefig("figure.pdf")
```
and again, see [Issue #129](https://github.com/pnkraemer/tueplots/issues/129) for more info.


## My submission template requires Type 1 fonts

Type 1 fonts are a tricky requirement; for example, because
<a href=https://helpx.adobe.com/fonts/kb/postscript-type-1-fonts-end-of-support.html> Adobe will turn off support for authoring with Type 1 fonts in January 2023 </a>.
Matplotlib cannot do Type 1 fonts but uses Type 3 as a default.
There is also no way of making matplotlib use Type 1 fonts.
The only options are Type 3 and Type 42 (/TrueType) fonts.

**Solution:**
If you _need_ a Type 1 font, using TeX typesetting usually does the trick: E.g., via `bundles.icml2022(usetex=True)`,
or `fonts.icml2022_tex()`.
If the goal, however, is only to avoid type 3 fonts, adding
`plt.rcParams.update({"pdf.fonttype": 42})` to your plotting code will create a PDF with `TrueType` fonts.
See <a href=https://github.com/pnkraemer/tueplots/issues/77>this issue</a> for more details.


## Setting the figure size of a 3d plot cuts off labels

This problem has been raised in [Issue #143](https://github.com/pnkraemer/tueplots/issues/143).
It's a known problem in matplotlib [for example, see this issue](https://github.com/matplotlib/matplotlib/issues/19519), and tight/constrained layouts are no help.

For now, and according to [this stackoverflow discussion](https://stackoverflow.com/questions/77577613/matplotlib-3d-plot-z-label-cut-off), one possible fix is to "zoom out" by running
```python
...
ax.set_box_aspect(None, zoom=0.85)
```
before `plt.show()` or `plt.savefig(...)`. This solution might require adjusting some whitespaces manually.
