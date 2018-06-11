class Screen(object):
    slots = ('width', 'height')

    def get_width(self):
        return self._width


    def set_width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be a integer!')
        if value < 0:
            raise ValueError('width must > 0 !')
        self._width = value


    def get_height(self):
        return self._height


    def set_height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be a integer!')
        if value < 0:
            raise ValueError('height must > 0 !')
        self._height = value


    def get_resolution(self):
        if not hasattr(self, 'width'):
            raise ValueError('has not width, not return relolution!')
        if not hasattr(self, 'height'):
            raise ValueError('has not height, not return relolution!')
        return self._width * self._height
    width = property(get_width, set_width)
    height = property(get_height, set_height)
    resolution = property(get_resolution)


# 测试:
s = Screen()
s.width = 0
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
