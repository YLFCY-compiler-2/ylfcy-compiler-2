#-*-coding:gbk-*-
import sys
import re
def coutconv(code_stream,j):
    cout_str='cout<<'
    if code_stream[len(code_stream)-1]=='��' or code_stream[len(code_stream)-1]=='��':
        raise ValueError('������н�β:'+code_stream[len(code_stream)-1]+'(λ�ڵ�'+str(j)+'�е�'+str(len(code_stream))+'���ַ�)')
    for i in range(3,len(code_stream)):
        if code_stream[i]=='��' and code_stream:
            cout_str+='<<'
    cout_str+=';'
    return cout_str
if __name__=="__main__":
    cpp_buffer=['//��YLFCY COMPILERת����','#include<iostream>','#include<cmath>','#include<ctime>','#include<string>','#include<cstring>','#include<algorithm>','#include<vector>','#include<queue>','using namespace std;']
    #ͷ�ļ��ͳ�ʼ��
    cpiurl="default_in.txt"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("���յ���"+cpiurl)
    with open (cpiurl,encoding='UTF8') as file_object:
        lines=file_object.readlines()#��ȡ�ļ�����
    code_string=''
    out_buffer=''#��ʼ��
    sum=0
    for line in lines:
        sum+=1
        code_string=line.rstrip()
        print(code_string)
        #����Ϊ�����ļ����ݲ�ת��ΪC++����
        if re.match("�����",code_string)!=None:
            out_buffer=coutconv(code_string,sum)
        cpp_buffer+=out_buffer    
    print("��ȡ�ɹ���")
    with open ('out.cpp','w',encoding='ANSI') as file_object2:
        for line in cpp_buffer:
            file_object2.write(line+'\n')#��ת���õĴ���д���ļ�
    print('д����ϣ�')
