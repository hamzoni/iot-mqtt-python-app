from fastapi import APIRouter, Depends

from api.signal.models.pin_model import Pin
from services.container import ServiceContainer, DatabaseContainer
from services.signal.pin_registry_service import PinRegistryService

router = APIRouter()

services = ServiceContainer.container()
db = DatabaseContainer.container()


@router.get('')
def list_all(
        collection=Depends(db.get_pin_collection),
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return service.list_all(collection)


@router.post('')
def add(
        pin: Pin,
        collection=Depends(db.get_pin_collection),
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return {
        'result': service.add(collection, pin)
    }


@router.delete('/{board_name}/{pin_name}')
def remove(
        board_name: str, pin_name: str,
        collection=Depends(db.get_pin_collection),
        service: PinRegistryService = Depends(services.get_pin_registry_service)
):
    return service.remove(collection, board_name, pin_name)
