from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from src.main.organization.schemas.section_schema import SectionCreate,SectionResponse
from src.main.organization.services.section_service import create_section, get_section_by_id
from src.main.organization.models.section import Section

router = APIRouter(prefix="/sections", tags=["Sections"])


@router.post("/", response_model=SectionResponse)
def create_new_section(section: SectionCreate):
    new_section = Section(head=section.head,address=section.address,name=section.name,
                          description=section.description,internalCode=section.internalCode,
                          phoneNum=section.phoneNum,sectionNum=section.sectionNum,
                          higherLevelSectionNum=section.higherLevelSectionNum)
    section_data = jsonable_encoder(create_section(new_section)[1])
    section_response = SectionResponse(**section_data)
    return section_response


@router.get("/{section_id}", response_model=SectionResponse)
def read_section(section_id: int):
    return get_section_by_id(section_id)
