"""Font settings for conference papers and journals."""

def neurips(usetex=False):
    # <- don't use LaTeX to typeset. It's much slower, and you can't change the font atm.
    return {
        "text.usetex": usetex,
        "font.serif": ["Times New Roman"],
        "mathtext.fontset": "custom",
        "mathtext.rm": "Times New Roman",
        "mathtext.it": "Times New Roman:italic",
        "mathtext.bf": "Times New Roman:bold",  #####
    }


def icml():
    return {
        "font.serif": ["Times"],
        "mathtext.fontset": "stix",  # free ptmx replacement
    }
