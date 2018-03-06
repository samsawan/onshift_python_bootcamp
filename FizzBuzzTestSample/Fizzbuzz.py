class Fizzbuzz:

    def get_fizzbuzz_string(self,input_num):
        if input_num % 3 == 0 and input_num % 5 == 0:
            return "Fizzbuzz"
        elif input_num % 3 == 0:
            return "Fizz"
        elif input_num % 5 == 0:
            return "Buzz"
        else:
            return ""