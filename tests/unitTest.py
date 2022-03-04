#!/usr/bin/env python
import unittest
import sys
sys.path.insert(1, '/app/src')
import app


class TestService(unittest.TestCase):
  def setUp(self):
    app.app.testing = True
    self.app = app.app.test_client()

  def test_get_key(self):
    rv = self.app.get('/get/key')
    self.assertEqual(rv.status, '200 OK')

  def test_getall(self):
    rv = self.app.get('/getall')
    self.assertEqual(rv.status, '200 OK')

  def test_set(self):
    rv = self.app.post("/set", data={"content": "hello world"})
    self.assertEqual(rv.status, '200 OK')

  def test_search_prefix(self):
    rv = self.app.get('/search?prefix=test')
    self.assertEqual(rv.status, '200 OK')

  def test_search_suffix(self):
    rv = self.app.get('/search?suffix=test')
    self.assertEqual(rv.status, '200 OK')

  def test_health(self):
    rv = self.app.get('/health')
    self.assertEqual(rv.status, '200 OK')
    self.assertEqual(rv.data, b'OK')

if __name__ == '__main__':
  unittest.main()
