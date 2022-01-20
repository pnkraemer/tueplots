Files generated via (while in the root of tueplots; source https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
)
```commandline
sphinx-apidoc -o docs tueplots --separate --module-first
```
and then, in the conf.py, change the html theme from `alabaster` to `sphinx_rtd_theme`.


Build via:
```commandline
cd docs/; make clean; make html; cd ..
```
