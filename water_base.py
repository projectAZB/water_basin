class Solution:
    def trap(self, arr: List[int]) -> int:
        arr_len = len(arr)

        total_water = 0
        i = 0
        while i < arr_len - 1:
            i_val = arr[i]
            if i_val == 0:
                i += 1
                continue
            
            j = i + 1
            i_water = 0
            while j < arr_len:
                j_val = arr[j]
                if j_val < i_val:
                    if j == arr_len - 1:
                        sub_array = arr[i:j + 1]
                        sub_array.reverse()
                        total_water += self.trap(sub_array)
                        i = j
                        break
                    else:
                        i_water += (i_val - j_val)
                    j += 1
                elif j_val == i_val:
                    total_water += i_water
                    i = j
                    break
                elif j_val > i_val:
                    total_water += i_water
                    i = j
                    break
                else:
                    assert False

        return total_water
