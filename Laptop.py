class Laptop:
    keyboard = "English"

    def __init__(self, processor_speed_in_GHz=None, random_access_memory=None, producer_name=None,
                 video_card_name=None, display=None, price=None):
        self.processor_speed_in_GHz = processor_speed_in_GHz
        self.random_access_memory = random_access_memory
        self.producer_name = producer_name
        self.video_card_name = video_card_name
        self.display = display
        self.price = price

    def __str__(self):
        return "Processor speed: " + str(self.processor_speed_in_GHz) + " GHz" + "\n" + \
               "RAM: " + str(self.random_access_memory) + " Gb" + "\n" + \
               "Producer's name: " + str(self.producer_name) + "\n" + \
               "Video card: " + str(self.video_card_name) + "\n" + \
               "Display: " + str(self.display) + "\n" + \
               "Price: " + str(self.price) + " $" + "\n"

    @staticmethod
    def get_keyboard():
        return Laptop.keyboard

    def __del__(self):
        pass
