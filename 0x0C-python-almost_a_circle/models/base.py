#!/usr/bin/python3

import json
import csv
import turtle

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id if id is not None else Base.increment_and_get_id()

    @classmethod
    def increment_and_get_id(cls):
        cls.__nb_objects += 1
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        new_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            fieldnames = cls.get_csv_fieldnames()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerows([obj.to_dictionary() for obj in list_objs] if list_objs else [])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = cls.get_csv_fieldnames()
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict((k, int(v)) for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_objects):
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        for obj in list_objects:
            turt.showturtle()
            turt.up()
            turt.goto(obj.x, obj.y)
            turt.down()
            for _ in range(2):
                turt.forward(obj.width)
                turt.left(90)
                turt.forward(obj.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

    @staticmethod
    def get_csv_fieldnames():
        return ["id", "width", "height", "x", "y"] if Base.__name__ == "Rectangle" else ["id", "size", "x", "y"]
