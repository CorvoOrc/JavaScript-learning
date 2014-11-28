from pymorphy import get_morph # ��������� ����������� ������
from pymorphy.contrib import tokenizers

morph = get_morph('C:/Python27/ru.sqlite-json/') # ������� ������ ������ pymorphy.Morph

text = (raw_input("������� ������():  ")).decode('cp1251')
print "�������� ������():",
for word in tokenizers.extract_tokens(text): # �������� ������, ������ ����� ����
    if word.isalpha() == True: # ��������� ����������
        info = morph.get_graminfo(word.upper())
        print str('{0}({1})').format(word.encode('cp1251'), info[0]['class'].encode('cp1251')),
    elif word.isspace() == False: # ������� ������ print, �� �� �������
        print word,
        
while True:
    q = (raw_input("\n\n�������� �����������?Y/N: "))
    if q == 'Y':
        print '�  - ���������������'
        print '�  - ��������������'
        print '�� - �����������'
        print '�  - ������ � ������ �����'
        print '�  - �������'
        print '���������    - ���������'
        print '������������ - ������������'
        print '���������    - ���������'
        print '��-�����     - ����������� ����������'
        print '��-�   - ����������� ��������������'
        print '����   - ������������(��������������)'
        print '����-� - ���������� ������������'
        print '�����  - ����������'
        print '�����  - �������'
        print '����   - ����'
        print '����   - ����������'
        print '����   - �������'
        print '�����  - ������� �����'
        print '��_����- ������� ��������������'
        print '��_��������� - ������� ���������'
        print '���� - ���������'
        break
    elif q != 'N':
        print '������������ ����',
    else:
        break

# ������������ ������ �3, �������� �.�.
