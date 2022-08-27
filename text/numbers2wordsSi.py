one_digit = {
        '0': ["බිංදුව"],
        '1': ["එක","", "" ,"එක" , "එක්" ],
        '2': ["දෙක", "විසි" ,"දෙ" ,"දෙ" , "දෙ"],
        '3': ["තුන", "තිස්", "තුන්", "තුන්", "තුන්"],
        '4': ["හතර", "හතලිස්" , "හාර","හාර", "හාර"],
        '5': ["පහ", "පනස්" , "පන්", "පන්", "පන්"],
        '6': ["හය","හැට" ,"හය", "හය", "හය"],
        '7': ["හත","හැත්තෑ" , "හත්" , "හත්", "හත්"],
        '8': ["අට","අසූ", "අට" , "අට", "අට"],
        '9': ["නවය","අනූ" ,"නව" , "නව", "නව"],
    }
two_digit = {
    "20" : "විස්ස" ,
    "30" : "තිහ" ,
    "40" : "හතලිහ" ,
    "50" : "පනහ" ,
    "60" : "හැට" ,
    "70" : "හැත්තෑව" ,
    "80" : "අසූව" ,
    "90" : "අනූව"
}
teen_numbers = {
    "10": ["දහය"],
    "11": ["එකොලහ", "එකලොස්"],
    "12": ["දොලහ" ,"දොලොස්" ],
    "13": ["දහතුන","දහතුන්"],
    "14": ["දාහතර","දාහතර"],
    "15": ["පහලොව","පහලොස්"],
    "16": ["දාසය","දාසය"],
    "17": ["දාහත","දාහත්"],
    "18": ["දහඅට","දහඅට"],
    "19": ["දහනවය" ,"දහනව"]
}
large_sum_words = ["දහස්", "මිලියන", "බිලියන", "ට්‍රිලියන"]


def converter(n):
  word = []

  if n.startswith('-'):
    word.append("ඍණ")
    n = n[1:]

  if len(n) % 3 != 0 and len(n) > 3:
        n = n.zfill(3 * (((len(n)-1) // 3) + 1))

  sum_list = [n[i:i + 3] for i in range(0, len(n), 3)]
  skip = False

  last = len(sum_list) - 1
  
  for i, num in enumerate(sum_list):
    if num != '000': 
      skip = False
    for _ in range(len(num)):
      num = num.lstrip('0')
      if len(num) == 1:
        if i != last:
          word.append(one_digit[num][4])
          num = num[1:]
        else:
          word.append(one_digit[num][0])
          num = num[1:]
        break

      if len(num) == 2:
        if num[0] != '0':
          if num.startswith('1'):
            if i != last:
              number = teen_numbers[num][1]             
              word.append(number)
            else:
              number = teen_numbers[num][0]             
              word.append(number)

          else:
            if (num[1] != '0') and (i != last):
               word.append(one_digit[num[0]][1] +" "+ one_digit[num[1]][2])
            elif (i == last) and (num[1] != '0'):
              word.append(one_digit[num[0]][1] +" "+ one_digit[num[1]][0])
            elif (num[1] == '0') and (i == last):
              word.append(two_digit[num])
            else:
              word.append(one_digit[num[0]][1])
          break
        else:
            num = num[1:]
            continue

      if len(num) == 3:
        if num[1:] == '00':
          word.append(one_digit[num[0]][2]+"සීය")
          break
        if num[0] != '0':
          word.append(one_digit[num[0]][3]+"සිය")
        num = num[1:]

    if len(sum_list[i:]) > 1 and not skip:
      word.append(large_sum_words[len(sum_list[i:]) - 2])
      skip = True
    if len(sum_list[i:]) > 1 and sum_list[-1] == '000':
      word.append("දාහ")
      skip = True

  word = " ".join(map(str.strip, word))
  return word