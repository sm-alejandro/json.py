import add_field
import delete_field
import replace_field


def add(data: dict, loc: str, key: str, val, rec: bool):
    return add_field.add(data=data, loc=loc, key=key, val=val, rec=rec)


def delete(data: dict, loc: str, key: str, rec: bool):
    return delete_field.delete(data=data, loc=loc, key=key, rec=rec)


def replace(data: dict, loc: str, key: dict, rec: bool):
    return replace_field.replace(data=data, loc=loc, key=key, rec=True)
