def yaml_load():
    import yaml
    config = yaml.load(open('config.yaml'))

    RATE = config['RATE']
    TIME = config['TIME']
    FFT_size = config['FFT_size']
    Noise_gate = config['Noise_gate']
    low_lim = config['low_lim']
    hight_lim = config['hight_lim']


def visualizer():
    import matplotlib
    matplotlib.use("Qt5Agg")  # claim qt5 agg.
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg\
        as FigureCanvas
    from matplotlib.figure import Figure

    class Figure_Canvas(FigureCanvas):

        def __init__(self, parent=None, width=7, height=1.2, dpi=100):
            # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
            fig = Figure(figsize=(width, height), dpi=dpi)
            fig.set_tight_layout(True)

            FigureCanvas.__init__(self, fig)  # 初始化父类
            self.setParent(parent)

            # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
            self.axes = fig.add_subplot(111)

        def visulizer(self, x, y):
            self.axes.plot(x, y)


def stdout_load():
    import sys
    print('222')
    with open('temp.txt','w') as f:
        sys.stdout = f
        print('1111111')
        f.write()




if __name__ == '__main__':
    stdout_load()
