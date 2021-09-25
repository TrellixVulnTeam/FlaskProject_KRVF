import pytest
import json
from repository.db_connector import DBConnector


def test_save(monkeypatch):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    db_connector = DBConnector()
    result_save = db_connector.save(id_test, object_to_save)
    assert result_save


def test_get_by_id():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    db_connector = DBConnector()
    db_connector.save(id_test, object_to_save)
    result = db_connector.get_by_id(id_test)
    assert result == object_to_save


