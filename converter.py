#-*-coding:gbk-*-
import sys
if __name__=="__main__":
    cpp_buffer=['//��YLFCY COMPILERת����','#include<iostream>','#include<cmath>','#include<ctime>','#include<string>','#include<cstring>','#include<algorithm>','#include<vector>','#include<queue>','using namespace std;']
    #ͷ�ļ��ͳ�ʼ��
    cpiurl="default_in.txt"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("���յ���"+cpiurl)
    with open (cpiurl,encoding='UTF8') as file_object:
        lines=file_object.readlines()#��ȡ�ļ�����
    code_string=''#��ʼ��
    for line in lines:
        code_string=line.rstrip()
        print(code_string)
        #����Ϊ�����ļ����ݲ�ת��ΪC++����
        
    print("��ȡ�ɹ���")
    with open ('out.cpp','w',encoding='ANSI') as file_object2:
        for line in cpp_buffer:
            file_object2.write(line+'\n')#��ת���õĴ���д���ļ�
    print('д����ϣ�')
