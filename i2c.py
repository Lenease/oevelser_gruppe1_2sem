import schedule
import time
import pigpio


class LightScheduler:
    def __init__(self, GPIO_pin):
        self.duty = 0
        self.GPIO_pin = GPIO_pin
        self.pi = pigpio.pi()
        self.pi.set_PWM_range(self.GPIO_pin, 100)
        self.init_schedule()

    def init_schedule(self):
        # Increase brightness: :01, :02, :03, :04 each minute
        schedule.every().minute.at(":01").do(self.bright_increase)
        schedule.every().minute.at(":02").do(self.bright_increase)
        schedule.every().minute.at(":03").do(self.bright_increase)
        schedule.every().minute.at(":04").do(self.bright_increase)

        # Decrease brightness: :05, :06, :07, :08 each minute
        schedule.every().minute.at(":05").do(self.bright_decrease)
        schedule.every().minute.at(":06").do(self.bright_decrease)
        schedule.every().minute.at(":07").do(self.bright_decrease)
        schedule.every().minute.at(":08").do(self.bright_decrease)

    def bright_increase(self):
        if self.duty < 100:
            self.duty += 10
            self.pi.set_PWM_dutycycle(self.GPIO_pin, self.duty)
            print(f"Increasing brightness: {self.duty}%")
        else:
            print("Brightness already at maximum.")

    def bright_decrease(self):
        if self.duty > 0:
            self.duty -= 10
            self.pi.set_PWM_dutycycle(self.GPIO_pin, self.duty)
            print(f"Decreasing brightness: {self.duty}%")
        else:
            print("Brightness already at minimum.")


if __name__ == "__main__":
    lamp = LightScheduler(13)
    while True:
        schedule.run_pending()
        time.sleep(1)
