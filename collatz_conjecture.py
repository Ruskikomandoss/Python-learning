import matplotlib.pyplot as plt


def start_number() -> int:
    while True:
        number = input("Write a number from which we begin computing:\n")
        if number.isnumeric():
            return int(number)
        else:
            print("You were supposed to write a number.")
        

def counting_collatz(start_number: int) -> list:
    numbers = []
    if start_number == 1:
        return numbers.append(start_number)
    else:
        while start_number != 1:
            if start_number%2==0:
                start_number = start_number/2
                
            elif start_number%2 != 0:
                start_number = (3*start_number)+1
            numbers.append(start_number)
        return list(map(lambda x: int(x), numbers))
    

def collatz_stats(numbers_list: list) -> None:
    print(f"""
    There were {len(numbers_list)} operations in total until we reached 1.
    The number we started from was {numbers_list[0]}.
    The highest number we reached was {max(numbers_list)}
    
    The numbers in order of appearance: {numbers_list}

    """)


def collatz_visualization(numbers_list: list) -> None:
    plt.style.use('seaborn-v0_8-notebook')
    plt.plot(numbers_list, label='The sequential distribution of numbers of computed array', marker='.', linewidth=0.5)
    plt.legend()
    plt.title("Distribution of computed values")
    plt.xlabel("Number of steps performed in given computation")
    plt.ylabel("The value of the number")

    plt.tight_layout()
    plt.show()


def main():
    user_number = start_number()
    operation_list = counting_collatz(user_number)
    collatz_stats(operation_list)
    collatz_visualization(operation_list)


if __name__ == "__main__":
    main()
