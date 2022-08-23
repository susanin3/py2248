def point_occurrence(rxy: tuple | list, pxy: tuple | list):
    """

    :param rxy: ((pos of the top left), (pos of the bottom right)) of the rectangle.
    :param pxy: (x, y) of the point
    :return: bool
    """
    rtx, rty, rbx, rby, px, py = rxy[0][0], rxy[0][1], rxy[1][0], rxy[1][1], pxy[0], pxy[1]
    print(f"{rtx=}", f"{rty=}", f"{rbx=}", f"{rby=}", f"{px=}", f"{py=}")
    return rtx < px < rbx and rty < py < rbx
