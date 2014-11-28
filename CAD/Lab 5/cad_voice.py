# -*- coding: cp1251 -*- 
import pyttsx

# ����� ������
Alena = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\Infovox Desktop v2.2\Alyona22k"

engine = pyttsx.init() # ������� ��������� � ����������� ��������� (����������� �� 'sapi5')

# ��������� ������
rate = engine.getProperty('rate') # �������� �������� ���������������
engine.setProperty('rate', rate - 20) # ������� ������, ���������
engine.setProperty('voice', Alena) # ���������� ����� �����

stop = False 
while stop == False: # ������ �� ���������� �������
    choose = (raw_input("���� �� �����(F)/�������(C): ")).decode('cp1251')
    if choose == 'F': # ���� ������� ���������� � �����
        text = open('input.txt', 'r+').readlines() # ��������� ��������� � ����
        for line in text: # ��������� �������������
            engine.say(line.decode('cp1251'))
        engine.runAndWait()
        stop = True
    elif choose == 'C': # ���� ������� ���������� � �������
        text = (raw_input("������� ������:  ")).decode('cp1251')
        engine.say(text) # ������������� ���������� � ������� �����
        engine.runAndWait()
        stop = True
        

