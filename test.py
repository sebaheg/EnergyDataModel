import typing as t
from pint import UnitRegistry
from dataclasses import dataclass

u = UnitRegistry()
Watt = t.Annotated[float, u.Quantity, u.watt]

def check_quantity_dimensionality_unit(attribute, type):
  if not isinstance(attribute, type.__metadata__[0]):
    raise TypeError('The type should be '+str(type.__metadata__[0]))
  if not attribute.dimensionality == type.__metadata__[1].dimensionality:
    raise TypeError('The dimensionality should be '+str(type.__metadata__[1].dimensionality))



@dataclass
class Location:
  longitude: float
  latitude: float

@dataclass
class PVSystem:
  system_id: str
  capacity: t.Union[Watt, t.List[Watt]]
  location: t.Optional[Location] = None
  installation_date: t.Optional[str] = None

  def __post_init__(self):
      check_quantity_dimensionality_unit(self.capacity, Watt)

loc = Location(1, 1)
print(loc)

pv = PVSystem('sd', 23*u.megawatt)
print(pv)
print(pv.capacity)
#print(pv.to_dict())
