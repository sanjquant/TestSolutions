from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Datum:
    id: int
    name: str
    year: int
    color: str
    pantone_value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        year = from_int(obj.get("year"))
        color = from_str(obj.get("color"))
        pantone_value = from_str(obj.get("pantone_value"))
        return Datum(id, name, year, color, pantone_value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["year"] = from_int(self.year)
        result["color"] = from_str(self.color)
        result["pantone_value"] = from_str(self.pantone_value)
        return result


@dataclass
class Support:
    url: str
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Support':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        text = from_str(obj.get("text"))
        return Support(url, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["text"] = from_str(self.text)
        return result


@dataclass
class Resources:
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Datum]
    support: Support

    @staticmethod
    def from_dict(obj: Any) -> 'Resources':
        assert isinstance(obj, dict)
        page = from_int(obj.get("page"))
        per_page = from_int(obj.get("per_page"))
        total = from_int(obj.get("total"))
        total_pages = from_int(obj.get("total_pages"))
        data = from_list(Datum.from_dict, obj.get("data"))
        support = Support.from_dict(obj.get("support"))
        return Resources(page, per_page, total, total_pages, data, support)

    def to_dict(self) -> dict:
        result: dict = {}
        result["page"] = from_int(self.page)
        result["per_page"] = from_int(self.per_page)
        result["total"] = from_int(self.total)
        result["total_pages"] = from_int(self.total_pages)
        result["data"] = from_list(lambda x: to_class(Datum, x), self.data)
        result["support"] = to_class(Support, self.support)
        return result


def resources_from_dict(s: Any) -> Resources:
    return Resources.from_dict(s)


def resources_to_dict(x: Resources) -> Any:
    return to_class(Resources, x)
