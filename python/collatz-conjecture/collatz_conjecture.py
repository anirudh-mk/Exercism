def steps(number):
    def steps_recursive(num, count=0):
        if num <= 0:
            raise ValueError("Only positive integers are allowed")

        if num == 1:
            return count

        if num % 2 == 0:
            return steps_recursive(num/2, count + 1)
        else:
            return steps_recursive(num*3 + 1, count + 1)

    return steps_recursive(number)