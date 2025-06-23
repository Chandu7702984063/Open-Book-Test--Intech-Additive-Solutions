def is_intersecting(r1, r2):
    return not (
        r1['x2'] < r2['x1'] or r1['x1'] > r2['x2'] or
        r1['y2'] < r2['y1'] or r1['y1'] > r2['y2']
    )

# Test
rect1 = {'x1': 0, 'y1': 0, 'x2': 4, 'y2': 4}
rect2 = {'x1': 2, 'y1': 2, 'x2': 6, 'y2': 6}
print(is_intersecting(rect1, rect2))  # True
