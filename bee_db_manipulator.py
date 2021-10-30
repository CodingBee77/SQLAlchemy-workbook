from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bee_db_create_table import Bee
from typing import List


class DbManipulator:
    def __init__(self, session):
        self.session = session

    def add_one(self, name: str, size: int, bee_type: str)-> None:
        """
        Add one record to the database.

        Args:
            name (str): Bee name
            size (int): Bee size
            bee_type (str): Bee type
        """
        bee = Bee(name=name, size=size, bee_type=bee_type)
        session.add(bee)
        session.commit()
        print(f"Record added successfully")


    def add_multiple(self, bee_list: List[dict])-> None:
        """
        Add multiple records to the database.

        Args:
            bee_list (List[dict]): List of multiple records mapped to a dictionary.
        """
        bee_obj_list = []
        for bee in bee_list:
            bee_obj = Bee(name=bee["name"], size=bee["size"], bee_type=bee["bee_type"])
            bee_obj_list.append(bee_obj)

        session.add_all(bee_obj_list)
        session.commit()
        print(f"Records added successfully")


    def show_bee_detail(self, bee)-> None:
        """
        Print model with it's attributes.

        Args:
            bee ([type]): bee object
        """
        print(f"Name: {bee.name}, size: {bee.size}, bee type: {bee.bee_type}")


    def get_all_data(self)-> None:
        """
        Get all data from the database.
        """
        bees = session.query(Bee)
        print("All bees in a hive:")
        for bee in bees:
            self.show_bee_detail(bee)


    def get_all_order_by(self, order_attribute)-> None:
        """
        Get all records ordered by specific an attribute.

        Args:
            order_attribute ([type]): 'model.attribute'
        """
        bees = session.query(Bee).order_by(order_attribute)
        print(f"All bees in a hive ordered by {order_attribute}")
        for bee in bees:
            self.show_bee_detail(bee)


    def get_filtered_data(self, condition)-> None:
        """
        Get records filtered by specific condition.

        Args:
            condition: condition statement
        """
        bees = session.query(Bee).filter(condition)
        print(f"Bees in a hive filtered by {condition}")
        for bee in bees:
            self.show_bee_detail(bee)

    def get_count_data(self, condition)-> None:
        """
        Count number of records filtered by specific condition.

        Args:
            condition:  condition statement
        """
        bee_count = session.query(Bee).filter(condition).count()
        print(f"Bees in a hive filtered by {condition}: \n {bee_count}")


    def update_bee_name(self, condition, update_name: str)-> None:
        """
        Update filtered record with a defined name.

        Args:
            condition:  condition statement
            update_name (str): new name
        """
        bee = session.query(Bee).filter(condition).first()
        bee.name = update_name
        self.session.commit()
        print(f"Record updated successfully")
    

    def delete_bee(self, condition)-> None:
        """
        Delete filtered record.

        Args:
            condition:  condition statement
        """
        bee = session.query(Bee).filter(condition).first()
        self.session.delete(bee)
        self.session.commit()
        print("Record deleted successfully")


if __name__ == "__main__":
    engine = create_engine('postgresql://codingbee:bee123@localhost:5432/alchemy', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    db_manipulator = DbManipulator(session)
    # db_manipulator.add_one("Lilianne",6, "U9")
    db_manipulator.get_filtered_data(Bee.size==4)
    # db_manipulator.get_filtered_data(or_(Bee.size==4, Bee.size==7))
    # db_manipulator.get_count_data(Bee.bee_type=="T7")
    # db_manipulator.update_bee_name(Bee.bee_type=="C1", "Jack")
    # db_manipulator.delete_bee(Bee.bee_type=="U9")