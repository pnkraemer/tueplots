"""Font settings for conference papers and journals."""

def neurips(*, usetex=False):
    return {
        "text.usetex": usetex,
        "font.serif": ["Times New Roman"],
        "mathtext.fontset": "custom",
        "mathtext.rm": "Times New Roman",
        "mathtext.it": "Times New Roman:italic",
        "mathtext.bf": "Times New Roman:bold",  #####
    }


def icml(*, usetex=False):
    return {
        "text.usetex": usetex,
        "font.serif": ["Times"],
        "mathtext.fontset": "stix",  # free ptmx replacement
    }
