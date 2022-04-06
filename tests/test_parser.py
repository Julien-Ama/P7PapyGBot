# coding: utf-8
from app import Parser


def test_parser_remove_all_accent():
    question = "Hé salùt touê, commé tu vè ?"
    parser = Parser(question)
    assert parser.question == "he salut toue ve"

def test_remove_ponctuation():
    question = "Hé salut, comment, tu vas ??!!??"
    parser = Parser(question)
    assert parser.question == "he salut"

def test_remove_uppercase():
    question = "HE SALUT COMMENT TU VAS"
    parser = Parser(question)
    assert parser.question == "he salut"


def test_all_parser():
    question = "Quelle est là capitale de la France ?"
    parser = Parser(question)
    assert parser.question == "capitale france"