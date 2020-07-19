from random import randint

from fastapi import APIRouter, Depends

from services.containers.service_container import ServiceContainer
from services.monitor.temperature_monitor_service import TemperatureMonitorService

router = APIRouter()

services = ServiceContainer.container()


@router.get('/')
def list_filter(
        service: TemperatureMonitorService = Depends(services.get_temperature_monitor_service)
):
    return service.filter()


@router.get('/all')
def list_all(
        service: TemperatureMonitorService = Depends(services.get_temperature_monitor_service)
):
    return service.list_all()


@router.delete('/purge')
def clean_up(
        service: TemperatureMonitorService = Depends(services.get_temperature_monitor_service)
):
    return service.clean_up()


@router.post('')
def insert(
        value: str = '',
        service: TemperatureMonitorService = Depends(services.get_temperature_monitor_service)
):
    value = str(randint(5, 30)) if not value else value
    return {
        'result': service.insert(value)
    }
