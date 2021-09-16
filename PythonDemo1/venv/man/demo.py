from config import driver

threads = driver.threads
if __name__ == '__main__':
    for t in driver.threads:
        #print(t.getName())
        t.start()