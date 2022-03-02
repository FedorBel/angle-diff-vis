def lerp(a: float, b: float, t: float) -> float:
    return a + t * (b - a)


def invLerp(from_: float, to: float, value: float) -> float:
    return (value - from_) / (to - from_)


def remap(orig_from: float, orig_to: float, target_from: float, target_to: float, value: float) -> float:
    rel = invLerp(orig_from, orig_to, value)
    return lerp(target_from, target_to, rel)
