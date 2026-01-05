from prb2_reverse_number import reverse

number = 1221
is_palindrome = True if number == reverse(number) else False

print("%d number --> palindrome result is %s" % (number,is_palindrome))