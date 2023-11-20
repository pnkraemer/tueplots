# FAQ: Frequently asked questions

## My version of matplotlib cannot find font XYZ?!

Some fonts that `tueplot` provides (e.g., `Times` or `Roboto`) must be installed on your machine before matplotlib can find them.
This means that you need to find a `.ttf` file online (e.g., the `Roboto` family is available at Google fonts: [link-to-roboto](https://fonts.google.com/specimen/Roboto),
download it, and install it. For Ubuntu, this means opening the file (with your font manager) and clicking `install`.
There are probably many other ways to do this.
Once the font is installed, delete your matplotlib cache (usually: `rm ~/.cache/matplotlib -rf`) and restart your notebook (not just the kernel).
See also [this question on Stack Overflow](https://stackoverflow.com/questions/42097053/matplotlib-cannot-find-basic-fonts/42841531).

On a related note: if you want to use the Latex version of the fonts/bundles, your system must include the required tex packages.
See [this Stack Overflow discussion](https://stackoverflow.com/questions/55746749/latex-equations-do-not-render-in-google-colaboratory-when-using-matplotlib)
for information.
You may encounter this problem when using Tueplots in combination with a Google Colab notebook.



## My fonts are not displayed as expected  with `plt.rc_context()`

In our experience, changing fonts works more reliably with `plt.rcParams.update()` than with `plt.rc_context()`.
If someone knows why, please let us know. :)

## I am still getting 'overfull hbox' errors in my latex code

Even though the figure sizes delivered by Tueplots match the figure sizes in style files exactly, sometimes, figures can be a few points wider than what latex allows.
Visually, this does not make any difference,
but it might lead to an 'overfull hbox' raised by, e.g., 'pdflatex'.
This is not Tueplots' fault but likely due to the optimisation that matplotlib carries out
as part of constrained_layout=True or tight_layout=True.
Refer to the <a href=https://matplotlib.org/stable/tutorials/intermediate/constrainedlayout_guide.html>constrained layout documentation</a>
for more info.

**Solution:**
If you really cannot live with this warning, there are the following possible solutions:
* Instead of `\includegraphics(<plot>)`, use `\includegraphics[width=\textwidth](<plot>)`. This fixes the final few pixels, and the visual difference is non-existent.
* Set the `rel_width` in the figsizes to, e.g., `rel_width=0.97` and use `\includegraphics(<plot>)` as usual.


## My submission template requires Type 1 fonts

Type 1 fonts are a tricky requirement; for example, because
<a href=https://helpx.adobe.com/fonts/kb/postscript-type-1-fonts-end-of-support.html> Adobe will disable support for authoring with Type 1 fonts in January 2023 </a>.
Matplotlib cannot do Type 1 fonts but uses Type 3 as a default.
There is also no way of making matplotlib use Type 1 fonts.
The only options are Type 3 and Type 42 (/TrueType) fonts.

**Solution:**
If you _need_ a Type 1 font, using TeX typesetting usually does the trick: E.g., via `bundles.icml2022(usetex=True)`,
or `fonts.icml2022_tex()`.
If the goal, however, is only to avoid type 3 fonts, adding
`plt.rcParams.update({"pdf.fonttype": 42})` to your plotting code will create a PDF with `TrueType` fonts.
See <a href=https://github.com/pnkraemer/tueplots/issues/77>this issue</a> for more details.
