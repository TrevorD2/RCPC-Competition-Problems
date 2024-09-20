def solution(points: list[list[int]]) -> int:
    num_squares = 0
    n = len(points)
    
    point_set = set()

    for x, y in points:
        point_set.add((x, y))

    def check_points(points):
        for point in points:
            if point not in point_set: return 0
        return 1
    

    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[j][0], points[j][1]

            dx, dy = abs(x1-x2), abs(y1-y2)

            if dx!=dy and dx!=0 and dy!=0: continue

            points_to_check = []

            if min(dx, dy) == 0: 
                side = max(dx, dy)
                if dx==0:
                    points_to_check.append((x1+side, y1))
                    points_to_check.append(x2+side, y2)
                else:
                    points_to_check.append((x1))

            else:
                if x1 < x2:
                    points_to_check.append((x1+dx, y1))
                else:
                    points_to_check.append((x2+dx, y2))
                
                if y1 < y2:
                    points_to_check.append(x1, y1+dy)
                else:
                    points_to_check.append((x2, y2+dy))

            num_squares+=check_points(points_to_check)

    return num_squares