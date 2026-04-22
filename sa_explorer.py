fimport tkinter as tk
from tkinter import ttk
import math

CANVAS_W, CANVAS_H = 500, 450
OBLIQUE_ANGLE = math.radians(45)
OBLIQUE_SCALE = 0.4  # fraction of full scale for depth axis

def surface_area_to_volume_ratio(width, height, length):
    surface_area = 2 * ((width * height) + (width * length) + (height * length))
    volume = width * height * length
    return surface_area / volume

def proj(x, y, z, cx, cy, scale):
    """Oblique cabinet projection. x=length, y=width(depth), z=height."""
    sx = cx + x * scale + y * scale * OBLIQUE_SCALE * math.cos(OBLIQUE_ANGLE)
    sy = cy - z * scale - y * scale * OBLIQUE_SCALE * math.sin(OBLIQUE_ANGLE)
    return sx, sy


def draw_box(l, w, h):
    canvas.delete("all")
    max_dim = max(l, w, h, 1)
    scale = 130 / max_dim

    # Center the box on the canvas
    cx = CANVAS_W / 2 - (l / 2) * scale - (w / 2) * scale * OBLIQUE_SCALE * math.cos(OBLIQUE_ANGLE)
    cy = CANVAS_H / 2 + (h / 2) * scale + (w / 2) * scale * OBLIQUE_SCALE * math.sin(OBLIQUE_ANGLE)

    def p(x, y, z):
        return proj(x, y, z, cx, cy, scale)

    # 8 corners: (x=length, y=width/depth, z=height)
    # Front face (y=0): 0=front-bottom-left, 1=front-bottom-right, 4=front-top-left, 5=front-top-right
    # Back face (y=w): 2=back-bottom-right, 3=back-bottom-left, 6=back-top-right, 7=back-top-left
    corners = [
        (0, 0, 0), (l, 0, 0), (l, w, 0), (0, w, 0),  # bottom: 0 1 2 3
        (0, 0, h), (l, 0, h), (l, w, h), (0, w, h),  # top:    4 5 6 7
    ]
    pts = [p(*c) for c in corners]

    # Hidden edges (back-left corner at vertex 3): dashed gray
    hidden_edges = [(0, 3), (3, 2), (3, 7)]
    for i, j in hidden_edges:
        canvas.create_line(*pts[i], *pts[j], fill="#bbb", width=1, dash=(5, 3))

    # Visible edges
    visible_edges = [
        (0, 1), (1, 2), (2, 6),  # bottom front, bottom right, right back vertical
        (4, 5), (5, 6), (6, 7), (7, 4),  # top face
        (0, 4), (1, 5), (2, 6),          # front verticals + back-right vertical (already have 2-6)
        (4, 7),                           # top left back
    ]
    # Deduplicate
    drawn = set()
    all_visible = [
        (0, 1), (1, 2), (2, 6), (6, 7), (7, 4), (4, 5), (5, 6),
        (0, 4), (1, 5), (4, 7),
    ]
    for i, j in all_visible:
        key = (min(i, j), max(i, j))
        if key not in drawn:
            drawn.add(key)
            canvas.create_line(*pts[i], *pts[j], fill="#222", width=2)

    # ---- Dimension labels ----
    # Length label: midpoint of front bottom edge (0→1)
    mx = (pts[0][0] + pts[1][0]) / 2
    my = (pts[0][1] + pts[1][1]) / 2
    canvas.create_text(mx, my + 16, text=f"L = {l}", font=("Arial", 10, "bold"), fill="#c00")

    # Width label: midpoint of right bottom depth edge (1→2)
    mx = (pts[1][0] + pts[2][0]) / 2
    my = (pts[1][1] + pts[2][1]) / 2
    canvas.create_text(mx + 32, my, text=f"W = {w}", font=("Arial", 10, "bold"), fill="#007700")

    # Height label: midpoint of front-left vertical edge (0→4)
    mx = (pts[0][0] + pts[4][0]) / 2
    my = (pts[0][1] + pts[4][1]) / 2
    canvas.create_text(mx - 32, my, text=f"H = {h}", font=("Arial", 10, "bold"), fill="#0000cc")


def calculate(*args):
    try:
        l = int(float(l_var.get()))
        w = int(float(w_var.get()))
        h = int(float(h_var.get()))
    except (ValueError, tk.TclError):
        return
    if l <= 0 or w <= 0 or h <= 0:
        return

    sa = 2 * (l * w + l * h + w * h)
    vol = l * w * h
    ratio = surface_area_to_volume_ratio(w, h, l)

    sa_label.config(text=f"Surface Area:   {sa} units²")
    vol_label.config(text=f"Volume:          {vol} units³")
    ratio_label.config(text=f"SA : Vol  =  {ratio:.4f}")

    draw_box(l, w, h)


# ---- Window setup ----
root = tk.Tk()
root.title("Cell Surface Area to Volume Ratio")
root.resizable(False, False)

# ---- Left control panel ----
left = ttk.Frame(root, padding=15)
left.pack(side=tk.LEFT, fill=tk.Y)

ttk.Label(left, text="Rectangular Solid", font=("Arial", 12, "bold")).pack(pady=(0, 12))

l_var = tk.StringVar(value="5")
w_var = tk.StringVar(value="5")
h_var = tk.StringVar(value="5")

dim_colors = {"Length (L)": "#cc0000", "Width (W)": "#007700", "Height (H)": "#0000cc"}
dim_vars   = {"Length (L)": l_var,     "Width (W)": w_var,     "Height (H)": h_var}

for label_text, var in dim_vars.items():
    row = ttk.Frame(left)
    row.pack(fill=tk.X, pady=5)
    ttk.Label(row, text=label_text, width=12,
              foreground=dim_colors[label_text]).pack(side=tk.LEFT)
    sb = ttk.Spinbox(row, from_=1, to=50, textvariable=var,
                     width=6, command=calculate)
    sb.pack(side=tk.LEFT, padx=(4, 0))
    var.trace_add("write", calculate)

ttk.Separator(left, orient="horizontal").pack(fill=tk.X, pady=14)

sa_label    = ttk.Label(left, text="", font=("Courier", 10))
vol_label   = ttk.Label(left, text="", font=("Courier", 10))
ratio_label = ttk.Label(left, text="", font=("Courier", 11, "bold"))

for lbl in (sa_label, vol_label, ratio_label):
    lbl.pack(anchor=tk.W, pady=2)

# ---- Canvas ----
canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white",
                   highlightthickness=1, highlightbackground="#ccc")
canvas.pack(side=tk.RIGHT, padx=(0, 10), pady=10)

calculate()
root.mainloop()
