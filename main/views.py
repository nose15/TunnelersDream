from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
# Create your views here.


def home(response):
    if response.method == "POST":
        get_first_point = forms.GetFirstPoint(response.POST)
        if get_first_point.is_valid():
            x = get_first_point.cleaned_data["x"]
            z = get_first_point.cleaned_data["z"]
            x_margin = get_first_point.cleaned_data["x_margin"]
            z_margin = get_first_point.cleaned_data["z_margin"]
        get_second_point = forms.GetSecondPoint(response.POST)
        if get_second_point.is_valid():
            x1 = get_second_point.cleaned_data["x1"]
            z1 = get_second_point.cleaned_data["z1"]
            x_margin1 = get_second_point.cleaned_data["x_margin"]
            z_margin1 = get_second_point.cleaned_data["z_margin"]
        string = str(int(x)) + "^" + str(int(z)) + "^" + str(x_margin) + "^" + str(z_margin) + "^" + str(int(x1)) + "^" + str(int(z1)) + "^" + str(x_margin1) + "^" + str(z_margin1)
        return HttpResponseRedirect(f'/{string}/')
    else:
        get_first_point = forms.GetFirstPoint()
        get_second_point = forms.GetSecondPoint()
    return render(response, 'main/home.html', {"inputfirst": get_first_point, "inputsecond": get_second_point})


def tunnel(response, x, z, x_margin, z_margin, x_margin1, z_margin1, x1, z1):
    x = int(x)
    z = int(z)
    x1 = int(x1)
    z1 = int(z1)
    x_margin = int(x_margin)
    z_margin = int(z_margin)
    x_margin1 = int(x_margin1)
    z_margin1 = int(z_margin1)

    xs = []
    ys = []
    x1s = []
    y1s = []

    for x in range(x - x_margin, x + x_margin):
        xs.append(x)
    for y in range(z - z_margin, z + z_margin):
        ys.append(y)
    for x1 in range(x1 - x_margin1, x1 + x_margin1):
        x1s.append(x1)
    for y1 in range(z1 - z_margin1, z1 + z_margin1):
        y1s.append(y1)

    points1 = []
    points2 = []

    for element in xs:
        for i in range(len(ys)):
            point = []
            point.append(element)
            point.append(ys[i])
            points1.append(point)

    for element in x1s:
        for i in range(len(y1s)):
            point = []
            point.append(element)
            point.append(y1s[i])
            points2.append(point)

    points_pairs = []

    for point in points1:
        for i in range(len(points2)):
            points_pair = []
            points_pair.append(point)
            points_pair.append(points2[i])
            points_pairs.append(points_pair)

    min = 100
    lowest_a = 10
    best_fit = []
    best_index = 0
    for points_pair in points_pairs:
        _x = points_pair[0][0]
        _y = points_pair[0][1]
        _x1 = points_pair[1][0]
        _y1 = points_pair[1][1]
        if _x1 != _x:
            a = (_y1 - _y) / (_x1 - _x)
        else:
            a = 1.00
        list_a = list(str(a))
        if len(list_a) < min and a < lowest_a:
            min = len(list_a)
            lowest_a = a
            best_fit = points_pair
    if best_fit[1][1] == best_fit[0][1] or best_fit[1][0] == best_fit[0][0]:
        straight = True
        if best_fit[1][1] == best_fit[0][1]:
            if best_fit[1][0] > best_fit[0][0]:
                direction = "west"
            else:
                direction = "east"
        elif best_fit[1][0] == best_fit[0][0]:
            if best_fit[1][1] > best_fit[0][1]:
                direction = "south"
            else:
                direction = "north"
        string = "From ( x =" + str(best_fit[0][0]) + "; z =" + str(best_fit[0][1]) + ") Dig straight facing " + direction + " until you get to the ( x =" + str(
            best_fit[1][0]) + "; z =" + str(best_fit[1][1]) + ")"
        return render(response, 'main/tunnel.html', {"straight": straight, "string": string})

    else:
        straight = False
        if best_fit[1][1] > best_fit[0][1]:
            direction_z = "south"
        else:
            direction_z = "north"

        if best_fit[1][0] > best_fit[0][0]:
            direction_x = "east"
        else:
            direction_x = "west"

        a_direction = lowest_a
        dir_blocks1 = abs(lowest_a * 10)
        dir_blocks2 = abs(10)

        while dir_blocks1 != int(dir_blocks1):
            dir_blocks1 = dir_blocks1 * 10
            dir_blocks2 = dir_blocks2 * 10

        if a_direction > 1:
            common_divider = 1
            for x in range(2, 6):
                if dir_blocks1 // x == dir_blocks1 / x and dir_blocks2 // x == dir_blocks2 / x:
                    common_divider = x
            dir_blocks_1 = dir_blocks1 / common_divider
            dir_blocks_2 = dir_blocks2 / common_divider
            first_dir = direction_z
            second_dir = direction_x
            if first_dir == "north":
                first_dir_reverse = "south"
            else:
                first_dir_reverse = "north"
            if second_dir == "east":
                second_dir_reverse = "west"
            else:
                second_dir_reverse = "east"
        else:
            common_divider = 1
            for x in range(2, 6):
                if dir_blocks1 // x == dir_blocks1 / x and dir_blocks2 // x == dir_blocks2 / x:
                    common_divider = x
            dir_blocks_1 = dir_blocks1 / common_divider
            dir_blocks_2 = dir_blocks2 / common_divider
            first_dir = direction_x
            second_dir = direction_z
            if second_dir == "north":
                second_dir_reverse = "south"
            else:
                second_dir_reverse = "north"
            if first_dir == "east":
                first_dir_reverse = "west"
            else:
                first_dir_reverse = "east"
        string = str(lowest_a) + "Points: A( x =" + str(best_fit[0][0]) + "; y =" + str(best_fit[0][1]) + ") B( x =" + str(best_fit[1][0]) + "; y =" + str(best_fit[1][1]) + ")"
        point1 = "(x = " + str(best_fit[0][0]) + "; z = " + str(best_fit[0][1]) + ")"
        point2 = "(x = " + str(best_fit[1][0]) + "; z = " + str(best_fit[1][1]) + ")"
        return render(response, 'main/tunnel.html', {"straight": straight, "string": string, "firstdir": first_dir, "seconddir": second_dir, "dir_blocks_1": dir_blocks_1, "dir_blocks_2": dir_blocks_2, "point1": point1, "point2": point2, "firstdir_reverse": first_dir_reverse, "seconddir_reverse": second_dir_reverse})


def poll(response):
    return HttpResponse('polls')


def credits(response):
    return HttpResponse('Credits')

