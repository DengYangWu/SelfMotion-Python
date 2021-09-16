import subprocess

def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a '+host+' -p '+str(port)+' -bp '+str(bootstrap_port)
    print(cmd)
    subprocess.Popen(cmd, shell=True, stdout=open('../test_case/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    appium_start(host, port)