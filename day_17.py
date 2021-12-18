X_RANGE = [201, 230]
Y_RANGE = [65, 99]


class Bullet:
    LIMIT_MIN_X = 0
    LIMIT_MAX_X = 50000
    LIMIT_MIN_Y = -50000
    LIMIT_MAX_Y = 100

    def __init__(self, direction):
        self.x = 0
        self.y = 0
        self.v_x = direction[0]
        self.v_y = direction[1]

        self.start_direction = direction

        self.max_y = 0

        self.success = False

        self.trail = [(self.x,self.y)]

    def next_frame(self):
        self.x += self.v_x
        self.y += self.v_y

        if self.y < self.max_y:
            self.max_y = self.y

        self.trail.append((self.x,self.y))

        if self.v_x > 0:
            self.v_x -= 1
        self.v_y += 1

    def within_constraints(self):
        return in_hit_box(self.x, self.y, [Bullet.LIMIT_MIN_X, Bullet.LIMIT_MAX_X], [Bullet.LIMIT_MIN_Y, Bullet.LIMIT_MAX_Y])

    def solve_trail(self, x_int, y_int):
        while self.within_constraints():
            self.next_frame()
            if self.in_hit_box(x_int, y_int):
                self.success = True

    def in_hit_box(self, x_int, y_int):
        return in_hit_box(self.x, self.y, x_int, y_int)


def in_hit_box(x, y, x_int, y_int):
    return not(x < x_int[0] or x > x_int[1] or y < y_int[0] or y > y_int[1])

def plot_trail(bullet):
    string = ''
    for y in range(Bullet.LIMIT_MIN_Y, Bullet.LIMIT_MAX_Y + 1):
        for x in range(Bullet.LIMIT_MIN_X, Bullet.LIMIT_MAX_X + 1):
            if (x,y) in bullet.trail:
                string += 'o'
            elif in_hit_box(x, y, X_RANGE, Y_RANGE):
                string += '#'
            else:
                string += ' '


        string += '\n'

    print(string)


if __name__ == "__main__":

    succesfull_runs = []
    most_succesfull_run = Bullet((0, 0))

    for i in range(500):
        for j in range(-500, 500):
            bullet = Bullet((i, j))
            bullet.solve_trail(X_RANGE, Y_RANGE)

            if bullet.success:
                succesfull_runs.append(bullet)

                if bullet.max_y < most_succesfull_run.max_y:
                    most_succesfull_run = bullet

    print(len(succesfull_runs))
    if len(succesfull_runs) > 0:
        # plot_trail(most_succesfull_run)
        print(most_succesfull_run.max_y)
        print(most_succesfull_run.start_direction)
