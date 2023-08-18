# functor

class Count:
    def __init__(self, init_steps):
        self.steps = init_steps

    def __call__(self, *args, **kwargs):
        inc, = args
        self.steps += inc

    def add_steps(self, steps):
        self.steps += steps
        return self.steps


if __name__ == '__main__':
    count_step = Count(100)
    count_step(25)
    count_step(50)
    print(count_step.steps)

    count_step.add_steps(25)
    count_step.add_steps(50)
    print(count_step.steps)
