from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_scan
from schemas import ScanBase, ScanDisplay
from sqlalchemy import func
from db.models import DbScan

router=APIRouter(
    prefix="/scans",
    tags=['Scans'],
)


# CREATE SCAN
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=ScanDisplay,summary="Create a new scan",)
def create_scan(request:ScanBase,db:Session=Depends(get_db)):
    return db_scan.create_scan(db,request)

# Get all scans
@router.get('/',status_code=status.HTTP_200_OK,response_model=list[ScanDisplay],summary="Get all scans",)
def get_scans(db:Session=Depends(get_db)):
    return db_scan.get_all_scans(db)

# Get scan by id
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ScanDisplay,summary="Get scan by id",)
def get_scan_by_id(id:int,db:Session=Depends(get_db)):
    return db_scan.get_scan_by_id(db,id)

# Delete scan by id
@router.delete('/{id}',status_code=status.HTTP_200_OK,summary="Delete scan by id",)
def delete_scan_by_id(id:int,db:Session=Depends(get_db)):
    return db_scan.delete_scan_by_id(db,id)



# dashboard
@router.get('/dashboard',status_code=status.HTTP_200_OK,summary="Get dashboard")
def get_dashboard(db:Session=Depends(get_db)):
    total_amount = db.query(func.sum(DbScan.line_of_code)).scalar()
    db.close()
    return {"total_amount":total_amount}
    