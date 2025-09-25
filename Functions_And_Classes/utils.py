class Utility:
    def print_logs(self, message):
        print(f"{message}")
    
    def convert_string_to_lower(self, message):
        result = message.lower()
        self.print_logs(result)
    
    def convert_string_to_upper(self, message):
        result = message.upper()
        self.print_logs(result)

    def get_second_highest_number(self, nums: list[int]) -> int | None: 
        highest_number = float('-inf')
        second_highest_number = float('-inf')
        for num in nums:
            if num > highest_number:
                second_highest_number = highest_number
                highest_number = num
            elif num > second_highest_number and num != highest_number:
                second_highest_number = num
        return second_highest_number if second_highest_number != float('-inf') else None
    
    def sort_list(self, nums: list[int]) -> list[int]:
        nums.sort()
        self.print_logs(nums)
        return nums

    def find_num_with_max_freq(self, nums: list[int]) -> tuple[int, int]:
        d = dict()
        for num in nums:
            if num in d:
                d[num] = d[num] + 1
            else:
                d[num] = 1

        max_num = None
        max_freq = 0
        for key, value in d.items():
            if max_freq < value:
                max_freq = value
                max_num = key
        self.print_logs(f"num : {max_num}, freq : {max_freq}")
        return max_num, max_freq
        
'''
utility = Utility()
utility.convert_string_to_lower("Testing")
utility.convert_string_to_upper("Testing")
utility.find_num_with_max_freq([1,2,4,6,3,4,3,2,3,4,5,3,2,4,3,3,3,31])
result = utility.get_second_highest_number([1,2,4,6,3,4,3,2,3,4,5,3,2,4,3,3,6,31,31,31])
print(f"second highest number => {result}")
utility.sort_list([32,4,45,23,45,6,23,56,23,246,23,235,56,3])
'''