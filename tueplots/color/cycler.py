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
