'''
13.	从键盘输入一段英文，将其中的英文单词分离出来：已知单词之间的分隔符包括空格、   问号、句号(小数点)和分号。    例如：输入：There
are   apples;   oranges   and   peaches   on   the   table.    输出：there    are

  apples
  oranges
  and
  peaches
  on
  the
  table
  '''
import re

s = 'There  are   apples;   oranges   and   peaches   on   the   table.  '
print(re.split('[^a-zA-Z ]+', s.lower().strip()))
