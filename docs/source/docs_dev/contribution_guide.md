# Contribution guide

Contributions from the community drive `tueplots`.
Are you thinking about contributing to `tueplots`?
If yes, that's fantastic!
To make it as easy as possible for you, follow the steps below.



## Is my contribution in scope?

`tueplots` welcomes all contributions that concern style-files of scientific papers.
Most obviously, new versions of existing style files (e.g., tueplots has `icml2023`, so `icml2025`, `icml2026`, or `icml2027` are in scope), but
new venues are also interesting (e.g., tueplots has ICML's style files, CVPR is also in scope).
For anything else, create an issue, and we will have a look together!


## How do I make a pull request on GitHub?
Making a pull request on GitHub can seem complicated if one is not used to doing that, but luckily, there are many guides:

- [Here](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) is GitHub's guide for contributing to open-source projects, including explanations of the terms "cloning" or "forking".
- [Here](https://docs.github.com/en/get-started/using-git) is information about working with `git`.
- And [here](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/) is how we can all write better commit messages.
- Using a virtual environment is generally a good idea when working with Python projects (such as `tueplots`). [Here](https://realpython.com/python-virtual-environments-a-primer/) are the basics. Be aware that if you place your environment inside the tueplots root folder, tueplots' auto-formatting might attempt to format the source code inside the environment, which is unnecessary.


A small project like tueplots might be the perfect place to start contributing to open-source projects.
If you would like to help but do not know where to start, reach out!

## Where do I put my code?

Once you've got the basic setup (forks, clones, git) going, it is time to write code.
Check out the [continuous-integration](https://tueplots.readthedocs.io/en/latest/docs_dev/continuous_integration) page for information about installing all dev-related tools.


Then, roughly follow these steps:

1. If you like to add a new style file, it would be ideal if you contributed four things: bundles, figsizes, fontsizes, and fonts. The remaining modules (axes, cycler, markers) are usually unimportant for adding a new style file.
2. Start by adding test cases to `tests/test_rc_params_cases/test_{fontsizes,figsizes,fonts,bundles}.py`. Take the existing cases as a reference. The next time you run `tox`, the tests will fail (which is expected).
3. Fix the failing tests by adding the corresponding functions to `tueplots/{fontsizes, figsizes, fonts, bundles}.py`. A good source for the concrete values of, e.g., the figsizes, are the author instructions that each conference/journal provides. Some values are easy to find; for others, you have to dig deeper. If you cannot find something, contribute what you can! Now, all tests should pass again.
4. A lot of this will be copying/pasting existing code. Remember to update the docstrings of the pasted code.
5. If you like, add a corresponding cell to one of the example notebooks. This step is optional, but sometimes it helps to see the configuration "in action".


Commit the results and open a pull request.
In the pull request's description, mention what you have contributed and where one can find the information. For example, write something like this:



    Title: Style-file for ICML2026

    Description: This PR adds the bundles, figsizes, fonts, and fontsizes for ICML 2026.

    Most values are the same as in previous years; see <link-to-call-for-papers> for reference.


Once this is done, we will process the pull request as quickly as we can.

Thank you for contributing to tueplots!
