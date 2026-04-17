import argparse
import csv
from tabulate import tabulate

def getting_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", nargs='*', required=True)
    parser.add_argument("-r", "--report", required=True)
    args = parser.parse_args()
    return args

def main():
    args = getting_args()
    file_names = args.file
    report = args.report
    return report_building(file_names, report)

def report_building(file_names, report):
    joined_video_metadata = {}
    for file_name in file_names:
        joined_video_metadata = joined_video_metadata | file_parser(file_name)
    match report:
        case 'clickbait':
            table, headers = clickbate_report(joined_video_metadata)
        case _:
            print(f"Неизвестный вид отчета: {report}. Доступные отчеты: clickbait, ")
            return
    print(tabulate(table, headers, tablefmt="grid"))

def file_parser(file_name):
    video_metadata = {}
    try:
        with open(file_name, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in list(csv_reader)[1:]:
                meta_data = {}
                meta_data['ctr'] = line[1]
                meta_data['retention_rate'] = line[2]
                meta_data['views'] = line[3]
                meta_data['likes'] = line[4]
                meta_data['avg_watch_time'] = line[5]
                video_metadata[line[0]] = meta_data
    except FileNotFoundError:
        print(f"Файл не найден: {file_name}")
    except IndexError:
        print(f"Неверная структура файла данных: {file_name}")
    return video_metadata

def clickbate_report(metadata):
    table = []
    headers = ['title', 'ctr', 'retention_rate']
    for video in metadata:
         if float(metadata[video]['ctr']) > 15 and float(metadata[video]['retention_rate']) < 40:
             table.append([video, metadata[video]['ctr'], metadata[video]['retention_rate']])
    table.sort(key=lambda x: x[1], reverse=True)
    return table, headers


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
