import unittest

from netengine import get_version, __version__
from netengine.backends import BaseBackend, Dummy
from netengine.exceptions import NetEngineError


__all__ = ['TestBaseBackend']


class TestBaseBackend(unittest.TestCase):
    
    def test_netengine_exception(self):
        with self.assertRaises(NetEngineError):
            raise NetEngineError('test')
    
    def test_version(self):
        get_version()
        __version__
    
    def test_dummy_backend(self):
        dummy = Dummy('10.40.0.1')
        self.assertIn('Dummy NetEngine', str(dummy))
    
    def test_base_backend(self):
        device = BaseBackend()
        
        self.assertTrue(device.__netengine__)
        
        with self.assertRaises(NotImplementedError):
            device.validate()
        
        with self.assertRaises(NotImplementedError):
            str(device)
        
        with self.assertRaises(NotImplementedError):
            device.__repr__()
        
        with self.assertRaises(NotImplementedError):
            device.__unicode__()
        
        with self.assertRaises(NotImplementedError):
            device.os
        
        with self.assertRaises(NotImplementedError):
            device.name
        
        with self.assertRaises(NotImplementedError):
            device.model
        
        with self.assertRaises(NotImplementedError):
            device.RAM_total
        
        with self.assertRaises(NotImplementedError):
            device.uptime
        
        with self.assertRaises(NotImplementedError):
            device.uptime_tuple
        
        with self.assertRaises(NotImplementedError):
            device.ethernet_standard
        
        with self.assertRaises(NotImplementedError):
            device.ethernet_duplex
        
        with self.assertRaises(NotImplementedError):
            device.wireless_channel_width
        
        with self.assertRaises(NotImplementedError):
            device.wireless_mode
        
        with self.assertRaises(NotImplementedError):
            device.wireless_channel
        
        with self.assertRaises(NotImplementedError):
            device.wireless_output_power
        
        with self.assertRaises(NotImplementedError):
            device.wireless_dbm
        
        with self.assertRaises(NotImplementedError):
            device.wireless_noise
        
        with self.assertRaises(NotImplementedError):
            device.olsr