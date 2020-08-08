from random import randint

from fastapi import APIRouter, Depends

from services.containers.service_container import ServiceContainer
from services.monitor.moisture_monitor_service import MoistureMonitorService

router = APIRouter()

services = ServiceContainer.container()


@router.get('/?')
def list_filter(
        board_name: str,
        service: MoistureMonitorService = Depends(services.get_moisture_monitor_service)
):
    return service.filter(board_name)


@router.get('/all')
def list_all(
        service: MoistureMonitorService = Depends(services.get_moisture_monitor_service)
):
    return service.list_all()


@router.delete('/purge')
def clean_up(
        service: MoistureMonitorService = Depends(services.get_moisture_monitor_service)
):
    return service.clean_up()


@router.post('')
def insert(
        value: str = '',
        service: MoistureMonitorService = Depends(services.get_moisture_monitor_service)
):
    value = str(randint(5, 30)) if not value else value
    return {
        'result': service.insert(value)
    }
