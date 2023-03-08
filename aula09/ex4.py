import bisect


def main():

    with open("wordlist.txt")as f:
        lst=[]
        for line in f:
            lst.append(line.strip())
            ea=bisect.bisect_left(lst)
            eb=bisect.bisect_left
            
