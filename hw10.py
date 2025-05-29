import os
import pickle

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    return sum(s) / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_scores(scores, filename="score.bin"):
    with open(filename, "wb") as f:
        pickle.dump(scores, f)

def load_scores(filename="score.bin"):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return None

def main():
    filename = "score.bin"
    scores = load_scores(filename)

    if scores is not None:
        print('[파일 읽기]')
    else:
        print('[점수 입력]')
        scores = input_scores()
        save_scores(scores, filename)

    print('\n[점수 출력]')
    print('개인점수: ', end='')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')

if __name__ == "__main__":
    main()
