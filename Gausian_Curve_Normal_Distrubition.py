import matplotlib.pyplot as plot
import random


skewness = 0 # change value in range of "-1.0 - 1.0" to effect
kurtosis = 1 # change value in range of "0.0 - positive infinity" to effect


x_axis_length = 100
x_axis_min = 0
x_axis_max = 100


# t ranges between 0.0 - 1.0
def get_normalized_unmodified_gausian_value(t:float) -> float:
    v = 1.0 - (1.0 - ((float(abs(0.5 - t)) - 0.5)/0.5)**2)**2
    return v

# t ranges between 0.0 - 1.0
# skewness ranges between -1.0 - 1.0
# krutosis ranges between 0.0 - positive infinity
def get_normalized_modified_gausian_value(t:float, skewness:float, kurtosis:float) -> float:
    skewness = min(1.0, max(-1.0, skewness))
    t = min(1.0, max(0.0, t - skewness * 0.5))
    v = 1.0 - (1.0 - ((float(abs(0.5 - t)) - 0.5)/0.5)**2)**2
    kurtosis = max(0.0, kurtosis)
    v = v**kurtosis
    return v


def get_normalized_unmodified_gausian_random() -> float:
    t = random.uniform(0.0, 1.0)
    return get_normalized_unmodified_gausian_value(t)

def get_normalized_modified_gausian_random(skewness:float, kurtosis:float) -> float:
    t = random.uniform(0.0, 1.0)
    return get_normalized_modified_gausian_value(t, skewness, kurtosis)


def draw_graph() -> None:
    x_axis_range = x_axis_max - x_axis_min
    x_axis = []
    y_axis = []
    for i in range(x_axis_length):
        t = float(i) / float(x_axis_length)
        x = x_axis_min + x_axis_range * t
        x_axis.append(x)
        y = get_normalized_modified_gausian_value(t, skewness, kurtosis)
        y_axis.append(y)
    plot.plot(x_axis, y_axis, color="g")
    plot.show()


while(True):
    draw_graph()
