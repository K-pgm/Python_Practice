from car import Car


class Truck(Car):

    def __init__(self, model_name, mileage, manufacturer, max_load_capacity):
        super(Truck, self).__init__(model_name=model_name, mileage=mileage, manufacturer=manufacturer)
        self._max_load_capacity = max_load_capacity
        self._current_load_capacity = 0
        print("Truck init called!!")

    @property
    def max_load_capacity(self):
        # print("max_load_capacity getter called")
        return self._max_load_capacity

    @max_load_capacity.setter
    def max_load_capacity(self, max_load_capacity):
        # print("max_load_capacity setter called")
        self._max_load_capacity = max_load_capacity

    @property
    def current_load_capacity(self):
        # print("current_load_capacity getter called")
        return self._current_load_capacity

    @current_load_capacity.setter
    def current_load_capacity(self, current_load_capacity):
        # print("current_load_capacity setter called")
        self._current_load_capacity = current_load_capacity

    def gas(self):
        if self.current_load_capacity > self.max_load_capacity:
            print("重量オーバーです")
            print(f"最低でも{self.current_load_capacity - self.max_load_capacity}の荷物を降ろしてください")
        else:
            super().gas()

    def load(self, load):
        if load > 0:

            self.current_load_capacity += load
            print(f"{load}の荷物を積みました")
            if self.current_load_capacity > self.max_load_capacity:
                print(f"積載量を{abs(self.current_load_capacity - self.max_load_capacity)}オーバーしています")
        else:
            if self._current_load_capacity + load > 0:
                # 負の値なので加算する
                self.current_load_capacity += load
            else:
                print(f"すべての荷物を降ろしました")
                self.current_load_capacity = 0
        self.show_load_capacity()

    def show_load_capacity(self):
        print(f"現在の積載量: {self.current_load_capacity}")


dump_truck = Truck("Dump_truck", 50, "トヨタ", 1000)
dump_truck.load(300)
dump_truck.load(-5000)
dump_truck.load(7000)

dump_truck.gas()