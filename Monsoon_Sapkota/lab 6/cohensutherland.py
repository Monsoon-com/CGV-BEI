import matplotlib.pyplot as plt

# -------- REGION CODES --------
INSIDE = 0
LEFT   = 1
RIGHT  = 2
BOTTOM = 4
TOP    = 8


# -------- COMPUTE REGION CODE --------
def compute_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code


# -------- COHEN–SUTHERLAND ALGORITHM --------
def cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    code0 = compute_code(x0, y0, xmin, ymin, xmax, ymax)
    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)

    while True:
        # Both points inside
        if code0 == 0 and code1 == 0:
            return x0, y0, x1, y1

        # Line completely outside
        if code0 & code1:
            return None

        # Select outside point
        outcode = code0 if code0 else code1

        if outcode & TOP:
            x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
            y = ymax
        elif outcode & BOTTOM:
            x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
            y = ymin
        elif outcode & RIGHT:
            y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
            x = xmax
        elif outcode & LEFT:
            y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
            x = xmin

        if outcode == code0:
            x0, y0 = x, y
            code0 = compute_code(x0, y0, xmin, ymin, xmax, ymax)
        else:
            x1, y1 = x, y
            code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)


# -------- MAIN --------
if __name__ == "__main__":
    # Line endpoints
    x0, y0 = 2, 2
    x1, y1 = 10, 6

    # Clipping window
    xmin, ymin = 4, 1
    xmax, ymax = 8, 5

    # Plot setup
    plt.figure(figsize=(6, 6))

    # Draw clipping window
    plt.plot(
        [xmin, xmax, xmax, xmin, xmin],
        [ymin, ymin, ymax, ymax, ymin],
        'k-', linewidth=2, label="Clipping Window"
    )

    # Draw original line
    plt.plot([x0, x1], [y0, y1], 'r--', label="Original Line")

    # Clip and draw result
    clipped = cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
    if clipped:
        cx0, cy0, cx1, cy1 = clipped
        plt.plot([cx0, cx1], [cy0, cy1], 'g-', linewidth=3, label="Clipped Line")

    plt.xlim(0, 12)
    plt.ylim(0, 8)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.legend()
    plt.title("Cohen–Sutherland Line Clipping Algorithm")
    plt.show()
