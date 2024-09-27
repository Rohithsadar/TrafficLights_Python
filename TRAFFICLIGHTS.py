class TrafficLight:
    def __init__(self, signal_id, green_time=30, yellow_time=5, red_time=30):
        self.signal_id = signal_id
        self.green_time = green_time
        self.yellow_time = yellow_time
        self.red_time = red_time

    def __repr__(self):
        return f"TrafficLight({self.signal_id}, Green: {self.green_time}, Yellow: {self.yellow_time}, Red: {self.red_time})"
class TrafficLightSystem:
    def __init__(self):
        self.lights = {}

    def create_traffic_light(self, signal_id, green_time=30, yellow_time=5, red_time=30):
        if signal_id in self.lights:
            raise ValueError(f"Traffic light {signal_id} already exists.")
        self.lights[signal_id] = TrafficLight(signal_id, green_time, yellow_time, red_time)

    def read_traffic_light(self, signal_id):
        return self.lights.get(signal_id)

    def update_traffic_light(self, signal_id, green_time=None, yellow_time=None, red_time=None):
        light = self.lights.get(signal_id)
        if light is None:
            raise ValueError(f"Traffic light {signal_id} not found.")
        if green_time is not None:
            light.green_time = green_time
        if yellow_time is not None:
            light.yellow_time = yellow_time
        if red_time is not None:
            light.red_time = red_time

    def delete_traffic_light(self, signal_id):
        if signal_id not in self.lights:
            raise ValueError(f"Traffic light {signal_id} not found.")
        del self.lights[signal_id]

    def optimize_traffic_signals(self, signal_id):
        # Simple optimization logic: increase green light by 10% and decrease red light by 10%
        light = self.lights.get(signal_id)
        if light is None:
            raise ValueError(f"Traffic light {signal_id} not found.")
        light.green_time = int(light.green_time * 1.1)
        light.red_time = int(light.red_time * 0.9)

    def analyze_traffic_impact(self, signal_id):
        # Placeholder for analysis logic
        light = self.lights.get(signal_id)
        if light is None:
            raise ValueError(f"Traffic light {signal_id} not found.")
        return {
            "signal_id": light.signal_id,
            "green_time": light.green_time,
            "yellow_time": light.yellow_time,
            "red_time": light.red_time,
            "impact": "Optimized flow expected with adjusted timings."
        }
import unittest

class TestTrafficLightSystem(unittest.TestCase):
    def setUp(self):
        self.system = TrafficLightSystem()

    def test_create_traffic_light(self):
        self.system.create_traffic_light('TL1', 30, 5, 30)
        self.assertEqual(len(self.system.lights), 1)

    def test_read_traffic_light(self):
        self.system.create_traffic_light('TL1', 30, 5, 30)
        light = self.system.read_traffic_light('TL1')
        self.assertIsNotNone(light)
        self.assertEqual(light.green_time, 30)

    def test_update_traffic_light(self):
        self.system.create_traffic_light('TL1', 30, 5, 30)
        self.system.update_traffic_light('TL1', green_time=40)
        light = self.system.read_traffic_light('TL1')
        self.assertEqual(light.green_time, 40)

    def test_delete_traffic_light(self):
        self.system.create_traffic_light('TL1', 30, 5, 30)
        self.system.delete_traffic_light('TL1')
        self.assertIsNone(self.system.read_traffic_light('TL1'))

    def test_optimize_traffic_signals(self):
        self.system.create_traffic_light('TL1', 30, 5, 30)
        self.system.optimize_traffic_signals('TL1')
        light = self.system.read_traffic_light('TL1')
        self.assertEqual(light.green_time, 33)  # 30 * 1.1
        self.assertEqual(light.red_time, 27)    # 30 * 0.9

    def test_analyze_traffic_impact(self):
        self.system.create_traffic_light('TL1', 30, 5, 30)
        impact = self.system.analyze_traffic_impact('TL1')
        self.assertEqual(impact['signal_id'], 'TL1')
        self.assertEqual(impact['impact'], "Optimized flow expected with adjusted timings.")

if __name__ == '__main__':
    unittest.main()
