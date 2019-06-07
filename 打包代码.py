from os import system as sy
import os,time
def main():
    nowpath=os.getcwd()
    if sy('where python'):
        print(r'未搜索到pyhon,是否下载(y\n)')
        if input()=='y':
            sy(r'bitsadmin /transfer n https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe %s\python3.7.exe'%nowpath)
            delay=time.time()
            while not os.path.exists(r'%s\python3.7.exe'%nowpath):
                if time.time()-delay>15:
                    print('FailDownload...')
                    return
            sy(r'start %s\python3.7.exe'%nowpath)      
        return
    if sy('where pyinstaller'):
        sy(r'pip install pyinstaller')
        sy('cls')
        print('打包程序下载成功...')
    else:
        sy('cls')
    try:
        sy(r'md %s\pyinsss'%nowpath)
        while not os.path.exists(r'%s\pyinsss'%nowpath):
            pass
        c=[]
        for a,b,c in os.walk('.'):
            break
        ico=[i for i in c if i[-4:]=='.ico']
        c=[i for i in c if i[-3:]=='.py']
        print('选择打包文件编号:')
        for i in range(len(c)):
            print(str(i)+'. '+c[i])
        name=c[int(input())]
        if ico:
            print('选择文件图片编号:')
            print('0. 不设置图片')
            for i in range(len(ico)):
                print(str(i+1)+'. '+ico[i])
            i=int(input())
            if i==0:
                ico=''
            else:
                ico=r'-i '+r'%s\%s'%(nowpath,ico[i-1])
        else:
            print('当前目录无ico图片，1s后开始生成')
            ico=''
            time.sleep(1)
        addpack='-p '+input('附加包地址(多个则用分号隔开)(默认:无):')
        if addpack=='-p ':
            addpack=''
        sy(r'pyinstaller -F {0} {4} --specpath {1}{2} --workpath {1}{2} --distpath {1} {3}'.format(name,nowpath,r'\pyinsss',ico,addpack))
        delay=time.time()
        while not os.path.exists(r'%s\%s.exe'%(nowpath,name[:-3])):
            if time.time()-delay>15:
                print('Timeout Error...')
                break
        sy(r'rd/s/q %s\__pycache__'%nowpath)
        sy(r'rd/s/q %s\pyinsss'%nowpath)
        input('Finished...')
    except:
        print('\a')
        input('Error...')

if __name__=='__main__':
    main()
