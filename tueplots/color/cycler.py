from matplotlib import cycler


def bright():
    """From Paul Tot's website: https://personal.sron.nl/~pault/."""
    color_cycler = cycler(
        "color", ["4477AA", "EE6677", "228833", "CCBB44", "66CCEE", "AA3377", "BBBBBB"]
    )
    return {"axes.prop_cycle": color_cycler}

def high_contrast():
    """From Paul Tot's website: https://personal.sron.nl/~pault/."""
    color_cycler = cycler('color', ['004488', 'DDAA33', 'BB5566'])
    return {"axes.prop_cycle": color_cycler}

def probnum():
    """ProbNum's colors: www.probabilistic-numerics.org"""
    color_cycler = cycler('color', ['107D79', 'FF9933', 'slateblue', 'lightcoral', '9467BD', '8C564B', 'E377C2', '7F7F7F', 'BCBD22', '17BECF'])
    return {"axes.prop_cycle": color_cycler}


def muted():
    """Muted color scheme. Color-blind safe.

    From Paul Tot's website: https://personal.sron.nl/~pault/
    """
    color_cycler =cycler('color', ['CC6677', '332288', 'DDCC77', '117733', '88CCEE', '882255', '44AA99', '999933', 'AA4499', 'DDDDDD'])
    return {"axes.prop_cycle": color_cycler}

