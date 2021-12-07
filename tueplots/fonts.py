"""Font settings for conference papers and journals."""


def neurips(*, usetex=False):
    return {
        "text.usetex": usetex,
        "font.serif": ["Times New Roman"],
        "mathtext.fontset": "custom",
        "mathtext.rm": "Times New Roman",
        "mathtext.it": "Times New Roman:italic",
        "mathtext.bf": "Times New Roman:bold",
    }


def icml(*, usetex=False):
    return {
        "text.usetex": usetex,
        "font.serif": ["Times"],
        "mathtext.fontset": "stix",  # free ptmx replacement
    }


def beamer(* usetex=False): # for use with the MoML beamer template
    return {
        "font.serif": ["Roboto Condensed"],
        "font.family": "serif",
        "text.color": TUdark,
        "axes.edgecolor": TUdark,
        "axes.labelcolor": TUdark,
        "xtick.color": TUdark,
        "ytick.color": TUdark,
    }

def beamer_dark_bg(* usetex=False):   # colors for dark beamer slides
    return {
        "font.serif": ["Roboto Condensed"],
        "font.family": "serif",
        "text.color": 'w',
        "axes.edgecolor": 'w',
        "axes.labelcolor": 'w',
        "xtick.color": 'w',
        "ytick.color": 'w',
    }
