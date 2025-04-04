from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


def linear(files):
    start_time = datetime.now()
    for file in files:
        read_info(file)
    end_time = datetime.now()
    elapsed = end_time - start_time
    print(f'Время линейных выполнений: {elapsed}')


def parallel(files):
    start_time = datetime.now()
    with Pool() as pool:
        pool.map(read_info, files)
    end_time = datetime.now()
    elapsed = end_time - start_time
    print(f'Время параллельных выполнений: {elapsed}')


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    linear(filenames)
    parallel(filenames)
