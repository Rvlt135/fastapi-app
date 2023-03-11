import hashlib

from fastapi import APIRouter
from typing import List
from .models import fake_strain_list, clear_strain_list
from .shemas import Strain, StrainDetails

strain_router = APIRouter(
    prefix='/api/strain',
    tags=['strains'],

)


@strain_router.post('/add')
def add_strain(strain: List[Strain]):
    """Create strain and hash_id"""
    for it in strain:
        string_strain_slug_hash = it.slug_name
        result_hash = hashlib.md5(string_strain_slug_hash.encode()).hexdigest()
        it.hash_id = result_hash
        fake_strain_list.extend(strain)
        clear_strain_list.extend(strain)
        # fake_strain.extend(strain)
    return fake_strain_list


@strain_router.get('/list', response_model=List[Strain])
def get_strain_list():
    return fake_strain_list


@strain_router.get('/get_id', response_model=StrainDetails)
def get_strain(strain_id: int):
    for strain in fake_strain_list:
        # strain_dict = strain.dict()
        if strain.get("id") == strain_id:
            return strain
