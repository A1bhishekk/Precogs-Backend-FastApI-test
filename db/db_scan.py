from sqlalchemy.orm.session import Session
from schemas import ScanBase
from db.models import DbScan

def create_scan(db:Session,request:ScanBase):
    new_scan = DbScan(
        project_id=request.project_id,
        line_of_code=request.line_of_code,
        total_vul=request.total_vul,
        type_of_vul=request.type_of_vul,
        total_issues=request.total_issues
        )
    db.add(new_scan)
    db.commit()
    db.refresh(new_scan)

    return new_scan

def get_all_scans(db:Session):
    scans = db.query(DbScan).all()
    return scans


def delete_scan_by_id(db:Session,id:int):
    scan = db.query(DbScan).filter(DbScan.id==id).first()
    db.delete(scan)
    db.commit()
    return "ok"

def get_scan_by_id(db:Session,id:int):
    scan = db.query(DbScan).filter(DbScan.id==id).first()
    return scan

def get_dashboard(db:Session):
    scans = db.query(DbScan).all()
    return scans