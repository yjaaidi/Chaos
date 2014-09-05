from nose.tools import *
import chaos

# value exist
def test_get_date_time_valid():
    with chaos.app.app_context():
        chaos.utils.option_value(chaos.formats.pt_object_type_values)('line', 'name')


# value not exist
@raises(ValueError)
def test_get_date_time_valid():
    with chaos.app.app_context():
        chaos.utils.option_value(chaos.formats.pt_object_type_values)('lineline', 'name')
