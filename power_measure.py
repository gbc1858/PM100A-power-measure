import pyvisa as visa
from ThorlabsPM100 import ThorlabsPM100
import sqlite3
import time


class DBConnection:
    Insert_Power_Value = """
    insert into powerdata (value, group_id)
    values
    (?, ?);
    """
    Read_Group_Id = """
    select max(group_id) from powerdata;
    """

    def __init__(self):
        self.conn = sqlite3.connect('pd.db', isolation_level=None)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def get_group_id(self):
        self.cursor.execute(self.Read_Group_Id)
        group_id_tuple = self.cursor.fetchone()
        return group_id_tuple[0] if group_id_tuple[0] is not None else 0

    def save_power_value(self, power_value, group_id):
        self.cursor.execute(self.Insert_Power_Value, (power_value, group_id))


def read_machine(duration: int, step_size: int):
    # setup the hardware
    rm = visa.ResourceManager()
    inst = rm.open_resource('USB0::0x1313::0x8079::P1004274::INSTR')
    pm100a = ThorlabsPM100(inst=inst)
    pm100a.configure.scalar.power()

    # Adjust the measurement wavelength.
    pm100a.sense.correction.wavelength = 232

    # init DB
    dbc = DBConnection()
    new_group_id = dbc.get_group_id() + 1

    for step in range(0, duration, step_size):
        read_value = pm100a.read
        print(read_value)
        dbc.save_power_value(read_value, new_group_id)
        time.sleep(step_size)


def main():
    print('Enter the desired running time in seconds:')
    duration = input('>> ')

    print('Enter the step size in second:')
    step_size = input('>> ')

    try:
        read_machine(int(duration), int(step_size))
    except ValueError:
        print("Total time and time step need to be integer.")


if __name__ == '__main__':
    main()
