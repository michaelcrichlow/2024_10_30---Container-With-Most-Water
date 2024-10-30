class Solution:
    def maxArea(self, height: List[int]) -> int:
        # def maxArea(height: list[int]) -> int:

        # function to use later
        def evaluate_best_area(l: list[int]) -> int:

            max_area = 0
            l_ptr, r_ptr = 0, len(l) - 1
            while l_ptr != r_ptr:
                length = abs(r_ptr - l_ptr)
                width = min([l[l_ptr], l[r_ptr]])
                return_max_area = length * width
                if return_max_area > max_area:
                    max_area = return_max_area

                if l[l_ptr] < l[r_ptr]:
                    l_ptr += 1
                else:
                    r_ptr -= 1

            return max_area

        # initialize variables
        max_value = 0
        max_value = evaluate_best_area(height)
        # print("max_value: ", max_value)

        return max_value
