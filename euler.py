def problem_0008():
    number = (
	'73167176531330624919225119674426574742355349194934'
	'96983520312774506326239578318016984801869478851843'
	'85861560789112949495459501737958331952853208805511'
	'12540698747158523863050715693290963295227443043557'
	'66896648950445244523161731856403098711121722383113'
	'62229893423380308135336276614282806444486645238749'
	'30358907296290491560440772390713810515859307960866'
	'70172427121883998797908792274921901699720888093776'
	'65727333001053367881220235421809751254540594752243'
	'52584907711670556013604839586446706324415722155397'
	'53697817977846174064955149290862569321978468622482'
	'83972241375657056057490261407972968652414535100474'
	'82166370484403199890008895243450658541227588666881'
	'16427171479924442928230863465674813919123162824586'
	'17866458359124566529476545682848912883142607690042'
	'24219022671055626321111109370544217506941658960408'
	'07198403850962455444362981230987879927244284909188'
	'84580156166097919133875499200524063689912560717606'
	'05886116467109405077541002256983155200055935729725'
	'71636269561882670428252483600823257530420752963450'
    )

    last_num = (None, 0)
    for i in range(0, 1000-12):
        current_str = number[i:i+13]
        product = reduce(lambda x, y: x*y, [int(num) for num in list(current_str)])

        if product > last_num[1]:
            last_num = (int(current_str), product)

    return last_num, number


def problem_0016():
    twos = [int(two) for two in list('2'*1000)]
    return reduce(lambda x, y: x + y, [int(num) for num in list(str(reduce(lambda x, y: x*y, twos)))])


def problem_0017():
    numbers = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
        9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
        40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
        100: 'hundred', 1000: 'one thousand'
    }
    def get_tens(num):
        if num < 20:
            return numbers[num]
        else:
            return numbers[num/10 * 10] + (' {0}'.format(numbers[num%10]) if num%10 else '')

    numbers_str = ''
    numbers_list = []
    for i in range(1, 1001):
        if i in numbers and i != 100:
            numbers_list.append(numbers[i])
        elif len(str(i)) == 3:
            numbers_str = '{0} {1}'.format(numbers[i/100], numbers[100])
            if  i % 100:
                numbers_str += ' and {0}'.format(get_tens(i - i/100*100))
            numbers_list.append(numbers_str)
        else:
            numbers_list.append(get_tens(i))

#    print numbers_list
    return len(''.join(numbers_list).replace(' ', ''))
