def k_boom(start, end, k):
    def count_k_apear(n,k):
        return len([x for x in str(n) if int(x) == k])
    def chek_digit(dig,k):
        check_k = count_k_apear(dig,k)
        if  check_k > 0 and dig%k == 0:
            ret = "bada-boom!"
        else:
            if check_k > 0:
                ret = ("boom-" * check_k)[:-1] + "!"
            else:
                if dig%k == 0:
                    ret = "boom!"
                else:
                    ret = str(dig)
        return ret
    result = ""
    if type(k) == int and 0 < k < 10:
        for digit in range(start,end+1):
            result += chek_digit(digit,k) + " "
    return result[:-1]



