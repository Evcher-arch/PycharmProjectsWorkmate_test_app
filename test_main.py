import pytest
import main

def test_invalid_argument_report(capsys):
    main.report_building(["stats1.csv"],"rep")
    captured = capsys.readouterr()
    assert "Неизвестный вид отчета: rep. Доступные отчеты: clickbait, " in captured.out

def test_unexisting_file(capsys):
    main.file_parser("stats4.csv")
    captured = capsys.readouterr()
    assert "Файл не найден: stats4.csv" in captured.out

def test_incorrect_csv(capsys):
    main.file_parser("stats3.csv")
    captured = capsys.readouterr()
    assert "Неверная структура файла данных: stats3.csv" in captured.out



