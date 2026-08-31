from pydantic import BaseModel, Field
from enum import Enum
from typing import Literal

class City(str, Enum):
    kalyan = "Kalyan"
    srinagar = "Srinagar"
    hyderabad = "hyderabad"
    vasai_virar = "vasai_virar"
    lucknow = "lucknow"
    thane = "thane"
    ludhiana = "ludhiana"
    agra = "agra"
    surat = "surat"
    kolkata = "kolkata"
    jaipur = "jaipur"
    patna = "patna"
    visakhapatnam = "visakhapatnam"
    pune = "pune"
    ahmedabad = "ahmedabad"
    bhopal = "bhopal"
    chennai = "chennai"
    meerut = "meerut"
    rajkot = "rajkot"
    delhi = "delhi"
    bangalore = "bangalore"
    ghaziabad = "ghaziabad"
    mumbai = "mumbai"
    vadodara = "vadodara"
    varanasi = "varanasi"
    nagpur = "nagpur"
    indore = "indore"
    kanpur = "kanpur"
    nashik = "nashik"
    faridabad = "faridabad"

class SleepDuration(str, Enum):
    FIVE_TO_SIX = "5-6 hours"
    LESS_THAN_FIVE = "Less than 5 hours"
    SEVEN_TO_EIGHT = "7-8 hours"
    MORE_THAN_EIGHT = "More than 8 hours"
    OTHERS = "Others"

class DietaryHabits(str, Enum):
    HEALTHY = "Healthy"
    MODERATE = "Moderate"
    UNHEALTHY = "Unhealthy"
    OTHERS = "Others"

class Degree(str, Enum):
    CLASS_12 = "Class 12"
    B_ED = "B.Ed"
    B_COM = "B.Com"
    B_ARCH = "B.Arch"
    BCA = "BCA"
    MSC = "MSc"
    B_TECH = "B.Tech"
    MCA = "MCA"
    M_TECH = "M.Tech"
    BHM = "BHM"
    BSC = "BSc"
    MED = "M.Ed"
    B_PHARM = "B.Pharm"
    M_COM = "M.Com"
    BBA = "BBA"
    MBBS = "MBBS"
    LLB = "LLB"
    BE = "BE"
    BA = "BA"
    M_PHARM = "M.Pharm"
    MD = "MD"
    MBA = "MBA"
    MA = "MA"
    PHD = "PhD"
    LLM = "LLM"
    MHM = "MHM"
    ME = "ME"
    OTHERS = "Others"


class StudentDetails(BaseModel):
    gender : Literal["Male","Female"] = Field(default="Male")
    age : int = Field(default=18, ge=18)
    city : City
    academic_pressure : int = Field(default=1, ge=0, le=5)
    cgpa : float = Field(default=8.0,gt=2.0, le=10.0)
    study_satisfaction : int = Field(default=4, ge=0, le=5)
    sleep_duration : SleepDuration
    dietary_habits : DietaryHabits
    degree : Degree
    suicidal_thoughts : Literal["Yes","No"]
    work_study_hours : int = Field(default=3, ge=0, le=12)
    financial_stress : int = Field(default=2, ge=1, le=5)
    family_history_of_mental_illeness : Literal["Yes","No"]