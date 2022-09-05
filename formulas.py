import math
import humanize as hmz
from humanize.i18n import _ngettext_noop as NS_

hmz.number.human_powers = (
    NS_("k", "k"),
    NS_("M", "M"),
    NS_("B", "B"),
    NS_("T", "T"),
    NS_("qd", "qd"),
    NS_("Qn", "Qn"),
    NS_("sx", "sx"),
    NS_("Sp", "Sp"),
    NS_("o", "o"),
    NS_("n", "n"),
    NS_("d", "d")  # if d - win
)


def point_occurrence(rxy: tuple | list, pxy: tuple | list):
    """

    :param rxy: ((pos of the top left), (pos of the bottom right)) of the rectangle.
    :param pxy: (x, y) of the point
    :return: bool
    """
    rtx, rty, rbx, rby, px, py = rxy[0][0], rxy[0][1], rxy[1][0], rxy[1][1], pxy[0], pxy[1]
    # print(f"{rtx=}", f"{rty=}", f"{rbx=}", f"{rby=}", f"{px=}", f"{py=}::::{(rtx < px < rbx) and (rty < py < rby)}")
    return rtx < px < rbx and rty < py < rby


def center(par_pos, par_size, child_size=None):
    px, py = par_pos
    pw, ph = par_size
    if child_size:
        cw, ch = child_size
        return px + pw / 2 - cw / 2, py + ph / 2 - ch / 2
    else:
        return px + pw / 2, py + ph / 2


def round_to_degree_of_two(n):
    return 2 ** round(math.log2(n))


def hmz_num(n):
    if n > 999:
        return hmz.intword(n, "%.0f").replace(" ", "")
    return str(n)
