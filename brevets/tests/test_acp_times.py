"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
import collections
import sys

# python 3.10 moves collections.Callable to collections.abc.Callable, 
# this fixes the issue. So it can be tested properly
if sys.version_info.minor >= 10:
    collections.Callable = collections.abc.Callable

import nose     # Testing framework
from unittest import TestCase
import logging
import arrow

import acp_times

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


class TestOpen(TestCase):
    def test_open_times(self):
        """
        basic tests to verify open_time() is functioning properly.
        """

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(0, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T00:00')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(200,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T05:53')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(400,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T12:08')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(600,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T18:48')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(1000,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-02T09:05')


    def test_complex_open_times(self):
        """
        Harder Tests to verify open_time() is functioning properly
        """
        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(50, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T01:28')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(250, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T07:27')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(500, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T15:28')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(750, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-02T00:09')
        
        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.open_time(900, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-02T05:31')

class TestClose(TestCase):
    def test_close_times(self):
        """
        Basic tests to verify close_time() is functioning properly
        """

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(0,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T01:00')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(200,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T13:20')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(400,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-02T02:40')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(600,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-02T16:00')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(1000,1000,test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-04T03:00')


    def test_complex_close_times(self):
        """
        Harder tests to verify close_time() is functioning properly
        """

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(50, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T03:30')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(250, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-01T16:40')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(500, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-02T09:20')

        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(750, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-03T05:08')
        
        test_arrow = arrow.get('2000-01-01T00:00', 'YYYY-MM-DDTHH:mm')

        self.assertEqual(acp_times.close_time(900, 1000, test_arrow).format('YYYY-MM-DDTHH:mm'), '2000-01-03T18:15')
