#-*-coding:gbk-*-
import sys
import re
def coutconv(code_stream,j):
    cout_str='cout<<'
    if code_stream[len(code_stream)-1]=='��' or code_stream[len(code_stream)-1]=='��' or code_stream[len(code_stream)-1]=='��':
        raise ValueError('������н�β:'+code_stream[len(code_stream)-1]+'(λ�ڵ�'+str(j)+'�е�'+str(len(code_stream))+'���ַ�)')
    if len(code_stream)<3:
        raise NameError("�����������Ҫ����һ������(λ�ڵ�"+str(j)+"��)")
    i=2
    while i<len(code_stream):
        #print(code_stream[i])
        if code_stream[i]=='��':
            cout_str+='"'
        elif code_stream[i]=='��':
            cout_str+='"'
        elif code_stream[i]=='��' and code_stream[i+1]=='��':
            cout_str+='endl'
            i+=1
        elif code_stream[i]=='��':
            cout_str+='<<'
        else:
            cout_str+=code_stream[i]
        i+=1
    cout_str+=';'
    return cout_str
if __name__=="__main__":
    cpp_buffer=['//��YLFCY COMPILERת����','#include<iostream>','#include<cmath>','#include<ctime>','#include<string>','#include<cstring>','#include<algorithm>','#include<vector>','#include<queue>','using namespace std;','int main(){']
    #ͷ�ļ��ͳ�ʼ��
    cpiurl="default_in.txt"
    if len(sys.argv)>1:
        cpiurl=sys.argv[1]
    print("���յ���"+cpiurl)
    with open (cpiurl,encoding='UTF8') as file_object:
        lines=file_object.readlines()#��ȡ�ļ�����
    code_string=''
    out_buffer=''#��ʼ��
    summ=0
    flag=False
    for line in lines:
        flag=True
        summ+=1
        code_string=line.rstrip()
        print(code_string)
        #����Ϊ�����ļ����ݲ�ת��ΪC++����
        if len(code_string)==0:
            pass
        elif re.match("���",code_string)!=None:
            out_buffer=coutconv(code_string,summ)
        else:
            raise SyntaxError("δָ֪��(��"+str(summ)+"��)")
        if flag:
            cpp_buffer.append(str(out_buffer))
    cpp_buffer.append('return 0;}')
    print("��ȡ�ɹ���")
    with open ('out.cpp','w',encoding='ANSI') as file_object2:
        for line in cpp_buffer:
            file_object2.write(line+'\n')#��ת���õĴ���д���ļ�
    print('д����ϣ�')
    print(cpp_buffer)
