MODULE_NAME = "distance"
MODULE_AUTHOR = "Tomas Caram <tcaramm@gmail.com>"
MODULE_VERSION = 0.1


def _abs(x):
    return x if x > 0 else -x

def get_1d_distance(x1, x2):
    """
    @Label(get_1d_distance)
    @Description(Get distance between two points)
    @Parameters(float x1, float x2)
    @Example(-74.2, 110.3)
    @Color(#00ff00)
    @Return(float)
    """

    return _abs(x1-x2)