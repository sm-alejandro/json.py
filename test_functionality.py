import unittest
import json
import bulkjson


class TestFunctions(unittest.TestCase):
    def load_data(self, path):
        with open(path, 'r') as start_file:
            data = json.load(start_file)
        return data

    def test_add(self):
        start_data = self.load_data('./data/example.json')
        add_data = self.load_data('./data/after_adding.json')
        temp = bulkjson.add(data=start_data, loc=None,
                            key="timestamp", val=None, rec=False)
        result_data = bulkjson.add(
            data=temp, loc="wind", key="direction", val='0', rec=False)
        assert result_data == add_data

    def test_delete(self):
        start_data = self.load_data('./data/example.json')
        delete_data = self.load_data('./data/after_deleting.json')

        temp = bulkjson.delete(
            data=start_data, loc=None, key="speed", rec=False)
        assert temp == start_data

        result_data = bulkjson.delete(
            data=temp, loc="wind", key="speed", rec=False)
        assert result_data == delete_data

    def test_replace(self):
        start_data = self.load_data('./data/example.json')
        replace_data = self.load_data('./data/after_replacing.json')

        temp = bulkjson.replace(data=start_data, loc=None, key={'wind': 'temperature'}, rec=True)
        result_data = bulkjson.replace(data=temp, loc='rain', key={'speed': 'quantity'}, rec=True)
        assert result_data == replace_data


if __name__ == "__main__":
    unittest.main()
