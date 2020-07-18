from random import randint

from fastapi import APIRouter

from services.container import ServiceContainer

router = APIRouter()


@router.get('/')
def list_filter():
    service = ServiceContainer.get_iot_temperature_monitor_service()
    return service.filter()


@router.get('/all')
def list_all():
    service = ServiceContainer.get_iot_temperature_monitor_service()
    return service.list_all()


@router.get('/clean')
def clean_up():
    service = ServiceContainer.get_iot_temperature_monitor_service()
    return service.clean_up()


@router.get('/insert')
def insert():
    service = ServiceContainer.get_iot_temperature_monitor_service()

    value = str(randint(5, 30))

    result = service.insert(value)

    return {
        'result': result
    }
